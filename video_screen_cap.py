import cv2
import os
import sys
from PIL import Image

# define video directory
d = "D:/Work Related/A3"
o = "C:/Users/yuego/Downloads/Screen_Caps"

file_list = os.listdir(d)

for file_name in file_list:
    video_file = os.path.join(d, file_name)
    output_file = os.path.join(o, os.path.splitext(file_name)[0] + '.jpg')
    print(file_name)

    # capture video file properties
    cap = cv2.VideoCapture(video_file)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = round(cap.get(cv2.CAP_PROP_FPS), 0)
    fourcc = str(cap.get(cv2.CAP_PROP_FOURCC))
    # print("Video length: ", length)
    # print("Video frame width: ", width)
    # print("Video frame length: ", height)
    # print("Video FPS: ", fps)
    # print("FourCC: ", fourcc)

    # Define the codec and set processing parameters
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    segment_count = 60

    # calculate frame position by dividing total length by segment count
    positions = []
    p = int(length / segment_count)
    for i in range(segment_count):
        positions.append(p * i)

    # read video frame at specific location and save the frame to a list
    frame_list = []
    for i in range(segment_count):
        cap.set(cv2.CAP_PROP_POS_FRAMES, positions[i])
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
                frame_list.append(frame)
                sys.stdout.write("==>   %d  \r" % (i) )
                sys.stdout.flush()
                break
            else:
                break

    # Release everything if job is finished
    cap.release()
    cv2.destroyAllWindows()

    # merge frames into a single image
    horizonal_length = 5
    vertical_length = int(segment_count / horizonal_length)
    im = Image.fromarray(frame_list[0])
    frame_width = im.width
    frame_height = im.height
    width = frame_width * horizonal_length
    height = frame_height * vertical_length
    new_image = Image.new('RGB', (width, height))

    frame_index = 0
    y_offset = 0
    for i in range(vertical_length):
        x_offset = 0
        for j in range(horizonal_length):
            im = frame_list[frame_index]
            pil_im = Image.fromarray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
            new_image.paste(pil_im, (x_offset, y_offset))
            x_offset += frame_width
            frame_index += 1
        y_offset += frame_height

    # save the final image
    new_image.save(output_file)
