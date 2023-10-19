import cv2 as cv
import os

def make_frames(clip_dir):
    pathOut = clip_dir.replace('.mp4','')
    if not os.path.exists(pathOut):
        os.makedirs(pathOut)
    vidcap = cv.VideoCapture(clip_dir)
    count = 0
    success = True
    while success:
        success,image = vidcap.read()
        # print('read a new frame:',success)
        frame_path = os.path.join(pathOut, 'frame_%s.jpg'%'{0:04}'.format(int(count/25)))
        anno_path = frame_path.replace('clips','annotations').replace('jpg', 'txt').replace('frame', 'annotations')
        if count%25 == 0 and os.path.isfile(anno_path):
            cv.imwrite(frame_path, image)
        count+=1