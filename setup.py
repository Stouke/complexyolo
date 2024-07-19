import os
import glob

def prepare_yolo_dataset(image_dir, label_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    images = glob.glob(os.path.join(image_dir, '*.png'))
    with open(os.path.join(output_dir, 'train.txt'), 'w') as f:
        for image in images:
            f.write(f"{os.path.abspath(image)}\n")

    with open(os.path.join(output_dir, 'classes.names'), 'w') as f:
        f.write("Pedestrian\nCar\n")

    with open(os.path.join(output_dir, 'yolov3.data'), 'w') as f:
        f.write(f"classes= 2\n")
        f.write(f"train= {os.path.join(output_dir, 'train.txt')}\n")
        f.write(f"valid= {os.path.join(output_dir, 'train.txt')}\n")
        f.write(f"names= {os.path.join(output_dir, 'classes.names')}\n")
        f.write(f"backup= backup/\n")

if __name__ == "__main__":
    image_dir = r'C:\Users\n2309064h\Desktop\Complex-YOLOv3\data\KITTI\object\training\image_2'
    label_dir = 'yolo_labels'  # Directory containing the converted YOLO labels
    output_dir = r'C:\Users\n2309064h\Desktop\darknet\yolo_data'

    prepare_yolo_dataset(image_dir, label_dir, output_dir)
