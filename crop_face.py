import os
from argparse import ArgumentParser
from fr.core import Fr
from fr.util import save_face


parser = ArgumentParser()
parser.add_argument('inputfile', type=str)
parser.add_argument('output_dir', type=str, default="output")
parser.add_argument('--region', type=str, default="us-west-2", help="AWS region name")

args = parser.parse_args()

fr = Fr(region=args.region)
res = fr.detect_faces(args.inputfile)
if len(res['FaceDetails']):
    os.makedirs(args.output_dir, exist_ok=True)
print(f"{args.inputfile}: Found {len(res['FaceDetails'])} faces")

for i, faceDetail in enumerate(res['FaceDetails']):
    output_filename = os.path.join(args.output_dir, f"{os.path.basename(args.inputfile)}_{i+1}.jpg")
    save_face(args.inputfile, output_filename, faceDetail["BoundingBox"])
