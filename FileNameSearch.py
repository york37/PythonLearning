import os
import shutil


d = "D:/Work Related/Web Capture"
md = "D:/Duplicate"
dir_list = os.listdir(d)



video_list = []
video_path = []
duplicate = []

for dir_name in dir_list:
    dd = os.path.join(d, dir_name)
    if os.path.isdir(dd):
        file_list = os.listdir(dd)
        for file_name in file_list:
            try:
                index = video_list.index(file_name)
                duplicate.append(video_path[index])
                duplicate.append(os.path.join(dd, file_name))
                #shutil.move(os.path.join(dd, file_name), os.path.join(md, file_name))
            except:
                video_list.append(file_name)
                video_path.append(os.path.join(dd, file_name))


print(len(video_list))
print(len(duplicate))

with open('D:/video_file.txt', 'w') as video_file:
    for file_name in duplicate:
        video_file.write(file_name + "\n")
