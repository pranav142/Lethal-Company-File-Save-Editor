import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, font
from encryption import encrypt_aes, decrypt_aes
import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s:%(message)s",
)


class App:
    def __init__(self, root):
        self.root = root
        root.title("Lethal Company Save File Encryptor/Decryptor")
        root.geometry("600x400")
        root.resizable(True, True)

        custom_font = font.Font(family="Helvetica", size=12)

        button_style = {"font": custom_font, "bg": "#0052cc", "fg": "white"}

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame, text="Open File", command=self.open_file, **button_style
        ).pack(side=tk.LEFT, padx=10)
        tk.Button(
            button_frame, text="Save File", command=self.save_file, **button_style
        ).pack(side=tk.LEFT, padx=10)

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=custom_font)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.status_bar = tk.Label(
            root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.current_file = None
        self.password = "lcslime14a5"

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.current_file = file_path
            logging.info(f"Opening file: {file_path}")
            try:
                decrypted_content = decrypt_aes(file_path, self.password)
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, decrypted_content)
            except Exception as e:
                logging.error(f"Error decrypting file: {e}")
                messagebox.showerror("Error", f"An error occurred: {e}")

    def save_file(self):
        if self.current_file:
            try:
                edited_content = self.text_area.get("1.0", tk.END)
                encrypt_aes(
                    edited_content.encode("utf-8"), self.current_file, self.password
                )
                logging.info(f"File saved: {self.current_file}")
                messagebox.showinfo("Success", "File saved successfully.")
            except Exception as e:
                logging.error(f"Error saving file: {e}")
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            logging.warning("Save operation attempted with no file selected.")
            messagebox.showwarning("Warning", "No file selected.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
