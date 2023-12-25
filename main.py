import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from encryption import encrypt_aes, decrypt_aes


class App:
    def __init__(self, root):
        self.root = root
        root.title("Lethal Company Save File Encryptor/Decryptor")

        tk.Button(root, text="Open File", command=self.open_file).pack()
        tk.Button(root, text="Save File", command=self.save_file).pack()

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.current_file = None
        self.password = "lcslime14a5"

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.current_file = file_path
            decrypted_content = decrypt_aes(file_path, self.password)
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, decrypted_content)

    def save_file(self):
        if self.current_file:
            edited_content = self.text_area.get("1.0", tk.END)
            encrypt_aes(
                edited_content.encode("utf-8"), self.current_file, self.password
            )
            messagebox.showinfo("Success", "File saved successfully.")
        else:
            messagebox.showwarning("Warning", "No file selected.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
