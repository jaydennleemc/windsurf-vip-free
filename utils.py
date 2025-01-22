"""
Utility functions for the Windsurf account registration program
"""
import os
import time
import shutil
import logging
import tkinter as tk
from tkinter import messagebox
from config import (
    CHROME_USER_DATA_DIR,
    CHROME_TEMP_DIR,
    CHROME_EXECUTABLE
)

def format_email(prefix, number, domain):
    """Format email address with number"""
    try:
        num = int(number)
        return f"{prefix}{num}@{domain}"
    except (ValueError, TypeError):
        return f"{prefix}{number}@{domain}"

def center_window(window):
    """Center a tkinter window on the screen"""
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def show_message(title, message, type_="info"):
    """Show message box with specified type"""
    if type_ == "yesno":
        return messagebox.askyesno(title, message)
    elif type_ == "error":
        messagebox.showerror(title, message)
    else:
        # 创建一个可以复制文本的对话框
        dialog = tk.Toplevel()
        dialog.title(title)
        dialog.geometry("400x200")
        dialog.resizable(False, False)
        dialog.attributes('-topmost', True)
        
        # 添加文本框
        text = tk.Text(dialog, wrap=tk.WORD, padx=10, pady=10)
        text.insert(tk.END, message)
        text.pack(fill=tk.BOTH, expand=True)
        text.config(state="normal")  # 允许选择和复制
        
        # 添加确定按钮
        button = tk.Button(dialog, text="确定", command=dialog.destroy)
        button.pack(pady=10)
        
        # 设置焦点并等待
        dialog.focus_set()
        dialog.grab_set()
        dialog.wait_window()

def clean_all_chrome_data():
    """Clean all Chrome user data"""
    try:
        # Remove Chrome user data directory
        if os.path.exists(CHROME_USER_DATA_DIR):
            shutil.rmtree(CHROME_USER_DATA_DIR)
            
        # Remove Chrome temp directory
        if os.path.exists(CHROME_TEMP_DIR):
            shutil.rmtree(CHROME_TEMP_DIR)
            
        # Recreate directories
        os.makedirs(CHROME_USER_DATA_DIR, exist_ok=True)
        os.makedirs(CHROME_TEMP_DIR, exist_ok=True)
        
        logging.info("Chrome data cleaned successfully")
        
    except Exception as e:
        logging.error(f"Error cleaning Chrome data: {e}")
        raise
