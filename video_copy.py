import cv2
import os

# capture from a camera
# cap = cv2.VideoCapture(0)

# capture from a video file
cap = cv2.VideoCapture('sample.mp4')
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
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# fourcc = cv2.VideoWriter_fourcc(*'CVID')
# fourcc = cv2.VideoWriter_fourcc(*'MSVC')
# fourcc = cv2.VideoWriter_fourcc(*'X264')
# fourcc = -1

# out_1 = cv2.VideoWriter('sample_2.mp4',fourcc, fps, (width,height), True)
out_2 = cv2.VideoWriter('output_20.mp4',fourcc, fps, (320,180), True)
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1280,720), True)

counter = 0
cap_counter = 0
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
            out_2.write(frame)
            print(counter)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break


#
# # capture video segments
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if counter == 0:
#         break
#     elif ret == True:
#         # cv2.imshow('frame',frame)
#         counter += 1
#
#         if counter % fps == 0:
#             # cv2.imwrite(os.path.join('%d.png') % counter, frame)
#             # out_1.write(frame)
#
#             frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
#             out_2.write(frame)
#             print(counter)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break

# Release everything if job is finished
cap.release()
# out_1.release()
out_2.release()
cv2.destroyAllWindows()
