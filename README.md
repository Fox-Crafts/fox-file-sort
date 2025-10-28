# Fox Craft 🦊
Fox Craft is a Python utility that automatically sorts files inside a folder into categorized subfolders (Images, Videos, Audio, Documents, Archives, Code, etc.). It uses [puremagic](https://pypi.org/project/puremagic/) for reliable file-type detection beyond just extensions.

## Features
- Automatically creates subfolders (Images, Videos, Audio, etc.)
- Detects file types using content-based magic numbers
- Falls back gracefully to filename extensions when needed
- Simple command-line interface (CLI)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/FoxCraft.git
   cd FoxCraft

    Install dependencies:

    pip install puremagic

Usage

Run the script with the --folder argument pointing to your target directory:

python fox_file_sorter.py --folder ~/Downloads

Example:

python fox_file_sorter.py --folder C:\Users\Luke\Desktop

The tool will:

    Create subfolders (Images, Videos, etc.)

    Move matching files into their respective folders

Supported File Types

    Images → jpg, png, gif, bmp, tiff, webp, svg, heic

    Videos → mp4, mkv, mov, avi, wmv, flv, webm

    Audio → mp3, wav, aac, flac, ogg, m4a, wma

    Documents → txt, md, rtf, log, pdf, doc, docx, odt, tex

    Spreadsheets → xls, xlsx, csv, ods

    Presentations → ppt, pptx, odp

    Archives → zip, rar, 7z, tar, gz, bz2, xz, iso

    Code → py, js, html, css, cpp, c, java, cs, php, rb, go, sh, bat, json, xml, yml, toml, ini

Roadmap

Planned future improvements:

    --dry-run option (preview changes without moving files)

    Logging support

    
Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to add.
License

Fox Craft License
Copyright (c) 2025 Luke (aka Fox)

Permission is hereby granted to any person obtaining a copy of this software 
and associated documentation files (the "Software") to use the Software for 
personal or internal purposes only.

The following are NOT permitted without prior written permission from the author:
- Redistribution of the Software, in whole or in part
- Commercial use of the Software, including selling or sublicensing
- Modification of the Software for distribution

The Software is provided "as is", without warranty of any kind, express or implied, 
including but not limited to the warranties of merchantability, fitness for a particular 
purpose and noninfringement. In no event shall the author be liable for any claim, damages 
or other liability, whether in an action of contract, tort or otherwise, arising from, 
out of or in connection with the Software or the use or other dealings in the Software.
