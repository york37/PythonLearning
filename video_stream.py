import cv2

cap = cv2.VideoCapture("https://ic-63f06c00-0ee256-23c3605.d.rncdn3.com/videos/201702/13/106086102/720P_1500K_106086102.mp4?ipa=99.240.108.14&rs=235&ri=1200&s=1496591085&e=1496598285&h=76f1718399f4d8c39132d12f71e1dc46")

# capture from a video file
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
out = cv2.VideoWriter("output.mp4" ,fourcc, fps, (int(width*0.25),int(height*0.25)), True)

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
    print("==>", positions[i])
    counter = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if counter > fps:
            break
        elif ret == True:
            counter += 1
            frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
            out.write(frame)
        else:
            break



# while(cap.isOpened()):
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

cap.release()
out.release()
cv2.destroyAllWindows()
