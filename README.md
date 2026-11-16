# JPEG Image Forgery Detection Using Error Level Analysis (ELA)

## Overview

This project demonstrates how digital forensic techniques can be used to examine JPEG images for possible manipulation.

It uses Error Level Analysis (ELA) to highlight differences in JPEG compression, SHA-256 hashing to compare file integrity, and ExifTool to examine image metadata.

The practical experiment compares an original photograph with an edited version containing manually added pencil marks.

## Objectives

- Understand the working of Error Level Analysis.
- Examine possible image manipulation using ELA.
- Compare original and edited images.
- Calculate SHA-256 hashes.
- Extract and compare image metadata.
- Understand the limitations of image forensic techniques.

## Tools and Technologies

- Python 3
- OpenCV
- C++
- ExifTool 13.64
- PowerShell
- SHA-256

## How It Works

1. Load the original and edited JPEG images.
2. Recompress each image using JPEG quality 95.
3. Calculate the absolute pixel difference between the original and recompressed images.
4. Multiply the differences by 30 to make them more visible.
5. Save the ELA results.
6. Compare the generated results.
7. Examine metadata and calculate SHA-256 hashes.

## Project Structure

- `ela.py` – Python implementation of ELA.
- `ela.cpp` – C++ implementation of ELA.
- `compare.py` – Creates a side-by-side comparison.
- `images/` – Original and edited photographs.
- `results/` – Generated ELA images and comparison.
- `evidence/` – Metadata and hash evidence.

## Installation

Install Python dependencies:

```bash
pip install opencv-python numpy
```

Install ExifTool separately from its official website.

## Usage

Run the ELA analysis:

```bash
python ela.py
```

Generate the comparison:

```bash
python compare.py
```

Calculate SHA-256 hashes in PowerShell:

```powershell
Get-FileHash .\images\original.jpg -Algorithm SHA256
Get-FileHash .\images\photoshopped_img.jpg -Algorithm SHA256
```

Extract metadata using ExifTool:

```powershell
.\exiftool.exe .\images\original.jpg
.\exiftool.exe .\images\photoshopped_img.jpg
```

## Results

The experiment produced separate ELA results for the original and edited photographs.

The edited photograph showed brighter outlines around the manually added pencil marks. The original and edited files also had different SHA-256 hashes and differences in their metadata.

## Limitations

- ELA does not independently prove that an image has been manipulated.
- Natural image features and different compression histories can also produce visible differences.
- Different SHA-256 hashes only indicate that two files are not byte-for-byte identical.
- Metadata may be missing, modified, or removed.
- Results should be interpreted with other forensic evidence.

## References

- [Original ELA implementation by prsntmaurya](https://github.com/prsntmaurya/Error-Level-Analysis)
- [ExifTool](https://exiftool.org/)
- [OpenCV Documentation](https://docs.opencv.org/)

## Disclaimer

This project is developed for educational and digital forensics learning purposes. ELA results are indicators for further investigation, not definitive proof of image forgery.
