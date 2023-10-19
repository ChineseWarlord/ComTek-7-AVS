import cv2 as cv
import os
from glob import glob

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

if __name__=='__main__':
    clips = glob(os.path.join('data/clips/', '*/*.mp4'))
    for clip in clips:
        make_frames(clip)