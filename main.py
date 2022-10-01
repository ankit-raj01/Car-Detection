import cv2 as cv

capture = cv.VideoCapture('rgb_vid.avi')                                                        # Reading Video

def empty(a):
    pass
cv.namedWindow('TrackBars')
cv.resizeWindow('TrackBars', 640, 240)
cv.createTrackbar('Threshold 1', 'TrackBars', 4, 255, empty)                                    # Using optimum threshold values
cv.createTrackbar('Threshold 2', 'TrackBars', 8, 255, empty)                        

def f(img, count):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        perimeter = cv.arcLength(cnt, True)                                                     # Finding perimeter of the contour
        approx = cv.approxPolyDP(cnt, 0.02 * perimeter, True)                                   # Finding corner points of the contour                       
        x, y, w, h = cv.boundingRect(approx)                                                    # Finding coordinates of origin(x, y), width(w) and height(h) of the rectagle which is bounding contour
        
        
        if (w ** 2 + h ** 2) ** 0.5 > 150 and w > 61:                                           # Applying condition to remove small bounding boxes
            cv.rectangle(img_contour, (x, y), (x + w, y + h), (0, 255, 0), 2)                   # Drawing rectangles
            count[0] += 1
            current_frame = str(count[0]) + ' of 3103'                                         
            cv.putText(img_contour, current_frame, (x + 2, y + 15), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)                  # Putting text inside rectangle depicting current frame sequence     

count = [0]
# output_video = cv.VideoWriter('rgb_vid_output.avi', 0, 1, (640, 480))                         # Line commented after saving the final output video

while(capture.isOpened()):
    isTrue, frame = capture.read()
    if isTrue:
        bilateral = cv.bilateralFilter(frame, 5, 80, 200, borderType = cv.BORDER_CONSTANT)      # Applying Bilateral Filter     
        gray = cv.cvtColor(bilateral, cv.COLOR_BGR2GRAY)                                        # Converting to Grayscale
        Threshold1 = cv.getTrackbarPos('Threshold 1', 'TrackBars')
        Threshold2 = cv.getTrackbarPos('Threshold 2', 'TrackBars')
        canny = cv.Canny(gray, Threshold1, Threshold2)                                          # Applying Canny edge detector
        dilated = cv.dilate(canny, (7, 7), iterations = 4)                                      # Applying Dilation             
        img_contour = frame.copy()
        f(dilated, count)
        # output_video.write(img_contour)                                                       # Line commented after saving the final output video
        cv.imshow('Original Video', frame)
        # cv.imshow('Blurred Video', bilateral)
        # cv.imshow('Canny', canny)
        # cv.imshow('Dilated', dilated)
        cv.imshow('Output Video', img_contour)                                                  # Displaying Output Video
        if cv.waitKey(1000) & 0xFF == ord('q'):                                                 # Will break after completion of video or if key 'q' is pressed
            break
    else:        
        break                                                                                   # Applying break condition to avoid error after video(frame) ends

capture.release()
# output_video.release()                                                                        # Line commented after saving the final output video

cv.destroyAllWindows()