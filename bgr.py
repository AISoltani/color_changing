import cv2
import os



mask_folders = os.listdir('test')
mask_folders = [y for y in mask_folders if ("." not in y)]

for mask_folder in mask_folders:
    srcBGR = cv2.imread("test/"+mask_folder+".png")
    destRGB = cv2.cvtColor(srcBGR, cv2.COLOR_BGR2RGB)
    window_name = 'image'
    cv2.imwrite("BGR_Final_Data/test/"+mask_folder+".png", destRGB)
  
