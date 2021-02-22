import os
from multiprocessing import Pool, freeze_support
from pathlib import Path

import cv2
from PIL import Image

from OctTree_image_quantization import OctTree


class VideoColourReduce:
    """Reduce a video's colours to the 8 most used colours, averaged using frame
    by frame OctTree image quantization.
    """
    def __init__(self, video_file):
        self.video_file_path = video_file
        self.frames_output_dir = Path(os.path.join(
            self.video_file_path.parent,
            f"./{self.video_file_path.name}_frames"))
        self.video_fps = None
        self.frames_list = []
        os.makedirs(self.frames_output_dir, exist_ok=True)

    def get_fps(self, vidcap_obj):
        """Return the FPS of a video"""
        # Find OpenCV version
        (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
        if int(major_ver) < 3:
            fps = vidcap_obj.get(cv2.cv.CV_CAP_PROP_FPS)
        else:
            fps = vidcap_obj.get(cv2.CAP_PROP_FPS)

        return fps

    def video_to_frames(self):
        """Output to folder PNG files for each frame of the video."""
        vidcap = cv2.VideoCapture(str(self.video_file_path))
        self.video_fps = self.get_fps(vidcap)
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

    def frames_to_video(self):
        """Create a video from a folder of images. FPS is matched to original video."""
        img = cv2.imread(self.frames_list[0])
        height, width, layers = img.shape
        size = (width, height)
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter(
            f"{self.video_file_path.name}_reduced.avi",
            fourcc,
            self.video_fps,
            size
        )
        for frame in self.frames_list:
            img = cv2.imread(frame)
            out.write(img)
        out.release()

    def reduce_frame_colours(self, start_frame, end_frame):
        """Run OctTree image quantization on each in the video frames output dir."""
        for frame_num in range(start_frame, end_frame):
            print(f"Reducing {frame_num}...")
            im = Image.open(os.path.join(
                self.frames_output_dir,
                self.frames_list[frame_num])
            )
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

            im.save(os.path.join(
                self.frames_output_dir,
                self.frames_list[frame_num]
            ))

    def process_video(self):
        """Read video, process to frames, quantize and process back to video."""
        self.video_to_frames()
        num_frames = len(self.frames_list)
        multi_args = [
            (i, i+num_frames // 7)
            if i+num_frames//7 < num_frames
            else (i, num_frames)
            for i in range(0, num_frames, num_frames // 7)
        ]

        with Pool() as pool:
            pool.starmap(self.reduce_frame_colours, multi_args)

        self.frames_to_video()
        print("Done")


if __name__ == "__main__":
    video_file_path = Path("example.mp4")
    vidya = VideoColourReduce(video_file_path)
    freeze_support()
    vidya.process_video()
