# Content Warning Video Extractor
<img src="https://github.com/Le-o-n/content-warning-video-extractor/assets/41658797/e796361a-7090-4bf6-8e34-5b7c73176c99" width="1000">

The Content Warning Video Extractor tool is designed to retrieve and convert all video recordings from the game '[Content Warning](https://store.steampowered.com/app/2881650/Content_Warning/)', including those that might have been lost. It efficiently converts videos from the `.webm` file format to the more widely used `.mp4` format, ensuring compatibility and ease of access.

## Important
- This tool needs to be run each time you want to extract the videos, it will extract all videos of the current/previous server.
- As soon as you join a new server, all previous video clips will be deleted so you want to run this before joining a new server.


## Download the Executable

You can download the latest version of the executable from the [Releases](https://github.com/Le-o-n/content-warning-video-extractor/releases/) section of this repository.

## Running via the Executable

1. Download and run the executable file found in the [Releases](https://github.com/Le-o-n/content-warning-video-extractor/releases/) section of this repository.
2. The tool automatically searches for the directory containing the videos.
3. Extracted videos will be saved in an "output" folder, located in the same directory as the executable.

## Running via Python

To efficiently run the program with Python, ensure you follow the outlined steps carefully:

### **1. Install Python 3:**
   To make sure you have Python 3 installed on your system, adhere to these instructions:
   - Navigate to the [Python Downloads Page](https://www.python.org/downloads/) to find the appropriate installer for your operating system.
   - Download and execute the installer. During the installation process, it is **critical** to select the option to "Add Python to PATH". This step ensures that Python is accessible from the command line across the system.

### **2. Install Necessary Dependencies:**
   Before running the program, all required dependencies must be installed. This is achieved by running the `install_requirements.bat` file. Simply double-click on this file, and it will automatically install the necessary libraries and packages.

### **3. Run the Program:**
   After setting up Python and the dependencies, you're ready to execute the program. Here's how to proceed:
   - **Open Command Prompt:** Start by opening the Command Prompt on your system.
   - **Navigate to Script Directory:** Use the `cd` command to change your current directory to the one containing `main.py`. Replace the placeholder path with the actual path to your script directory:

     ```cmd
     cd C:/this/is/the/full/dir/path/to/the/folder/containing/the/project
     ```

   - **Execute the Program:** Finally, run the program by executing the following command:

     ```cmd
     python ./main.py
     ```

   **Important Note:** Before running the command above, ensure you're in the correct directory that contains the `main.py` script. This step is crucial for the successful execution of the program.

   

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

