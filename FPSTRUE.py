import os
import cv2
import numpy as np
from tqdm import tqdm
from PIL import Image
from PIL import ImageFile
from natsort import natsorted

"""
Exposuretimes = [50, 100, 150, 250, 400, 650, 1050, 1700, 2750]
[0.75, 1.5, 2.25, 3.75, 6.0, 9.75, 15.75, 25.5, 41.25]
[1, 2, 2, 4, 6, 10, 16, 26, 41]

FPSframrate = [50ms, 100ms, 150ms, 250ms, 400ms, 650ms, 1050ms, 1700ms, 2750ms]
in sum 7100 ms = 7,1s
"""


def fps_custom(path):
    exposure_times = {'50': 30, '100': 20, '150': 3, '250': 5, '400': 8, '650': 13, '1050': 21, '1700': 34, '2750': 45}
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    images = [x for x in os.listdir(path)]
    images = natsorted(images)
    im = Image.open(os.path.join(path, images[0])).convert('RGB')
    open_cv_image = np.array(im)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    writer = cv2.VideoWriter("videoXX.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 1,
                             (int(open_cv_image.shape[1]), int(open_cv_image.shape[0])))
    writer_new = cv2.VideoWriter("video_newXX.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 15,
                                 (int(open_cv_image.shape[1]), int(open_cv_image.shape[0])))
    image_list_fps = []
    for i in tqdm(range(len(images))):
        exposure_time = images[i].split(".")[0].split("_")[1]
        im = Image.open(os.path.join(path, images[i])).convert('RGB')
        open_cv_image = np.array(im)
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        for i in range(int(exposure_times[str(exposure_time)])):
            image_list_fps.append(open_cv_image)
        writer.write(open_cv_image)
    writer.release()
    for open_cv_image in tqdm(image_list_fps):
        writer_new.write(open_cv_image)
    writer_new.release()


def open_tga(path):
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    images = [x for x in os.listdir(path)]
    images = natsorted(images)
    im = Image.open(os.path.join(path, images[0])).convert('RGB')
    open_cv_image = np.array(im)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    writer = cv2.VideoWriter("videoXX.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 15,
                             (int(open_cv_image.shape[1]), int(open_cv_image.shape[0])))
    for i in tqdm(range(len(images))):
        im = Image.open(os.path.join(path, images[i])).convert('RGB')
        open_cv_image = np.array(im)
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        writer.write(open_cv_image)
    writer.release()


if __name__ == '__main__':
    data_folder = 'C:\\Users\\PaulM\\PycharmProjects\\videoskyimages\\19'
    fps_custom(data_folder)
# open_tga(data_folder)
