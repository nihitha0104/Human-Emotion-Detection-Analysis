# Video Emotion Detection with DeepFace

This repository contains a script that processes a video file to detect and annotate emotions on detected faces using the DeepFace library. The processed video is saved with the annotations.

## Requirements
- Python 3.x
- OpenCV
- DeepFace
- Google Colab (for mounting Google Drive)

## Installation

First, clone the repository and navigate into the project directory:

```command prompt
git clone <repository_url>
cd <repository_directory>
```

Then, install the required packages:
```python
pip install deepface
pip install opencv-python
```

## Usage

### Mount Google Drive

If you are running this script in Google Colab, you need to mount your Google Drive to access the video file:

```python
from google.colab import drive
drive.mount('/content/drive')
```
## Set Video Path
Set the path to your video file stored in Google Drive:

```python
video_path = "/content/drive/MyDrive/VID-20230914-WA0005.mp4"
```
## Run the Script
The human-emotion.py script reads the video file, detects faces in each frame, analyzes the emotions on those faces, and annotates the frames with the dominant emotion.

## Output
The script will generate a video file named Emotions.avi with the annotated emotions for each detected face.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
* DeepFace
* OpenCV
Feel free to contribute to this project by submitting issues or pull requests.
