# Human Pose Estimation Using Python

## Project Overview
This project detects human body landmarks from a video using **MediaPipe Pose** and **OpenCV**.

It generates two output videos:
1. **Original Video with Pose:** Displays the original video with a detected human skeleton overlay.
2. **Skeleton Only:** Displays the detected body skeleton on a black background.

## Technologies Used
- Python 3.12
- OpenCV
- MediaPipe
- NumPy

## Project Files
- `pose_detection.py` – Main Python program for pose detection.
- `input_video.mp4` – Input video.
- `original_with_pose.mp4` – Output video with skeleton overlay.
- `skeleton_only.mp4` – Output video containing only the skeleton.
- `requirements.txt` – Required Python libraries.
- `.gitignore` – Excludes unnecessary files.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Kavya18-r/Human-Pose-Estimation.git
   ```

2. Open the project folder:
   ```bash
   cd Human-Pose-Estimation
   ```

3. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment on Windows:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

5. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

Run the following command:

```bash
python pose_detection.py
```

The program processes the input video and generates:

- `original_with_pose.mp4`
- `skeleton_only.mp4`

## Working
1. Read the input video frame by frame.
2. Convert each frame from BGR to RGB.
3. Detect human body landmarks using MediaPipe Pose.
4. Draw the skeleton connections on the original frame.
5. Draw the same skeleton on a black background.
6. Save both processed videos.

## Applications
- Human movement analysis
- Fitness and exercise monitoring
- Sports activity analysis
- Gesture recognition
- Human-computer interaction

## Author
**Kavya18-r**

