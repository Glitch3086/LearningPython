# YouTube Downloader
## Status: ✅
---
## Disclamier !?
- First of all, I would like to thank the sponsor of this script, the beautiful ChatGPT, for creating this masterpiece.
- The script does indeed work but be aware that as of now, due to YouTube guidelines, some YouTube might not download or the scipt may not be able to retirive the title.
- If you use this code, make sure to define the path or else things might get a little funcky. It will create a path for you but like I said, it will get wierd.

## General Info:
This script downloads YouTube videos as its title suggests. Initially, I generated the script using ChatGPT. However, to improve it, I had ChatGPT generate multiple instances of the Python script. Unfortunately, the AI usually missed some important code, so I decided to use this as a learning experience and fix it myself rather than relying on the AI.

First, I had the AI generate the first script, then I added additional features one by one, generating a wide variety of scripts, each with a different function. Finally, I combined all the scripts into a single one using Visual Studio Code.

## The script does the following:

The code begins by importing two modules: "os" for handling file operations and "pytube" for downloading videos. The user is prompted to enter a YouTube URL, and a 'YouTube' object is created to retrieve the available streams. Next, the user is asked to choose between downloading a video or an audio file. If a video file is selected, the script retrieves the highest resolution stream, and if an audio file is selected, the script retrieves the audio-only stream. The script then checks if the download directory exists, creating it if necessary. I didn't want the script to ask the user a download path everytime, so I have it predefined in the code. The download location is predefined in the code to avoid asking the user for it each time. Finally, the script downloads the selected file type to the download directory and prints a message indicating success or failure.

## What I learned:

Through this experience, I have gained valuable knowledge in using the ChatGPT API to create multiple instances of a script and fusing them together to automate repetitive tasks. It saved me a lot of time and improved the efficiency of my programming work. Additionally, I gained experience in working with the pytube library for downloading YouTube videos and using Python's os module for handling file operations.

Moreover, I learned how to read other people's code and make my own changes, as well as debugging the code. These skills are crucial in becoming a successful programmer as it helps in collaborating with others and understanding the coding structure. Overall, this experience taught me that combining AI and human intelligence can be a powerful tool in programming and can significantly improve workflow efficiency.