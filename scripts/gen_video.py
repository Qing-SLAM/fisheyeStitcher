import os
import cv2
import numpy as np
from glob import glob
from tqdm import tqdm


train_list=["2013_05_28_drive_0000_sync"
            "2013_05_28_drive_0002_sync" 
	        "2013_05_28_drive_0003_sync"
            "2013_05_28_drive_0004_sync" 
            "2013_05_28_drive_0005_sync" 
            "2013_05_28_drive_0006_sync" 
            "2013_05_28_drive_0007_sync" 
            "2013_05_28_drive_0009_sync" 
	        "2013_05_28_drive_0010_sync"]

for data_path in train_list:

    files_1 = sorted(glob("/disk1/KITTI-360/data_2d_raw/{}/image_02/data_rgb/*.png".format(data_path)))
    files_2 = sorted(glob("/disk1/KITTI-360/data_2d_raw/{}/image_03/data_rgb/*.png".format(data_path)))

    count = 0
    for im1, im2 in tqdm(zip(files_1, files_2), total=len(files_1)):
        im1 = cv2.imread(im1)
        im2 = cv2.imread(im2)
        im1 = cv2.resize(im1, (1920, 1920))
        im2 = cv2.resize(im2, (1920, 1920))
        im_h = cv2.hconcat([im1, im2])
        cv2.imwrite('temp/{:06}.png'.format(count), im_h)
        count+=1
    os.system('ffmpeg -i temp/%06d.png -vcodec libx264 -pix_fmt yuv420p {}_video.mp4'.format(data_path))