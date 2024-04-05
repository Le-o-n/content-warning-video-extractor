import os
from os import path
from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips


print("||===================================================================================||")
print("||      ___            _             _     __    __                 _                ||")
print("||     / __\___  _ __ | |_ ___ _ __ | |_  / / /\ \ \__ _ _ __ _ __ (_)_ __   __ _    ||")
print("||    / /  / _ \| '_ \| __/ _ \ '_ \| __| \ \/  \/ / _` | '__| '_ \| | '_ \ / _` |   ||")
print("||   / /__| (_) | | | | ||  __/ | | | |_   \  /\  / (_| | |  | | | | | | | | (_| |   ||")
print("||   \____/\___/|_| |_|\__\___|_| |_|\__|   \/  \/ \__,_|_|  |_| |_|_|_| |_|\__, |   ||")
print("||                                                                          |___/    ||")
print("||                          Video Extraction Tool                                    ||")
print("||===================================================================================||")
print("||                                                                                   ||")
print("|| This tool collects all currently available videos from the last or current server ||")
print("|| you are on. Run each time you want to collect the videos.                         ||")
print("||                                                                                   ||")
print("||===================================================================================||")

# .../AppData/Roaming
APP_DATA_PATH: str = os.getenv('APPDATA')
# .../AppData/Local
APP_DATA_LOCAL: str = path.join(APP_DATA_PATH, "..", "Local")
# .../AppData/Local/Temp/rec
REC_DIR: str = path.join(APP_DATA_LOCAL, "Temp", "rec")
# ./output
OUTPUT_FOLDER: str = path.abspath("./output")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

if not path.exists(REC_DIR):
    print(f"The directory {REC_DIR} does not exist.")
else:
    rec_dirs = os.listdir(REC_DIR)
    num_videos: int = len(rec_dirs)

    print("\n\n\n\n\n")
    print("||===================================================================================||")
    print("||                                     Log                                           ||")
    print("||===================================================================================||")

    if num_videos == 0:
        print(" No videos found, make sure to run this before joining a new server.")
        input(" Press any key to close...")
        exit()

    for i, rec_full_recording_folder in enumerate(rec_dirs):

        # full path to recording dir
        full_recording_dir: str = path.join(
            REC_DIR,
            rec_full_recording_folder
        )

        # full path to the final generated recording file
        recording_file_path: str = path.join(
            full_recording_dir,
            "fullRecording.webm"
        )

        # output recording file name
        out_recording_file_name: str = f"{rec_full_recording_folder}.mp4"
        # output recording full file path
        out_recording_file_path: str = path.join(
            OUTPUT_FOLDER,
            out_recording_file_name
        )

        if path.exists(recording_file_path):
            # the full recording already exists

            # create VideoFileClip object for webm file
            clip: VideoFileClip = VideoFileClip(recording_file_path)
            # write as mp4 file in output folder
            clip.write_videofile(out_recording_file_path)
            # close handle to file
            clip.close()
        else:
            # the recording was never generated (the recording was lost)
            # collect all the sub-clips and sort based on their
            # last modified time
            sub_clip_paths = []
            for sub_folder in os.listdir(full_recording_dir):
                # for each of the sub clips

                # full path to the sub clip directory
                sub_clip_dir_full_path = path.join(
                    full_recording_dir,
                    sub_folder
                )
                if path.isdir(sub_clip_dir_full_path):
                    # if there exists this subclip dir

                    # full path to the subclip webm file
                    sub_clip_path = path.join(
                        sub_clip_dir_full_path,
                        "output.webm"
                    )
                    if path.exists(sub_clip_path):
                        # if the sub-clip webm file exists

                        # append this subclip path to the list of sub-clips along with it's modified time
                        sub_clip_paths.append(
                            (
                                sub_clip_path,
                                os.path.getmtime(sub_clip_path)
                            )
                        )

            # sort the sub-clips based on their last modified time
            sub_clip_paths.sort(key=lambda x: x[1])
            # extract only the subclip paths
            sorted_paths = [path for path, _ in sub_clip_paths]

            # convert the sub-clips into VideoFileClip objects
            clips: list[VideoFileClip] = [
                VideoFileClip(sub_clip)
                for sub_clip in sorted_paths
            ]

            # concatenate all the sub-clips into one clip
            final_clip: VideoFileClip = concatenate_videoclips(clips)
            # write this to the output director
            final_clip.write_videofile(out_recording_file_path)
            # close the handle to the file
            final_clip.close()

print(f" Finished extraction of the {num_videos} video(s).")
print(f" The videos are found in the directory {OUTPUT_FOLDER}")
input(" Press any key to close...")
