import cv2
import os
from pathlib import Path
from PIL import Image

from OctTree_image_quantization import OctTree


class VideoColourReduce:
    """TODO"""
    def __init__(self, video_file):
        self.video_file = video_file
        self.video_name = str(video_file).rstrip(".mp4")
        self.frames_output_dir = f"./{self.video_name}_frames"
        self.reduced_frames_dir = f"./{self.video_name}_rframes"
        self.frames_list = os.listdir(self.frames_output_dir)
        os.makedirs(self.frames_output_dir, exist_ok=True)
        os.makedirs(self.reduced_frames_dir, exist_ok=True)

    def video_to_frames(self):
        """TODO"""
        vidcap = cv2.VideoCapture(self.video_file)
        count = 0
        while vidcap.isOpened():
            success, image = vidcap.read()
            if success:
                print(f"Extracting frame {count}...")
                frame_path = os.path.join(self.frames_output_dir, "%d.png") % count
                cv2.imwrite(frame_path, image)
                self.frames_list.append(frame_path)
                count += 1
            else:
                break
        cv2.destroyAllWindows()
        vidcap.release()

    def reduce_frame_colours(self):
        """TODO"""
        for frame in self.frames_list:
            print(f"Reducing {frame}...")
            im = Image.open(os.path.join(self.frames_output_dir, frame))
            w, h = im.size
            ot = OctTree()

            for row in range(0, h):
                for col in range(0, w):
                    r, g, b = im.getpixel((col, row))
                    ot.insert(r, g, b)

            ot.reduce(8)

            for row in range(0, h):
                for col in range(0, w):
                    r, g, b = im.getpixel((col, row))
                    nr, ng, nb = ot.find(r, g, b)
                    im.putpixel((col, row), (nr, ng, nb))

            im.save(os.path.join(self.frames_output_dir, frame))



vidya = VideoColourReduce("birb.mp4")
# vidya.video_to_frames()
vidya.reduce_frame_colours()
print("done")