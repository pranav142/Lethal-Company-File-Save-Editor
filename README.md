# Lethal Company Save Editor

## Overview

The Lethal Company Save Editor is a GUI-based application designed to provide gamers with the ability to easily modify their game save files. This tool is specifically tailored for editing save files of Lethal Company games, enabling players to customize various aspects of their gaming experience. Users can add credits, unlock items, modify enemy scans, and adjust item values directly through a user-friendly interface.

## Getting Started

### Prerequisites

Before you start using the Lethal Company Save Editor, ensure you have the following installed:

- Python 3.8 or higher

### Installation

1. Clone or download the repository to your local machine.
2. Navigate to the application directory.
3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

To use the Lethal Company Save Editor, follow these steps:

1. **Find your Save File**:

   - Click Windows Button + r
   - Paste in the following

   ```txt
   %localappdata%Low\ZeekerssRBLX\Lethal Company
   ```

   Your save files should be shown as LCSaveFile1 to LCSaveFile3 make sure you see where this path is so you can easily access it

2. **Start the Application**:

   - Launch your terminal or command prompt.
   - Navigate to the `src` directory where the application files are located.
   - Run the application by executing:

   ```bash
   python app.py
   ```

   This command will open the graphical interface of the Save Editor.

3. **Open a Save File**:

   - In the Save Editor's main window, click on the `Open File` button. This will open a file dialog.
   - Use the file dialog to locate and select your Lethal Company game save files that we found in step 1.
   - After selecting the file, click 'Open'. The application will decrypt and load the file, displaying its contents in the text area for editing.

4. **Edit the Save File**:

   - With the save file loaded, you can now modify various aspects of your game data. This includes adding credits, unlocking items, modifying enemy scans, and adjusting item values.
   - Make your edits directly in the provided text area. The changes you make here will be reflected in your game once the file is saved and reloaded in the game.
   - An example edit would be changing the GroupCredits value to whatever value you want. This will change how many credits you have on your ship

5. **Save Your Changes**:

   - After editing, click the `Save File` button to apply your changes to the save file.
   - A confirmation dialog will appear, asking you to confirm the save operation. Click 'OK' to proceed.
   - The application will then encrypt and save your changes back to the original save file.

6. **Confirmation and Completion**:
   - Upon successful saving, a message will appear confirming that the file was saved successfully.
   - You can now close the Save Editor and enjoy your modified gaming experience in Lethal Company.

**Note:** It is highly recommended to back up your original save files before using the editor to avoid any potential loss of data.
