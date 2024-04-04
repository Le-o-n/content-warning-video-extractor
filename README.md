# Content Warning Video Extractor
<img src="https://github.com/Le-o-n/content-warning-video-extractor/assets/41658797/e796361a-7090-4bf6-8e34-5b7c73176c99" width="1000">

The Content Warning Video Extractor tool is designed to retrieve and convert all video recordings from the game [Content Warning](https://store.steampowered.com/app/2881650/Content_Warning/), including those that might have been lost. It efficiently converts videos from the `.webm` file format to the more widely used `.mp4` format, ensuring compatibility and ease of access.

## Download the Executable

You can download the latest version of the executable from the [Releases](https://github.com/Le-o-n/content-warning-video-extractor/releases/) section of this repository.

## Usage Instructions

### Running via the Executable

1. Download and run the executable file found in the [Releases](https://github.com/Le-o-n/content-warning-video-extractor/releases/) section of this repository.
2. The tool automatically searches for the directory containing the videos.
3. Extracted videos will be saved in an "output" folder, located in the same directory as the executable.

### Running via Python

To run the program using Python, follow these steps:

1. Ensure Python 3 is installed:
   - Visit the [Python Downloads Page](https://www.python.org/downloads/).
   - Download and run the installer.
   - **Important:** Check the option to "Add Python to PATH" during installation.
2. Run the `install_requirements.bat` file to install all necessary dependencies.
3. Execute `main.py` to start the video extraction process.

## Build Instructions

To build the executable yourself:

1. Install Python 3 and add it to your PATH as described above.
2. Execute `install_requirements.bat` to set up the required libraries.
3. Run `build.bat` to initiate the build process.
4. The newly built executable will be available in the `build` folder that get's created.

## FAQ

### Why is the executable file so large?

The executable includes the entire Python runtime to ensure it operates as a standalone application. This bundling is necessary for the executable to run independently of the user's Python environment.

### Executable flagged as malware?

Some antivirus programs might mistakenly flag the executable as malware. If this occurs, you have the option to run the tool directly using Python, as described in the "Running via Python" section.

## Support My Work
If you appreciate this tool, consider buying me a coffee. Here is my [Paypal](https://paypal.me/LeonB923). Thank you!

