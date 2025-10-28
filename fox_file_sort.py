#fox_file_sort

#Script to sort files in folders into subfolders

import os, puremagic, shutil, argparse
from puremagic import PureError

def create_sub_folders(folder_path):
    if folder_path[0] == '~': #catches user using ~ shorthand for supplying directory names
      folder_path = os.path.expanduser(folder_path)

    if not os.path.exists(folder_path):  #simple error handling for invalid path names
            print(f'Path/Directory doesn\'t exist: {folder_path} \nCheck spelling/path is correct')
            return
    
    sub_folders = ['Images', 'Videos', 'Text_Files', 'Audio', 'Spreadsheets', 'Presentations', 'Archives', 'Code'] #names of folders to use
    
    
    for name in sub_folders:
        name_path = os.path.join(folder_path, name) #Full directory name to be created using names in sub_folders var
        try:
            os.mkdir(name_path)
        except FileExistsError:
            print(f'Folder already exists: {name_path}')

def file_detection(file): #file must be a valid filepath. ex: ~/Documents/some_file.mp3

    try:
        file_info = puremagic.magic_file(file) #Create pure magic object using a passed file path
        if file_info:
            result = max(file_info, key= lambda x: x.confidence) #finds and assigns the tuple with the greatest confidence value
            print(f"Detected by pure magic: {result.extension}")
            return result.extension #returns the name of file type
        else: #if file_info is empty list
            fallBk_ext = os.path.splitext(file)[1].lower()
            print(f'Pure magic failed to identify: falling back to named extension in file name: {fallBk_ext}')
            return fallBk_ext

    except (FileNotFoundError, PureError) as e:
        print(f'Skipped {file} : {e}')
        return None

def bulk_sort(folder_path): #sorts all files into folder into catagorised subFolders
   
    if folder_path[0] == '~': #catches user using ~ shorthand for supplying directory names
      folder_path = os.path.expanduser(folder_path)

    if not os.path.exists(folder_path):  #simple error handling for invalid path names
            print(f'Path/Directory doesn\'t exist: {folder_path} \nCheck spelling/path is correct')
            return

    
    file_types_dict = {
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".tiff": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".heic": "Images",

    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".webm": "Videos",

    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",
    ".flac": "Audio",
    ".ogg": "Audio",
    ".m4a": "Audio",
    ".wma": "Audio",

    # Text / Documents
    ".txt": "Text_Files",
    ".md": "Text_Files",
    ".rtf": "Text_Files",
    ".log": "Text_Files",
    ".pdf": "Text_Files",
    ".doc": "Text_Files",
    ".docx": "Text_Files",
    ".odt": "Text_Files",
    ".tex": "Text_Files",

    # Spreadsheets
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".ods": "Spreadsheets",

    # Presentations
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".odp": "Presentations",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".bz2": "Archives",
    ".xz": "Archives",
    ".iso": "Archives",

    # Code
    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".cpp": "Code",
    ".c": "Code",
    ".java": "Code",
    ".cs": "Code",
    ".php": "Code",
    ".rb": "Code",
    ".go": "Code",
    ".sh": "Code",
    ".bat": "Code",
    ".json": "Code",
    ".xml": "Code",
    ".yml": "Code",
    ".toml": "Code",
    ".ini": "Code",
}


    file_names = os.listdir(folder_path)
    
    for file in file_names:
       full_path = os.path.join(folder_path, file)
       if not os.path.isfile(full_path) or file.startswith('.'):
           continue #skip folders/directories and hidden files
       file_type = file_detection(full_path)
       try:
        shutil.move(full_path, os.path.join(folder_path, file_types_dict[file_type]))

       except KeyError:
           print(f'While sorting file: {file} file type \"{file_type}\" not supported by FoxFileSorter')
           continue

def cli():

    parser = argparse.ArgumentParser(description="Sorts files inside of a specified folder into newly created subfolders by their file types.")

    parser.add_argument(
        "--folder",
        type=str,
        required=True,
        help="Path to the folder of which the user wishes to sort"
    )

    return parser.parse_args()

def main():
    
    args = cli()
    folder = args.folder

    create_sub_folders(folder)
    bulk_sort(folder)
    print("Sort complete.")


    return

if __name__ == "__main__":
    main()
