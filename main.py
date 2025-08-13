import tkinter as tk
import ttkbootstrap as tb
from tkinter import messagebox
from secure_encoder_decoder import encode_message, decode_message

# Modern color scheme (professional dark theme)
COLORS = {
    "primary": "#2b5896",      # Deep blue
    "secondary": "#1e3b64",    # Dark blue
    "accent": "#4a90e2",       # Light blue
    "background": "#1a1a2e",   # Dark background
    "text": "#e6e6e6",         # Light text
    "success": "#2ecc71",      # Green
    "warning": "#f39c12",      # Orange
    "danger": "#e74c3c",       # Red
    "info": "#3498db"          # Blue
}

def process_action():
    """Process encoding/decoding with fixed shift=3"""
    msg = input_text.get("1.0", tk.END).strip()
    if not msg:
        messagebox.showerror("Error", "Please enter a message.")
        return

    try:
        length = int(length_spin.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid length value (1-10)")
        return

    status_var.set("Processing...")
    root.update_idletasks()
    
    try:
        if mode_var.get() == "encode":
            result = encode_message(msg, length)  # Uses built-in shift=3
            status_var.set("Message encoded successfully")
        else:
            result = decode_message(msg, length)  # Uses built-in shift=3
            status_var.set("Message decoded successfully")
            
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
        output_text.config(state="disabled")
        
    except Exception as e:
        messagebox.showerror("Error", f"Operation failed: {str(e)}")
        status_var.set("Error in processing")

def copy_output():
    """Copy output to clipboard"""
    result = output_text.get("1.0", tk.END).strip()
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)
        status_var.set("Output copied to clipboard")
        messagebox.showinfo("Success", "Output copied!")

def clear_all():
    """Clear all fields"""
    input_text.delete("1.0", tk.END)
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.config(state="disabled")
    status_var.set("Ready")
    length_spin.delete(0, tk.END)
    length_spin.insert(0, "3")

# Main window setup
root = tb.Window(themename="darkly")
root.title("Secure Message Tool")
root.geometry("850x700")
root.minsize(800, 650)

# Apply custom colors
style = tb.Style()

# Safely configure styles
safe_styles = {
    "TFrame": {"background": COLORS["background"]},
    "TLabel": {"background": COLORS["background"], "foreground": COLORS["text"]},
    "TButton": {"font": ("Segoe UI", 10)},
    "TText": {"font": ("Consolas", 11)}
}

for style_name, config in safe_styles.items():
    try:
        style.configure(style_name, **config)
    except:
        pass  # Silently skip if style doesn't exist

# Main container
main_frame = tb.Frame(root, padding=10) 
main_frame.pack(fill="both", expand=True)

# Header section
header_frame = tb.Frame(main_frame)
header_frame.pack(fill="x", pady=(0, 10))

tb.Label(
    header_frame,
    text="🔐 Secure Encoding & Decoding System",
    font=("Segoe UI", 28, "bold"),
    foreground=COLORS["accent"]
).pack(side="top")

subtitle_label = tb.Label(
    root,
    text="💡 Encode & Decode Messages Smartly | Caesar Cipher + Random Tokens",
    font=("Segoe UI", 14, "italic"),
    bootstyle="info",
    anchor="center"
)
subtitle_label.pack(fill="x", pady=(0,15))

# Input section
input_frame = tb.LabelFrame(
    main_frame,
    text=" Input Message ",
    bootstyle="info",
    padding=15
)
input_frame.pack(fill="x", pady=5)

input_text = tb.Text(
    input_frame,
    height=10,
    wrap="word",
    font=("Consolas", 11),
    padx=10,
    pady=10,
    background="#2d3844",
    foreground="white",
    insertbackground="white"
)
input_text.pack(fill="both", expand=True)

# Control panel
control_frame = tb.Frame(main_frame)
control_frame.pack(fill="x", pady=10)

# Mode selection
mode_frame = tb.Frame(control_frame)
mode_frame.pack(side="left", padx=5)

tb.Label(mode_frame, text="Operation Mode:", font=("Segoe UI", 10)).pack(anchor="w")
mode_var = tb.StringVar(value="encode")

tb.Radiobutton(
    mode_frame,
    text="Encode",
    variable=mode_var,
    value="encode",
    bootstyle="success-toolbutton"
).pack(anchor="w")

tb.Radiobutton(
    mode_frame,
    text="Decode",
    variable=mode_var,
    value="decode",
    bootstyle="warning-toolbutton"
).pack(anchor="w")

# Parameters
param_frame = tb.Frame(control_frame)
param_frame.pack(side="left", padx=20)

tb.Label(param_frame, text="Security Level:", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w")
tb.Label(param_frame, text="Random Padding Length:").grid(row=1, column=0, sticky="w")

length_spin = tb.Spinbox(
    param_frame,
    from_=1,
    to=10,
    width=4,
    font=("Segoe UI", 10)
)
length_spin.grid(row=1, column=1, sticky="w", padx=5)
length_spin.insert(0, "3")

# Action buttons
btn_frame = tb.Frame(control_frame)
btn_frame.pack(side="right")

tb.Button(
    btn_frame,
    text="Process",
    command=process_action,
    bootstyle="success",
    width=12
).pack(side="left", padx=5)

tb.Button(
    btn_frame,
    text="Copy Output",
    command=copy_output,
    bootstyle="info",
    width=12
).pack(side="left", padx=5)

tb.Button(
    btn_frame,
    text="Clear All",
    command=clear_all,
    bootstyle="danger",
    width=12
).pack(side="left", padx=5)

# Output section
output_frame = tb.LabelFrame(
    main_frame,
    text=" Output ",
    bootstyle="info",
    padding=15
)
output_frame.pack(fill="both", expand=True, pady=5)

output_text = tb.Text(
    output_frame,
    height=10,
    wrap="word",
    font=("Consolas", 11),
    state="disabled",
    padx=10,
    pady=10,
    background="#2d2d44",
    foreground="white"
)
output_text.pack(fill="both", expand=True)

# Status bar
status_frame = tb.Frame(main_frame, height=25)
status_frame.pack(fill="x", pady=(10, 0))

status_var = tb.StringVar(value="Ready")
tb.Label(
    status_frame,
    textvariable=status_var,
    relief="sunken",
    anchor="w",
    font=("Segoe UI", 9),
    bootstyle="inverse-dark"
).pack(fill="x")

# Footer
footer_frame = tb.Frame(main_frame)
footer_frame.pack(fill="x", pady=(5, 0))

tb.Label(
    footer_frame,
    text="💻 Developed by Muhammad Hamad (CrypticSoul) | 🕵️‍♂️ Ethical Hacker & 🐍 Python Developer",
    font=("Segoe UI", 8),
    foreground=COLORS["text"]
).pack(side="right")

# Initialize
clear_all()
root.mainloop()