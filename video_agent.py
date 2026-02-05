import cv2
import numpy as np

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)
    blur_scores = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.Laplacian(gray, cv2.CV_64F).var()
        blur_scores.append(blur)

    cap.release()
    avg_blur = np.mean(blur_scores)

    if avg_blur < 100:
        return {"risk": 0.7, "message": "Low facial detail detected"}
    else:
        return {"risk": 0.3, "message": "Video looks natural"}