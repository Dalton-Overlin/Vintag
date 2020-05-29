Got a messy music library? Don't want to sort it by hand? Then Vintag is your solution! Vintag will allow you to sort a music library effortlessly!

![This-To-This](https://user-images.githubusercontent.com/30564402/83207665-fe868980-a110-11ea-8e87-c3a6021db032.jpg)

## **About Vintag**

![Vintag Wallpaper](https://user-images.githubusercontent.com/30564402/83207699-13fbb380-a111-11ea-96e5-1049d110e107.jpg)

Vintag allows you to quickly and efficiently sort mp3 files and place them into corresponding folders. This program can only sort mp3 files as of right now. You can run this program using the Python script or you can use the Windows executable which I will discuss below in this information. 

## **How to Use**

Start Vintag and the window below will open. You can either type the path to the folder to sort manually or you can click the "Open Selector" button, or the decorative image that says "Vintag By Dalton Overlin" and a GUI will pop-up asking you to select a folder. The program will then begin scanning the directory you selected. 

![GUI-1](https://user-images.githubusercontent.com/30564402/83207725-28d84700-a111-11ea-9d4b-1981a3fb5795.PNG)

After a folder with mp3s has been selected and the program has scanned the folder this window below will pop-up so you can specify the attributes for the album. The dropdown boxes at the top of the window allow you to set the Genre, Album Name, Artist Name, and Album, year in that order. The edit buttons to the left of the window will allow you to manually type out or edit the data for each album. You can also click the change cover button to select a different album cover to use for the album. You can also specify the size of the album cover to embed it into the mp3. This is done by choosing a size from the dropdown menu placed toward the left side of the window. Noting that the original size of the original album cover and its original size will be stored as a JPG file named cover in the corresponding albums folder along with the mp3s. Only the album cover that is embedded into the mp3s will be resized. Another option you can set is the naming scheme. A dropdown box to the right side of the window will let you choose from example file numbering schemes. This will be how your file names will appear once the program renames/renumbers them. 

![GUI-2](https://user-images.githubusercontent.com/30564402/83207758-3b528080-a111-11ea-86e0-a7317724ce94.PNG)

You can also merge mp3s into a merged album. When sorting through files just click the Merge One or Merge Two button. Once you have sorted through all of the files you have specified to merge, a window will pop-up asking you what name you want the merged album to be named. Then once you specify that it will give you further options to edit the newly merged album. Keep in mind, there are "Merge One" and "Merge Two" buttons. This way you can store files between two albums to merge for each time you sort a folder. This just allows you to sort files more efficiently. You can also skip files, this way those files will not be moved or processed. 

## **Vintag for Windows OS**

I have compiled Vintag to run on Windows. There are two compiled versions of Vintag. The first version is a standalone executable file where all files are stored in a single file. The second version is a zipped folder containing the program files and the Vintag.exe file which can run on Windows also. The difference is that the single Vintag.exe file takes longer to start up on Windows, while the one in the zipped folder starts up much faster because all files aren't compressed into a single file. 

## **Version One**

This version takes longer to launch, but the benefits are that all files are stored in a single executable file. 

**[`Download the Vintag.exe `](https://github.com/Dalton-Overlin/Vintag/blob/master/Windows%20Executables/Vintag.exe "`Download the Vintag.exe `")**

## **Instructions**

Download Vintag.exe and run it on a Windows OS. I have verified this program to run on Windows 8.1, and Windows 10. Presumably, it will work on Windows 7, but I have not verified this. 

## **Version Two**

This version launches quicker, but all program files are extracted so it looks a little messy. You would probably want to create a shortcut to the Vintag.exe file to make it easier to launch.

**[`Download Vintag.zip `](https://github.com/Dalton-Overlin/Vintag/blob/master/Windows%20Executables/Vintag.zip "`Download Vintag.zip `")**

## **Instructions**

Download the zipped file, then extract the zipped file. Once you do you can run the program by running the Vintag.exe file. To make it easier you may want to create a shortcut and place it somewhere on your device that will make it easier for you to launch the program in the future. This way you don't have to sort through all the files to find the Vintag.exe file each time. I have verified this program to run on Windows 8.1, and Windows 10. Presumably, it will work on Windows 7, but I have not verified this.

## **Running from Python Script**

First, download the Python script.

**[`Download Vintag.pyw `](https://github.com/Dalton-Overlin/Vintag/blob/master/Vintag.pyw "`Download Vintag.pyw `")**

This program is built using Python 3, so if you want to run the raw code of this program you will need a way of running Python 3 scripts. This program depends on these modules below.

Required Python Modules

os
sys
threading
random
string
Tkinter
time
DateTime
eyed3
tinytag
PIL (also known as pillow)

Most of those modules come pre-installed with Python, but on some systems like Linux, some packages may be missing which you will have to install. Then once those modules are installed on your system you can run the raw Python script. 

Enjoy!
