"""
Task 01 - Temperature Converter
Converts temperature between Celsius, Fahrenheit and Kelvin using a styled Tkinter GUI.
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- Color & Font Theme ----------------

BG_COLOR = "#1e293b"        # dark slate background
CARD_COLOR = "#27344d"      # slightly lighter card background
ACCENT_COLOR = "#38bdf8"    # sky blue accent
TEXT_COLOR = "#f1f5f9"      # near-white text
SUBTEXT_COLOR = "#94a3b8"   # muted gray text
RESULT_COLOR = "#4ade80"    # green for the result

FONT_HEADING = ("Segoe UI", 18, "bold")
FONT_LABEL = ("Segoe UI", 11)
FONT_ENTRY = ("Segoe UI", 13)
FONT_RESULT = ("Segoe UI", 14, "bold")


# ---------------- Conversion Functions ----------------

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32


# ---------------- Main Logic ----------------

def convert_temperature():
    # Everything is wrapped in a try/except so that ANY unexpected error
    # shows up as a popup instead of failing silently in the background.
    try:
        try:
            value = float(entry_value.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        from_scale = from_var.get()
        to_scale = to_var.get()

        if from_scale == to_scale:
            result_label.config(text="Both scales are the same — no conversion needed.")
            return

        conversions = {
            ("Celsius", "Fahrenheit"): celsius_to_fahrenheit,
            ("Celsius", "Kelvin"): celsius_to_kelvin,
            ("Fahrenheit", "Celsius"): fahrenheit_to_celsius,
            ("Fahrenheit", "Kelvin"): fahrenheit_to_kelvin,
            ("Kelvin", "Celsius"): kelvin_to_celsius,
            ("Kelvin", "Fahrenheit"): kelvin_to_fahrenheit,
        }

        convert_func = conversions[(from_scale, to_scale)]
        result = convert_func(value)

        symbol = {"Celsius": "°C", "Fahrenheit": "°F", "Kelvin": "K"}[to_scale]
        result_label.config(text=f"{result:.2f} {symbol}")

    except Exception as e:
        messagebox.showerror("Something Went Wrong", f"Error: {e}")


def clear_fields():
    entry_value.delete(0, tk.END)
    result_label.config(text="")
    entry_value.focus()


def swap_scales():
    # Quick way to flip "From" and "To" without re-selecting both dropdowns
    from_val, to_val = from_var.get(), to_var.get()
    from_var.set(to_val)
    to_var.set(from_val)


# ---------------- GUI Setup ----------------

window = tk.Tk()
window.title("Temperature Converter")
window.geometry("440x620")
window.minsize(440, 620)
window.resizable(True, True)
window.configure(bg=BG_COLOR)

# Style the dropdown menus to match the dark theme
style = ttk.Style()
style.theme_use("default")
style.configure(
    "TCombobox",
    fieldbackground=CARD_COLOR,
    background=CARD_COLOR,
    foreground=TEXT_COLOR,
    arrowcolor=TEXT_COLOR,
    bordercolor=ACCENT_COLOR,
    padding=6,
)
style.map("TCombobox", fieldbackground=[("readonly", CARD_COLOR)])

# ---- Header ----
header = tk.Frame(window, bg=BG_COLOR)
header.pack(pady=(30, 10))

tk.Label(header, text="🌡️", font=("Segoe UI Emoji", 28), bg=BG_COLOR).pack()
tk.Label(header, text="Temperature Converter", font=FONT_HEADING,
         bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=(5, 0))
tk.Label(header, text="Convert between Celsius, Fahrenheit & Kelvin",
         font=FONT_LABEL, bg=BG_COLOR, fg=SUBTEXT_COLOR).pack(pady=(2, 0))

# ---- Card container ----
card = tk.Frame(window, bg=CARD_COLOR, padx=25, pady=25)
card.pack(padx=30, pady=15, fill="both", expand=True)

# Input field
tk.Label(card, text="Enter Value", font=FONT_LABEL, bg=CARD_COLOR, fg=SUBTEXT_COLOR).pack(anchor="w")
entry_value = tk.Entry(card, font=FONT_ENTRY, justify="center", bg="#1e293b",
                        fg=TEXT_COLOR, insertbackground=TEXT_COLOR, relief="flat")
entry_value.pack(fill="x", pady=(5, 15), ipady=8)

# From / To row
scales_row = tk.Frame(card, bg=CARD_COLOR)
scales_row.pack(fill="x", pady=(0, 5))

from_col = tk.Frame(scales_row, bg=CARD_COLOR)
from_col.pack(side="left", expand=True, fill="x")
tk.Label(from_col, text="From", font=FONT_LABEL, bg=CARD_COLOR, fg=SUBTEXT_COLOR).pack(anchor="w")
from_var = tk.StringVar(value="Celsius")
from_menu = ttk.Combobox(from_col, textvariable=from_var, state="readonly", width=12,
                          values=["Celsius", "Fahrenheit", "Kelvin"], font=FONT_LABEL)
from_menu.pack(fill="x", pady=5)

swap_btn = tk.Button(scales_row, text="⇄", font=("Segoe UI", 12, "bold"), command=swap_scales,
                      bg=ACCENT_COLOR, fg="#0f172a", relief="flat", width=3, cursor="hand2")
swap_btn.pack(side="left", padx=8, pady=(22, 0))

to_col = tk.Frame(scales_row, bg=CARD_COLOR)
to_col.pack(side="left", expand=True, fill="x")
tk.Label(to_col, text="To", font=FONT_LABEL, bg=CARD_COLOR, fg=SUBTEXT_COLOR).pack(anchor="w")
to_var = tk.StringVar(value="Fahrenheit")
to_menu = ttk.Combobox(to_col, textvariable=to_var, state="readonly", width=12,
                        values=["Celsius", "Fahrenheit", "Kelvin"], font=FONT_LABEL)
to_menu.pack(fill="x", pady=5)

# Buttons
button_row = tk.Frame(card, bg=CARD_COLOR)
button_row.pack(fill="x", pady=(20, 10))

convert_btn = tk.Button(button_row, text="Convert", font=("Segoe UI", 12, "bold"),
                         bg=ACCENT_COLOR, fg="#0f172a", relief="flat", cursor="hand2",
                         activebackground="#0ea5e9", command=convert_temperature)
convert_btn.pack(side="left", expand=True, fill="x", ipady=8, padx=(0, 8))

clear_btn = tk.Button(button_row, text="Clear", font=("Segoe UI", 12),
                       bg="#475569", fg=TEXT_COLOR, relief="flat", cursor="hand2",
                       activebackground="#334155", command=clear_fields)
clear_btn.pack(side="left", expand=True, fill="x", ipady=8)

# Result display
result_label = tk.Label(card, text="", font=FONT_RESULT, bg=CARD_COLOR, fg=RESULT_COLOR)
result_label.pack(pady=(15, 0))

window.mainloop()