#import the open source computer vision (cv2) and the time module 
import cv2, time, pandas
from datetime import datetime

#providing none parameter to the first frame 
first_frame = None

status_capture = [None, None]

times = []

df = pandas.DataFrame(columns=["Start","End"])

#start to capture the video
video = cv2.VideoCapture(0)

while True:
#checks the first frame
	check, frame = video.read()

	status = 0

#checks the gray intensity of the first frame
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#generates a blur image for the original image, (21,21) are standard parametrics and 0 is SD. You can change if you want. 
#SD is used to quantify the amount of variation or dispersion from  a set of data values
	gray = cv2.GaussianBlur(gray,(21,21),0)

#check if first image is None type and if yes, it makes it gray and continues the loop from the top (from while) again. 
#If it's not the None type, it doesn't go through the loop again and directly runs from after continue 
	if first_frame is None:
		first_frame = gray
		continue

#This frame checks for the difference between the first frame and gray frame
	delta_frame = cv2.absdiff(first_frame,gray)

#anything more than 30 intensity is assigned to white 
#using the threshold binary method here (THRESH_BINARY) WHICH RETURNS TUPLE
#you just need to access the second item of the tuple which is the actual frame hence using [1]
	threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

#To remove the extra white spots from the capture, more iterations = more clarity in the picture
	threshold_frame = cv2.dilate(threshold_frame, None, iterations = 1)

#find contours basically checks for continuity in the image and finds its location 
	(_,cnts,_) = cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#contourarea continuously checks for area > than 10000 and repeats that process
#once found it frames the coordinates in green color as a bounding rectangle 
	for contour in cnts:
		if cv2.contourArea(contour) < 10000:
			continue
		status = 1
		(x, y, w, h) = cv2.boundingRect(contour)
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
	status_capture.append(status)
	if status_capture[-1] == 1 and status_capture[-2] == 0:
		times.append(datetime.now())
	if status_capture[-1] == 0 and status_capture[-2] == 1:
		times.append(datetime.now())

#Open 2 windows which shows the gray frame and the new difference frame
	cv2.imshow("Gray Frame",gray)
	cv2.imshow("Variation Frame",delta_frame)
	cv2.imshow("Threshold Frame", threshold_frame)
	cv2.imshow("Color frame", frame)

#captures the video to the precesion of 1ms and could be changed to see the difference
	key = cv2.waitKey(1)

#print the gray and delta frame arrays (for checking the difference manually)
	print(gray)
	print(delta_frame)

#Use the 'q' key to break through the loop and stop the whole process
	if key == ord('q'):
		if status == 1:
			times.append(datetime.now())
		break

print(status_capture)
print(times)

for i in range(0, len(times),2):
	df = df.append({"Start":times[i],"End":times[i+1]}, ignore_index = True)

df.to_csv("Times.csv")

#releases the video and destroys all windows which are running through this code. 
video.release()
cv2.destroyAllWindows()
