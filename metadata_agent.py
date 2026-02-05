import os

def analyze_metadata(file_path):
    size = os.path.getsize(file_path)

    if size < 50000:
        return {"risk": 0.5, "message": "Suspicious file size"}
    else:
        return {"risk": 0.2, "message": "Normal metadata"}