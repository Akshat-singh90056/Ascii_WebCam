import cv2
import numpy as np
import os
import sys

ASCII_CHARS = "@%#*+=-:. "
WIDTH = 100  # adjust as needed for your terminal

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def frame_to_ascii(frame, width=WIDTH):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Resize according to aspect ratio for terminal
    height, orig_width = gray.shape
    aspect_ratio = height / orig_width
    new_height = int(aspect_ratio * width * 0.55)
    resized_gray = cv2.resize(gray, (width, new_height))
    # Map to ascii
    scale = len(ASCII_CHARS) - 1
    ascii_img = ""
    for row in resized_gray:
        ascii_img += "".join([ASCII_CHARS[int(px/255 * scale)] for px in row]) + "\n"
    return ascii_img

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Webcam not found")
        sys.exit(1)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            ascii_frame = frame_to_ascii(frame, WIDTH)
            clear_terminal()
            print(ascii_frame)
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
