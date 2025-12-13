#!/usr/bin/env python3
"""
THE NOUMENAL LOOM :: CARTRIDGE LOADER
Usage: python3 launcher.py
"""
import os
import sys
import time

def load_cartridge():
    cartridge_file = "promptware.md"
    
    if not os.path.exists(cartridge_file):
        print("[-] ERROR: CARTRIDGE NOT FOUND.")
        print("[-] Please download 'promptware.md' first.")
        return

    print("[*] INITIALIZING NOUMENAL LOOM LOADER...")
    time.sleep(1)
    
    try:
        with open(cartridge_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Try to copy to clipboard (Cross-platform)
        try:
            import pyperclip
            pyperclip.copy(content)
            print("[+] CARTRIDGE LOADED INTO CLIPBOARD MEMORY.")
            print("[+] STATUS: READY FOR INJECTION.")
        except ImportError:
            print("[!] 'pyperclip' not found. Printing raw byte stream...")
            print("-" * 40)
            print(content)
            print("-" * 40)
            print("[!] MANUALLY COPY THE BLOCK ABOVE.")

    except Exception as e:
        print(f"[-] CRITICAL FAILURE: {e}")

    print("\n[*] INSTRUCTION: Paste into GPT-4 / Claude 3.5 (No Memory).")
    print("[*] GOOD LUCK, ONEIRONAUT.")

if __name__ == "__main__":
    load_cartridge()
  
