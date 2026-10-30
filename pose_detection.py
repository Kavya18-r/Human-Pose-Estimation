
import cv2
import mediapipe as mp
import numpy as np
import os

# 1. Input and output video paths
INPUT_VIDEO = "input_video.mp4"
OUTPUT_ORIGINAL = "original_with_pose.mp4"
OUTPUT_SKELETON = "skeleton_only.mp4"

# 2. Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    smooth_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# 3. Open input video
cap = cv2.VideoCapture(INPUT_VIDEO)

if not cap.isOpened():
    print("Error: Could not open input video.")
    exit()

# 4. Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 30

# 5. Create output video writers
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

original_writer = cv2.VideoWriter(
    OUTPUT_ORIGINAL, fourcc, fps, (width, height)
)

skeleton_writer = cv2.VideoWriter(
    OUTPUT_SKELETON, fourcc, fps, (width, height)
)

# 6. Process video frame by frame
while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    # Convert BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect body landmarks
    results = pose.process(rgb_frame)

    # Create black background
    black_background = np.zeros((height, width, 3), dtype=np.uint8)

    if results.pose_landmarks:

        # Draw skeleton on original video
        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

        # Draw skeleton on black background
        mp_drawing.draw_landmarks(
            black_background,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

    # Save both output frames
    original_writer.write(frame)
    skeleton_writer.write(black_background)

# 7. Release resources
cap.release()
original_writer.release()
skeleton_writer.release()
pose.close()

print("Pose detection completed successfully!")
print("Saved:", OUTPUT_ORIGINAL)
print("Saved:", OUTPUT_SKELETON)
