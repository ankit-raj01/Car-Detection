# Converting image sequence to video

import cv2 as cv
import os

def image_to_video():
    image_folder = 'rgb_imgs' 
    video_name = 'rgb_vid.avi'
    os.chdir('C:\\Users\\Acer\\Desktop\\OpenCV Hackathon')
    images = [img for img in os.listdir(image_folder)]
    frame = cv.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape  
    video = cv.VideoWriter(video_name, 0, 1, (width, height)) 

    for image in images:
        video.write(cv.imread(os.path.join(image_folder, image))) 

    cv.destroyAllWindows()

    video.release() 

image_to_video()