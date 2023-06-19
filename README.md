# TkPad
TkPad is a simple text editor application developed using the Tkinter library in Python 3. It provides users with a user-friendly interface to create, edit, and save text documents. TkPad serves as a practice project for integrating various features of Tkinter and implementing key functionalities of a text editor.

![Image shows TkPad text editor application.](images/preview.png)

## Key Features
* **Graphical User Interface**: TkPad offers a visual interface where users can interact with buttons, menus, and a text area.
* **Text Editing Capabilities**: Users can create, edit, and modify text documents within TkPad. It supports basic text editing functionalities. The supported files types are .txt, .rtf and .py.
* **File Operations**: TkPad allows users to open and save text files. It provides options to create new files, open existing files, and save the edited documents.
* **Keyboard Shortcuts**: TkPad incorporates keyboard shortcuts to enhance productivity and user experience. Users can utilise regular operating system shortcut commands to save and open files, and to quit the application. Users can also use the zoom feature with shortcuts, which increases the font size. **These shortcuts are designed to work across different operating systems.**

## Usage
To use TkPad, you have two options for downloading and running the application.
1. Run with Python Interpreter:
    * Make sure you have Python 3 installed on your system.
    * Clone or download the TkPad repository from GitHub.
    * Open a terminal or command prompt and navigate to the downloaded TkPad directory.
    * Run the following command to start the application: `python main.py`.
    * The TkPad graphical user interface will be displayed, allowing you to start using the application.
2. Download the Release:
    * Visit this repository's release page here on GitHub.
    * Choose the desired release version and download the corresponding executable file for your operating system.
        * Windows: After downloading, double-click the executable file to launch the TkPad application. 
        * Mac: Right click on TkPad and click "Open" from the menu. 
    * The TkPad graphical user interface will be displayed, allowing you to start using the application.

## Dependencies
TkPad relies on Python 3, striprtf, and the Tkinter library, which is a standard GUI toolkit for Python. Ensure that both Tkinter and striprtf are installed before running the application, if using an interpreter. Striprtf can be installed through pip using `pip install striprtf`.