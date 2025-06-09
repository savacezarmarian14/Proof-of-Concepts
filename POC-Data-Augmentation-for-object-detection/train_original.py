import sys
import os
import argparse

YOLOV5_PATH = os.path.join(os.path.dirname(__file__), 'yolov5')
if YOLOV5_PATH not in sys.path:
    sys.path.append(YOLOV5_PATH)

from train import run  


def main():
    parser = argparse.ArgumentParser(description="YOLOv5 Training Wrapper")

    parser.add_argument('--img', type=int, default=640, help='Image size')
    parser.add_argument('--batch', type=int, default=16, help='Batch size')
    parser.add_argument('--epochs', type=int, default=30, help='Number of epochs')
    parser.add_argument('--data', type=str, default='dataset_original.yaml', help='Path to data.yaml')
    parser.add_argument('--weights', type=str, default='yolov5s.pt', help='Initial weights')
    parser.add_argument('--name', type=str, default='train_original', help='Experiment name')
    parser.add_argument('--project', type=str, default='results', help='Path to project directory (can be custom)')
    parser.add_argument('--device', type=str, default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')

    args = parser.parse_args()

  
    os.makedirs(args.project, exist_ok=True)

    run(
        img=args.img,
        batch=args.batch,
        epochs=args.epochs,
        data=args.data,
        weights=args.weights,
        project=args.project,
        name=args.name,
        device=args.device,
        exist_ok=True
    )


if __name__ == '__main__':
    main()
