import os
import glob
import shutil
from argparse import ArgumentParser
from tqdm import tqdm
from botocore.exceptions import ClientError
from fr.core import Fr
from fr.util import draw_matched_face_positions


parser = ArgumentParser()
parser.add_argument('template_dir', type=str, help="face templates directory")
parser.add_argument('target_pictures_dir', type=str)
parser.add_argument('-o', '--output_dir', type=str, default="output")
parser.add_argument('--region', type=str, default="us-west-2", help="AWS region name")
parser.add_argument('--th', type=int, default=80, help="similarity threshold")

args = parser.parse_args()


face_template_files = sorted(glob.glob(os.path.join(args.template_dir, "*.jpg")))
print(f"Found {len(face_template_files)} templates")

album_dirs = sorted(os.listdir(args.target_pictures_dir))
album_dirs = [x for x in album_dirs if os.path.isdir(os.path.join(args.target_pictures_dir, x))]
print(f"Found {len(album_dirs)} albumns", album_dirs)
print("\n")

fr = Fr(region=args.region)

reject_target_files = []
for face_template_file in face_template_files:
    user_name = os.path.splitext(os.path.basename(face_template_file))[0]
    user_output_dir = user_name
    os.makedirs(user_output_dir, exist_ok=True)
    print(f"[{user_name}]")

    for album_dir in album_dirs:
        match_cnt = 0
        target_files = glob.glob(os.path.join(args.target_pictures_dir, album_dir, "*.jpg"))
        target_files.extend(glob.glob(os.path.join(args.target_pictures_dir, album_dir, "*.JPG")))
        target_files = [filename for filename in target_files if filename not in reject_target_files]
        for target_file in tqdm(target_files):
            try:
                res = fr.compare_faces(face_template_file, target_file, args.th)
            except ClientError as e:
                print(f"Couldn't match faces from {face_template_file} to {target_file}.")
                reject_target_files.append(target_file)
                continue

            if len(res["FaceMatches"]):
                user_album_output_dir = os.path.join(args.output_dir, "raw", user_output_dir, album_dir)
                os.makedirs(user_album_output_dir, exist_ok=True)
                shutil.copy(target_file, user_album_output_dir)

                user_marker_output_dir = os.path.join(args.output_dir, "marker", user_output_dir, album_dir)
                os.makedirs(user_marker_output_dir, exist_ok=True)
                marked_file = os.path.join(user_marker_output_dir, os.path.basename(target_file))
                draw_matched_face_positions(target_file, marked_file, res['FaceMatches'])
                match_cnt += 1

        print(f"{album_dir}: match cnt={match_cnt}")
