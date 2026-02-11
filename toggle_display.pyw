import subprocess
import ctypes
import customtkinter as ctk

SM_CMONITORS = 80


def get_monitor_count():
    return ctypes.windll.user32.GetSystemMetrics(SM_CMONITORS)


def is_extended():
    return get_monitor_count() > 1


def update_ui():
    if is_extended():
        status_label.configure(text="Extended", text_color="#34d399")
        icon_label.configure(text="\U0001F5B5 \U0001F5B5")
        toggle_btn.configure(text="Switch to Single")
    else:
        status_label.configure(text="Single", text_color="#60a5fa")
        icon_label.configure(text="\U0001F5B5")
        toggle_btn.configure(text="Switch to Extended")


def toggle_display():
    if is_extended():
        subprocess.run(["DisplaySwitch.exe", "/internal"])
    else:
        subprocess.run(["DisplaySwitch.exe", "/extend"])
    root.after(500, update_ui)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Display Toggle")
root.attributes("-topmost", True)
root.resizable(False, False)
root.geometry("280x220")

frame = ctk.CTkFrame(root, corner_radius=12)
frame.pack(fill="both", expand=True, padx=12, pady=12)

title_label = ctk.CTkLabel(frame, text="Display Mode", font=("Segoe UI", 18, "bold"))
title_label.pack(pady=(16, 4))

icon_label = ctk.CTkLabel(frame, text="", font=("Segoe UI", 28))
icon_label.pack(pady=(4, 4))

status_label = ctk.CTkLabel(frame, text="", font=("Segoe UI", 14, "bold"))
status_label.pack(pady=(0, 12))

toggle_btn = ctk.CTkButton(frame, text="", font=("Segoe UI", 14, "bold"),
                           height=42, corner_radius=10, command=toggle_display)
toggle_btn.pack(padx=20, pady=(0, 16))

update_ui()
root.mainloop()
