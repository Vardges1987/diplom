import os
import cv2
import logging

logging.basicConfig(filename='puzzle_pieces.log', level=logging.DEBUG)


def slice_and_save_puzzle_pieces(level, image_path, output_dir, rows, cols):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image at path '{image_path}' not found.")

    target_width, target_height = 550, 550
    image = cv2.resize(image, (target_width, target_height), interpolation=cv2.INTER_AREA)

    piece_height = target_height // rows
    piece_width = target_width // cols

    pieces_data = []

    for i in range(rows):
        for j in range(cols):
            y1, y2 = i * piece_height, (i + 1) * piece_height
            x1, x2 = j * piece_width, (j + 1) * piece_width
            piece = image[y1:y2, x1:x2]

            if piece.size == 0:
                continue

            piece_filename = f"piece_{level.id}_{i}_{j}.png"
            piece_path = os.path.join(output_dir, piece_filename)

            cv2.imwrite(piece_path, piece)

            pieces_data.append({
                'level': level,
                'image': f'static/images/{piece_filename}',
                'position_x': j,
                'position_y': i,
                'is_solved': False,
            })

    return pieces_data
