from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
import ttkbootstrap as tb

def translate_text():
    try:
        src_lang = source_lang.get()
        dest_lang = target_lang.get()
        text_to_translate = source_text.get(1.0, END).strip()
        
        if not text_to_translate:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return

        translator = Translator()
        translated_text = translator.translate(text_to_translate, src=src_lang, dest=dest_lang).text

        target_text.delete(1.0, END)
        target_text.insert(END, translated_text)

    except Exception as e:
        messagebox.showerror("Error", f"Translation failed!\n{e}")

# Initialize themed window
root = tb.Window(themename="superhero")  # Use 'superhero' theme for modern UI
root.title("Language Translator")
root.geometry("550x600")
root.resizable(False, False)

# Header
header_label = tb.Label(root, text="Language Translator", font=("Arial", 20, "bold"))
header_label.pack(pady=10)

# Source Text Section
source_frame = tb.Frame(root)
source_frame.pack(pady=5, fill="both", padx=20)

source_label = tb.Label(source_frame, text="Enter Text:", font=("Arial", 12, "bold"))
source_label.pack(anchor="w")

source_text = Text(source_frame, font=("Arial", 12), height=5, wrap=WORD)
source_text.pack(fill="both", padx=5, pady=5)

# Language Selection
lang_frame = tb.Frame(root)
lang_frame.pack(pady=5, fill="x", padx=20)

languages = list(LANGUAGES.values())

source_lang = ttk.Combobox(lang_frame, values=languages, state="readonly")
source_lang.set("english")
source_lang.pack(side="left", padx=10)

translate_button = tb.Button(lang_frame, text="Translate", command=translate_text, bootstyle="primary")
translate_button.pack(side="left", padx=10)

target_lang = ttk.Combobox(lang_frame, values=languages, state="readonly")
target_lang.set("hindi")
target_lang.pack(side="left", padx=10)

# Translated Text Section
target_frame = tb.Frame(root)
target_frame.pack(pady=5, fill="both", padx=20)

target_label = tb.Label(target_frame, text="Translated Text:", font=("Arial", 12, "bold"))
target_label.pack(anchor="w")

target_text = Text(target_frame, font=("Arial", 12), height=5, wrap=WORD, bg="#f0f0f0")
target_text.pack(fill="both", padx=5, pady=5)

# Run App
root.mainloop()






