import cv2
import os

# define video directory
o = "C:/Users/yuego/Downloads/JAV_"
d = "C:/Users/yuego/Downloads/JAV"

file_list = os.listdir(d)
print(file_list)

for file_name in file_list:
    video_file = os.path.join(d, file_name)
    output_file = os.path.join(o, file_name)

    # capture from a video file
    cap = cv2.VideoCapture(video_file)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = round(cap.get(cv2.CAP_PROP_FPS), 0)
    fourcc = str(cap.get(cv2.CAP_PROP_FOURCC))
    print("Video length: ", length)
    print("Video frame width: ", width)
    print("Video frame length: ", height)
    print("Video FPS: ", fps)
    print("FourCC: ", fourcc)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file ,fourcc, fps, (int(width*0.25),int(height*0.25)), True)

    counter = 0
    segment_count = 10

    # calculate frame position at every 1/10 of video length
    positions = []
    p = int(length / segment_count)
    for i in range(segment_count):
        positions.append(p * i)

    print(positions)

    for i in range(segment_count):
        cap.set(cv2.CAP_PROP_POS_FRAMES, positions[i])
        counter = 0
        while(cap.isOpened()):
            ret, frame = cap.read()
            if counter > fps:
                break
            elif ret == True:
                counter += 1
                frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
                out.write(frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
