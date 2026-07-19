import tkinter as tk
from tkinter import ttk, messagebox
def encrypt(text: str, key: int) -> str:
    result = []
    for char in text:
        if char.isupper():
            x = ord(char) - ord('A')
            result.append(chr((x + key) % 26 + ord('A')))
        elif char.islower():
            x = ord(char) - ord('a')
            result.append(chr((x + key) % 26 + ord('a')))
        else:
            result.append(char)
    return "".join(result)


def decrypt(cipher_text: str, key: int) -> str:
    return encrypt(cipher_text, -key)

class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        root.title("Caesar Cipher — Encrypt & Decrypt")
        root.geometry("520x480")
        root.resizable(False, False)

        pad = {"padx": 12, "pady": 6}
        ttk.Label(root, text="Enter text:", font=("Segoe UI", 10, "bold")).pack(anchor="w", **pad)
        self.input_box = tk.Text(root, height=5, wrap="word")
        self.input_box.pack(fill="x", padx=12)
        key_frame = ttk.Frame(root)
        key_frame.pack(fill="x", **pad)
        ttk.Label(key_frame, text="Shift key (n):").pack(side="left")
        self.key_var = tk.IntVar(value=3)
        self.key_spin = ttk.Spinbox(key_frame, from_=-100, to=100, textvariable=self.key_var, width=8)
        self.key_spin.pack(side="left", padx=8)
        btn_frame = ttk.Frame(root)
        btn_frame.pack(fill="x", **pad)
        ttk.Button(btn_frame, text="Encrypt", command=self.do_encrypt).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="Decrypt", command=self.do_decrypt).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="Validate (Encrypt -> Decrypt)", command=self.do_validate).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="Clear", command=self.clear_all).pack(side="left", padx=4)
        ttk.Label(root, text="Result:", font=("Segoe UI", 10, "bold")).pack(anchor="w", **pad)
        self.output_box = tk.Text(root, height=5, wrap="word", state="disabled", background="#f4f4f4")
        self.output_box.pack(fill="x", padx=12)
        self.status_var = tk.StringVar(value="")
        self.status_label = ttk.Label(root, textvariable=self.status_var, font=("Segoe UI", 9, "italic"))
        self.status_label.pack(anchor="w", padx=12, pady=(6, 0))

    def _get_input(self) -> str:
        return self.input_box.get("1.0", "end-1c")

    def _set_output(self, text: str):
        self.output_box.config(state="normal")
        self.output_box.delete("1.0", "end")
        self.output_box.insert("1.0", text)
        self.output_box.config(state="disabled")

    def _get_key(self):
        try:
            return int(self.key_var.get())
        except (tk.TclError, ValueError):
            messagebox.showerror("Invalid Key", "Please enter a valid integer key.")
            return None

    def do_encrypt(self):
        key = self._get_key()
        if key is None:
            return
        text = self._get_input()
        self._set_output(encrypt(text, key))
        self.status_var.set("")

    def do_decrypt(self):
        key = self._get_key()
        if key is None:
            return
        text = self._get_input()
        self._set_output(decrypt(text, key))
        self.status_var.set("")

    def do_validate(self):
        key = self._get_key()
        if key is None:
            return
        original = self._get_input()
        cipher_text = encrypt(original, key)
        round_trip = decrypt(cipher_text, key)

        self._set_output(f"Encrypted: {cipher_text}\nDecrypted: {round_trip}")

        if round_trip == original:
            self.status_var.set("[VALID] Decryption matches original text.")
            self.status_label.config(foreground="green")
        else:
            self.status_var.set("[ERROR] Mismatch between original and decrypted text.")
            self.status_label.config(foreground="red")

    def clear_all(self):
        self.input_box.delete("1.0", "end")
        self._set_output("")
        self.status_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()