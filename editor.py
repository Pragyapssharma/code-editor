import tkinter as tk
from tkinter import scrolledtext
import subprocess

class CodeEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Editor")
        self.text_area = scrolledtext.ScrolledText(self.root, width=100, height=20)
        self.text_area.pack()
        self.terminal = scrolledtext.ScrolledText(self.root, width=100, height=10)
        self.terminal.pack()
        self.run_button = tk.Button(self.root, text="Run", command=self.run_code)
        self.run_button.pack()

    def run_code(self):
        code = self.text_area.get("1.0", tk.END)
        process = subprocess.Popen(["python", "-c", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        self.terminal.delete("1.0", tk.END)
        if output:
            self.terminal.insert(tk.END, output.decode("utf-8"))
        if error:
            self.terminal.insert(tk.END, error.decode("utf-8"))

if __name__ == "__main__":
    root = tk.Tk()
    code_editor = CodeEditor(root)
    root.mainloop()