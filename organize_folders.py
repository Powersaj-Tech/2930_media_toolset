import os
import tkinter as tk
from tkinter import filedialog


def create_subfolders(folder_path):
    """
    Creates subfolders named "videos," "pictures," and "other" within the specified folder path.

    Args:
        folder_path (str): The path to the folder to be organized.

    Returns:
        None
    """
    # Create subfolders
    video_folder = os.path.join(folder_path, "videos")
    picture_folder = os.path.join(folder_path, "pictures")
    other_folder = os.path.join(folder_path, "other")
    os.makedirs(video_folder, exist_ok=True)
    os.makedirs(picture_folder, exist_ok=True)
    os.makedirs(other_folder, exist_ok=True)

    # Organize files based on their extensions
    for root, _, files in os.walk(folder_path):
        for filename in files:
            _, ext = os.path.splitext(filename)
            ext = ext.lower()  # Normalize extension to lowercase
            if ext in (".mp4", ".mov", ".avi", ".thm"):
                os.rename(os.path.join(root, filename), os.path.join(video_folder, filename))
            elif ext in (".jpg", ".png", ".gif", ".cr2"):
                os.rename(os.path.join(root, filename), os.path.join(picture_folder, filename))
            else:
                os.rename(os.path.join(root, filename), os.path.join(other_folder, filename))


def main():
    """
    Main function to prompt the user to select a folder and organize its contents.

    Returns:
        None
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    # Prompt user to select a folder
    folder_path = filedialog.askdirectory(title="Select a folder to organize")
    if folder_path:
        create_subfolders(folder_path)
        print(f"Organized files in '{folder_path}' into 'videos,' 'pictures,' and 'other' subfolders.")
    else:
        print("No folder selected. Exiting.")


if __name__ == "__main__":
    main()
