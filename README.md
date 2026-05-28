# PDF Merger

A clean desktop app to merge PDF files, built with pywebview + pypdf.

Latest release:(https://github.com/lukeMiP/z-merge/releases/latest)

## Setup

```bash
pip install -r requirements.txt
```

On macOS you may also need:
```bash
pip install pyobjc-framework-WebKit
```

On Linux:
```bash
sudo apt install python3-gi gir1.2-webkit2-4.0
pip install pywebview[gtk]
```

## Run

```bash
python app.py
```

## Usage

1. Click the upload area (or drag PDFs onto it) to add files
2. Drag the rows to reorder them — the merge order matches the list order
3. Type your desired output filename in the bottom field (`.pdf` is added automatically)
4. Click **Merge PDFs**
5. Select the destination file location
