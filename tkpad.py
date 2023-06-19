import os
import sys
import tkinter.messagebox as tkmsg
from striprtf.striprtf import rtf_to_text
from tkinter import BOTH, END, Canvas, Frame, Menu, Scrollbar, Text, filedialog


class TkPad:
    """Main application class for TkPad."""
    
    def __init__(self, master):
        """Initialize the Main class.

        Args:
            master (Tk): The root Tk instance.
        """
        
        self.master = master   
        self.frame = Frame(self.master)
        self.canvas = Canvas(self.master, height=20)
        self.canvas.pack(fill="x")
        self.frame.pack(fill=BOTH, expand=True)
        
        self.add_menus_to_top_menu_bar()
        self.draw_ruler_on_canvas()
        self.create_text_widget()
        self.create_keyboard_shortcuts()

    def add_menus_to_top_menu_bar(self):
        """Add file menus to the top menu bar."""
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        
        self.fileMenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.fileMenu)
        
        if sys.platform.startswith('darwin'):
            open = "Open [Command + O]"
            save = "Save [Command + S]"
            quit = "Quit [Command + Q]"
        else:
            open = "Open [Control + O]"
            save = "Save [Control + S]"
            quit = "Quit [Alt + F4]"
            
        self.fileMenu.add_command(label=open, command=self.on_open_button)
        self.fileMenu.add_command(label=save, command=self.on_save_button)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label=quit, command=self.quit_prompt)
        
        self.zoomMenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Zoom", menu=self.zoomMenu)
        
        if sys.platform.startswith('darwin'):
            zoom_in = "Zoom in [Command + plus]"
            zoom_out = "Zoom out [Command + minus]"
        else:
            zoom_in = "Zoom in [Control + plus]"
            zoom_out = "Zoom out [Control + minus]"

        self.zoomMenu.add_command(label=zoom_in, command=self.zoom_in)
        self.zoomMenu.add_command(label=zoom_out, command=self.zoom_out)
        self.zoomMenu.add_separator()
        self.zoomMenu.add_command(label="Restore zoom", command=self.restore_zoom)
    
    def draw_ruler_on_canvas(self):
        """Draw a ruler on the canvas."""
        steps = 3
        for i in range(0, self.master.winfo_screenwidth(), steps*10):
            self.canvas.create_line(i, 10, i, 20, fill="grey") 

    def create_text_widget(self):
        """Create the text widget."""
        text_frame = Frame(self.frame)
    
        scrollbar = Scrollbar(text_frame)
        scrollbar.pack(side="right", fill="y")
    
        self.text = Text(text_frame, wrap="word", font=("Helvetica", 14), highlightthickness=0)
        self.text.pack(side="left", fill=BOTH, expand=True)
    
        scrollbar.config(command=self.text.yview)
        self.text.config(yscrollcommand=scrollbar.set)
    
        text_frame.pack(fill=BOTH, expand=True)

    def create_keyboard_shortcuts(self):
        """Create keyboard shortcuts."""
        if sys.platform.startswith('darwin'):
            save = "<Command-s>"
            open = "<Command-o>"
            close = "::tk::mac::Quit"
            self.master.createcommand(close, self.quit_prompt)
            self.master.bind("<Command-plus>", self.zoom_in)
            self.master.bind("<Command-minus>", self.zoom_out)
        else:
            save = "<Control-s>"
            open = "<Control-o>"
            self.master.bind("<Control-plus>", self.zoom_in)
            self.master.bind("<Control-minus>", self.zoom_out)
        
        self.master.protocol("WM_DELETE_WINDOW", self.quit_prompt)
        self.master.bind(save, self.on_save_button)
        self.master.bind(open, self.on_open_button)
    
    def on_text_focus_in(self, event):
        """Handle the event when the text widget gains focus."""
        self.text.config(highlightthickness=0)

    def on_text_focus_out(self, event):
        """Handle the event when the text widget loses focus."""
        self.text.config(highlightthickness=0)
        
    def on_save_button(self, event=None):
        """Handle the event when the save button/menu is clicked or its associated shortcut is pressed."""
        text = self.text.get("1.0", END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")

        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(text)
                tkmsg.showinfo('Info', 'File saved successfully at ' + file_path)
            except IOError:
                tkmsg.showwarning('Warning!', 'Error occurred while saving the file. Please retry.')
    
    def on_open_button(self, event=None):
        """Handle the event when the open button/menu is clicked or its associated shortcut is pressed."""
        file_path = filedialog.askopenfilename(filetypes=[
            ("Text Files", "*.txt"), ("Rich Text Files", "*.rtf"), ("Python Files", "*.py")])
        if file_path:
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension == ".txt" or file_extension == ".py":
                with open(file_path, "r") as file:
                    file_content = file.read()
                    self.text.delete("1.0", END)
                    self.text.insert("1.0", file_content)
            elif file_extension == ".rtf":
                with open(file_path, "rb") as file:
                    rtf_content = file.read().decode("utf-8")
                    file_content = rtf_to_text(rtf_content)
                    self.text.delete("1.0", END)
                    self.text.insert("1.0", file_content)
            else:
                tkmsg.showerror("Error", "Unsupported file format. Please use .rtf, .py, or .txt files.", icon="warning")

                
    def quit_prompt(self, event=None):
        """Handle the event when the window close button or its associated shortcut is pressed."""
        answer = tkmsg.askokcancel(
            'WARNING', 'All unsaved content will be discarded! Are you sure you wish to exit?', 
            icon = 'warning', default='cancel')
        
        if (answer == True):
            self.master.destroy()
        else:
            pass
    
    def zoom_in(self, event=None):
        """Increase the font size of the text widget by 2 points."""
        font_info = self.text.cget("font")
        font_size = font_info.split(" ")[-1]
        self.text.config(font=("Helvetica", int(font_size) + 2))

    def zoom_out(self, event=None):
        """Decrease the font size of the text widget by 2 points, if the font size is greater than 7."""
        font_info = self.text.cget("font")
        font_size = font_info.split(" ")[-1]
        if int(font_size) <= 7:
            pass
        else:
            self.text.config(font=("Helvetica", int(font_size) - 2))

    def restore_zoom(self):
        """Restore the font size of the text widget to the default value (14 points)."""
        self.text.config(font=("Helvetica", 14))