import os
import cv2
import numpy as np
from tqdm import tqdm

def convert_kitti_to_yolo(label_dir, image_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    label_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')]

    for label_file in tqdm(label_files):
        with open(os.path.join(label_dir, label_file), 'r') as f:
            lines = f.readlines()

        image_file = os.path.join(image_dir, label_file.replace('.txt', '.png'))
        image = cv2.imread(image_file)
        img_height, img_width = image.shape[:2]

        yolo_labels = []
        for line in lines:
            parts = line.strip().split()
            label = parts[0]
            if label not in ['Pedestrian', 'Car']:
                continue

            x_min = float(parts[4])
            y_min = float(parts[5])
            x_max = float(parts[6])
            y_max = float(parts[7])

            x_center = (x_min + x_max) / 2.0 / img_width
            y_center = (y_min + y_max) / 2.0 / img_height
            width = (x_max - x_min) / img_width
            height = (y_max - y_min) / img_height

            class_id = 0 if label == 'Pedestrian' else 1  # Assign class ids: Pedestrian = 0, Car = 1
            yolo_labels.append(f"{class_id} {x_center} {y_center} {width} {height}")

        with open(os.path.join(output_dir, label_file), 'w') as f:
            f.write("\n".join(yolo_labels))

if __name__ == "__main__":
    training_label_dir = r'C:\Users\n2309064h\Desktop\Complex-YOLOv3\data\KITTI\object\training\label_2'
    training_image_dir = r'C:\Users\n2309064h\Desktop\Complex-YOLOv3\data\KITTI\object\training\image_2'
    output_label_dir = r'C:\Users\n2309064h\Desktop\darknet\yolo_labels'

    convert_kitti_to_yolo(training_label_dir, training_image_dir, output_label_dir)
