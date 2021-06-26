# ImageSorter

Image Sorter is a graphical image sorting and cropping tool.

It is written in Python and uses Qt for it's graphical interface.

![Screen 1](https://github.com/atharva-bhagwat/image_sorter/blob/main/readme_assets/1.png?raw=true)

![Screen 2](https://github.com/atharva-bhagwat/image_sorter/blob/main/readme_assets/2.png?raw=true)

## Installation

### Ubuntu Linux

- [Download](https://github.com/atharva-bhagwat/image_sorter/blob/main/installation_assets/imagesorter_1.0_amd64.deb) .deb file
- `sudo dpkg -i imagesorter_1.0_amd64.deb`

You'll find *Image Sorter* in Applications

### Windows

1. Clone this repo
2. Install PyQt5 and Pillow
    1. `pip install PyQt5`
    2. `pip install pillow`
3. Run `python image_sorter.py`

### MacOS

1. Clone this repo
2. Install PyQt5 and Pillow
    1. `pip install PyQt5`
    2. `pip install pillow`
3. Run `python image_sorter.py`

## Usage

### Steps

**Screen 1:**
1. Install and launch using the [instruction above](https://github.com/atharva-bhagwat/image_sorter/blob/main/README.md#installation)
2. Click 'Open Folder' to select folder to be processed
3. Choose either 'Copy' or 'Cut' operation
4. Add subfolders in which you wish to sort the data
5. Click 'Proceed'

**Screen 2:**
1. Click on buttons with subfolder names to sort the image

### Hotkeys
| Key | Description |
|-----|-----|
| Ctrl+o | Open Folder on Screen 1 |
| Enter | Add subfolder to the list of subfolders |
| ← → | Arrow key to move between images |
| Number keys | To sort images in respective subfolder |

*Note: Number keys are assigned according to the order in which the buttons appear on Screen 2*

### Output
<process_folder_name>_sorted will be created in the folder directory with the 'process folder'.

## How to contribute
Send a pull request

## ImageSorter: Notes for packaging

### Resources:
[Creating executable](https://blog.aaronhktan.com/posts/2018/05/14/pyqt5-pyinstaller-executable)
[Creating working directory and generating .deb](https://www.internalpointers.com/post/build-binary-deb-package-practical-guide)

# Notes & Credits
- Target audience for this application are ML Engineers. I hope this makes creating datasets easier.
- Found a bug? Have an improvement? Contribute by sending a pull request.
- Icon made by [Freepik](https://www.freepik.com) from [flaticon](https://www.flaticon.com)
