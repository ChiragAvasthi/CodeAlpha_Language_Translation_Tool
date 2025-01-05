import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Function to translate text
def translate_text():
    source_text = input_text.get("1.0", tk.END).strip()
    source_lang = source_lang_combo.get()
    target_lang = target_lang_combo.get()

    if not source_text:
        messagebox.showerror("Input Error", "Please enter text to translate.")
        return
    if not source_lang or not target_lang:
        messagebox.showerror("Selection Error", "Please select both source and target languages.")
        return

    try:
        translator = Translator()
        translation = translator.translate(source_text, src=source_lang, dest=target_lang)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translation.text)
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {e}")

# Create main window
root = tk.Tk()
root.title("🌟 Language Translator 🌟")
root.geometry("650x550")
root.resizable(False, False)
root.configure(bg="#222831")

# Styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Helvetica", 12), background="#222831", foreground="white")
style.configure("TButton", font=("Helvetica", 12, "bold"), background="#00ADB5", foreground="white", relief="flat")
style.map("TButton", background=[("active", "#007F87")])
style.configure("TCombobox", font=("Helvetica", 11), fieldbackground="#eeeeee", foreground="#393E46")

# Title label
title_label = tk.Label(
    root, text="🌍 Language Translator 🌐", font=("Helvetica", 20, "bold"), fg="#00ADB5", bg="#222831"
)
title_label.pack(pady=15)

# Input text area
input_label = ttk.Label(root, text="Enter text to translate:")
input_label.pack()
input_text = tk.Text(root, height=7, width=65, wrap=tk.WORD, font=("Helvetica", 12), bg="#393E46", fg="#eeeeee")
input_text.pack(pady=10)

# Language selection frame
lang_frame = tk.Frame(root, bg="#222831")
lang_frame.pack(pady=15)

source_lang_label = ttk.Label(lang_frame, text="Source Language:")
source_lang_label.grid(row=0, column=0, padx=5, pady=5)
source_lang_combo = ttk.Combobox(lang_frame, values=list(LANGUAGES.values()), width=25, state="readonly")
source_lang_combo.grid(row=0, column=1, padx=5, pady=5)

target_lang_label = ttk.Label(lang_frame, text="Target Language:")
target_lang_label.grid(row=1, column=0, padx=5, pady=5)
target_lang_combo = ttk.Combobox(lang_frame, values=list(LANGUAGES.values()), width=25, state="readonly")
target_lang_combo.grid(row=1, column=1, padx=5, pady=5)

# Translate button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=15)

# Output text area
output_label = ttk.Label(root, text="Translated text:")
output_label.pack()
output_text = tk.Text(root, height=7, width=65, wrap=tk.WORD, font=("Helvetica", 12), bg="#393E46", fg="#eeeeee")
output_text.pack(pady=10)

# Footer
footer_label = tk.Label(
    root,
    text="© 2025 Language Translator | Designed by Chirag Avasthi",
    font=("Helvetica", 10),
    fg="#eeeeee",
    bg="#222831",
)
footer_label.pack(pady=10)

# Run the application
root.mainloop()
