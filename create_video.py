import os
import cv2
import numpy as np
from tqdm import tqdm
from PIL import Image
from PIL import ImageFile
from natsort import natsorted

data_folder = 'G:\\Meine Ablage\\DATASETS\\tuning\\11\\10\\'


def open_tga(path):
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    images = [x for x in os.listdir(path)]
    natsorted(images)
    im = Image.open(os.path.join(path, images[0])).convert('RGB')
    open_cv_image = np.array(im)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    writer = cv2.VideoWriter("video50fps.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 50,
                             (int(open_cv_image.shape[1]), int(open_cv_image.shape[0])))
    for i in tqdm(range(len(images))):
        im = Image.open(os.path.join(path, images[i])).convert('RGB')
        open_cv_image = np.array(im)
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        writer.write(open_cv_image)
    writer.release()


if __name__ == '__main__':
    open_tga(data_folder)
