from PIL import Image, ImageDraw


def draw_matched_face_positions(imageFile, outFile, matched_faces, margin_ratio=0.1, outline=(255, 255, 0), outline_width=4):
    im = Image.open(imageFile)
    img_width, img_height = im.size

    draw = ImageDraw.Draw(im)

    for matched_face in matched_faces:
        position = matched_face['Face']['BoundingBox']
        left = position['Left'] * img_width
        upper = position['Top'] * img_height
        width = position['Width'] * img_width
        height = position['Height'] * img_height

        h_margin = width * margin_ratio
        v_margin = height * margin_ratio

        right = left + width
        lower = upper + height

        left = max(left - h_margin, 0)
        right = min(right + h_margin, img_width-1)
        upper = max(upper - v_margin, 0)
        lower = min(lower + v_margin, img_height-1)
        area = (left, upper, right, lower)

        draw.rectangle(area, fill=None, outline=outline, width=outline_width)

    im.save(outFile, quality=95)
