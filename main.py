import os
from os import path
from moviepy.editor import VideoFileClip

APP_DATA_PATH: str = os.getenv('APPDATA')
APP_DATA_LOCAL: str = path.join(APP_DATA_PATH, "..", "Local")
REC_DIR: str = path.join(APP_DATA_LOCAL, "Temp", "rec")
OUTPUT_FOLDER: str = path.abspath("./output")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

if not path.exists(REC_DIR):
    print(f"The directory {REC_DIR} does not exist.")
else:
    rec_dirs = os.listdir(REC_DIR)

    for i, folder_name in enumerate(rec_dirs):

        folder_dir: str = path.join(
            REC_DIR,
            folder_name
        )
        recording_file_path: str = path.join(
            folder_dir,
            "fullRecording.webm"
        )

        out_recording_file_name: str = f"{folder_name}.mp4"
        out_recording_file_path: str = path.join(
            OUTPUT_FOLDER,
            out_recording_file_name
        )

        if path.exists(recording_file_path):
            clip = VideoFileClip(recording_file_path)
            clip.write_videofile(out_recording_file_path)
            clip.close()
        else:
            print(f"The file {recording_file_path} does not exist.")
