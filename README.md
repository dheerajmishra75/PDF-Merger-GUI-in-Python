# PDF Merger GUI in Python

A simple desktop PDF merger application built with Python that allows users to select multiple PDF files and combine them into a single PDF document.

The project uses Tkinter for the graphical interface and `pypdf` for PDF processing and merging.

## 🎥 Preview

[▶️ Watch Project Demo](./Preview/PDF%20Merger%20GUI%20in%20Python.mp4)

The preview demonstrates selecting multiple PDF files, displaying the selected files in the application, choosing an output location, and merging the PDFs into a single document.

## ✨ Features

- Simple graphical user interface
- Select multiple PDF files
- Display selected PDF paths
- Add PDFs to the merge list
- Remove selected PDFs
- Clear the complete selection
- Merge selected PDF files
- Choose the output location
- Save the merged PDF
- Uses `pypdf` for PDF processing
- Provides GUI-based file selection

## 🎯 Project Overview

The PDF Merger GUI is a Python desktop utility designed to combine multiple PDF files into a single PDF document.

The application provides a simple graphical interface where users can select PDF files, manage the selected files, and merge them into one output document.

The project demonstrates the combination of Python GUI programming with practical PDF file processing.

## 🔄 How It Works

    1. The application starts using Tkinter.
    2. The user clicks the Add PDFs button.
    3. A file-selection dialog opens.
    4. Multiple PDF files can be selected.
    5. The selected PDF paths are added to the application.
    6. Unwanted files can be removed from the list.
    7. The list can also be cleared completely.
    8. The user clicks Merge.
    9. A save dialog is used to select the output location.
    10. `PdfWriter` combines the selected PDF pages.
    11. The merged PDF is saved to the selected location.

## 🖥️ Application Interface

The application provides controls for managing the PDF selection:

    Add PDFs
    Remove
    Clear
    Merge

The selected PDF files are displayed inside the application before the merge operation.

## 📄 PDF Processing

The project uses `PdfWriter` from the `pypdf` package to create the merged PDF.

The basic workflow is:

    Select PDF Files
          ↓
    Store Selected Paths
          ↓
    Read PDF Pages
          ↓
    Add Pages to PdfWriter
          ↓
    Save Merged PDF

## 🗂️ File Selection

Tkinter's file dialog is used to select PDF files.

The application filters the file-selection dialog for PDF documents so that users can select the files that need to be merged.

## 💾 Output

After selecting the PDFs, the application provides a save dialog where the user can specify the output location and filename.

The merged document is then written to the selected location.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Tkinter | Graphical user interface |
| `filedialog` | Selecting PDF files and output location |
| `messagebox` | Displaying application messages |
| `pypdf` | Reading and merging PDF documents |
| `PdfWriter` | Creating the merged PDF |

## 📁 Project Structure

    PDF-Merger-GUI-in-Python/
    │
    ├── Preview_video/
    │   └── PDF Merger GUI in Python.mp4
    │
    ├── main.py
    └── README.md

## ▶️ Run Locally

### 1. Clone the Repository

    git clone https://github.com/dheerajmishra75/PDF-Merger-GUI-in-Python.git

### 2. Navigate to the Project

    cd PDF-Merger-GUI-in-Python

### 3. Install the Required Package

    pip install pypdf

### 4. Run the Application

    python main.py

The PDF Merger window will open and you can start selecting PDF files.

## 🧪 Example Workflow

    Start Application
          ↓
    Click "Add PDFs"
          ↓
    Select Multiple PDFs
          ↓
    Selected PDFs Appear in List
          ↓
    Remove / Clear if Required
          ↓
    Click "Merge"
          ↓
    Select Output Location
          ↓
    Save Merged PDF

## 📚 Python Concepts Practiced

- Functions
- Lists
- File handling
- GUI programming
- Tkinter widgets
- File dialogs
- Message boxes
- External Python packages
- Working with file paths
- PDF document processing

## 🎯 Learning Outcomes

Through this project, I practiced how to:

- Build a simple desktop GUI using Tkinter
- Work with file-selection dialogs
- Handle multiple file paths
- Manage lists of selected files
- Use an external PDF-processing library
- Combine multiple PDF documents
- Save generated files to a selected location
- Connect GUI actions with Python functions

## 🚀 Future Improvements

Possible improvements for future versions include:

- Drag-and-drop PDF support
- PDF page reordering
- Preview selected PDFs
- Page-selection support
- Merge progress indicator
- Better error handling
- Duplicate-file detection
- Dark-mode interface
- Custom output filename before merging

## 🔗 Project Links

- GitHub: https://github.com/dheerajmishra75/PDF-Merger-GUI-in-Python

## 👨‍💻 Author

**Dheeraj Mishra**

B.Tech CSE Student | Python | Data Science | Machine Learning | Backend Development

## 📌 Disclaimer

This project was created for learning and practice purposes. It is a simple PDF utility and should be tested with important documents carefully before using it for critical document workflows.
