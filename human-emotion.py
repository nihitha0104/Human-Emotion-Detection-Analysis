from google.colab import drive #Import the Google Colab library for mounting Google Drive.
drive.mount('/content/drive') #Mount Google Drive to the specified path

!pip install deepface #Install the "deepface" library using the pip package manager.
from deepface import DeepFace #Import the DeepFace module from the deepface library.

video_path = "/content/drive/MyDrive/VID-20230914-WA0005.mp4" #Set the variable`video_path` to the path of a video file on Google Drive. 

import cv2 #Import the OpenCV library.

capture = cv2.VideoCapture(video_path) #Create a VideoCapture object to capture video frames from the specified `video_path`.
#Load a pre-trained Haar Cascade classifier for detecting faces from the OpenCV data directory

face_model = 
cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
#Initialize an empty list to store processed frames 

frame_list=[]
while True:
    ret, frame = capture.read() #Read a frame from the video and store it in the `frame` variable.
    if not ret: # Check if the frame is valid
        break # Exit the loop if there are no more frames
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Convert the frame to grayscale.
    faces = face_model.detectMultiScale(gray_frame, 1.1, 5) #Detect faces in the grayscale frame using the Haar Cascade classifier.
    if len(faces) == 0: #If no faces are detected, continue to the next iteration of the loop.
        continue # Skip this frame and go to the next one
    for (x, y, width, height) in faces:
        face_roi = gray_frame[y:y + height, x:x + width] #Extract the region of interest (ROI) for each detected face.
    if len(face_roi.shape) == 2: #If the face ROI is 2-dimensional (grayscale), convert it to RGB.
        face_roi = cv2.cvtColor(face_roi, cv2.COLOR_GRAY2RGB) #Convert the grayscale face ROI to RGB.
# Analyze the emotion on the face_roi using the DeepFace library.
    emotion_list = DeepFace.analyze(face_roi, actions=["emotion"], enforce_detection=False)
# Check if any face is detected in the ROI
    if len(emotion_list) > 0:
        dominant_emotion = emotion_list[0]['dominant_emotion'] #Get the dominant emotion from the analysis.
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2) #Draw a rectangle around the detected face.
        cv2.putText(frame, dominant_emotion, (x, y - 10),
cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 0), 2) #Put text indicating the dominant emotion near the detected face.
else:
# Handle the case when no face is detected in the ROI
    print("No face detected in the ROI")
# Continue with the rest of your code...
    frame_list.append(frame) #Add the processed frame to the `frame_list`. 
capture.release() #Release the video capture object.
# Check if at least one frame with a face was processed
11 
if frame_list:
    height, width, colors = frame_list[0].shape #Get the dimensions of the first processed frame.
    size = (width, height)
    output_path = "Emotions.avi" #Set the output video file path
    output = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"DIVX"), 30, size) 
#Create a VideoWriter object for writing the output video.
    for frame in frame_list:
        output.write(frame) #Write each frame to the output video
        output.release() # Release the output video writer.
        cv2.destroyAllWindows() #Close all OpenCV windows.
    else: #If no frames with detected faces were processed
        print("No frames with detected faces were processed.")
