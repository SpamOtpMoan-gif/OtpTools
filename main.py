#!/usr/bin/env python3
import os
import sys
import json
import time
import random
import subprocess
import platform
from datetime import datetime

VERSION = "2.2.7"
AUTHOR = "XERXEZ & BUDI"
USERS = 182

os.system("clear" if os.name == "posix" else "cls")

def banner():
    print("""
    ╔═══════════════════════════════════════════════╗
    ║              DARSHNESS TOOLS v2.2.7          ║
    ╠═══════════════════════════════════════════════╣
    ║  Author  : MonzapAhAh                        ║
    ║  Version : 2.2.7                             ║
    ║  Users   : 182 User                          ║
    ║  Tanggal : 11-08-2026                        ║
    ║  IP      : 112.215.235.1                     ║
    ║  ID      : u0_a330                           ║
    ║  NAMA    : Mkan                              ║
    ║  STATUS  : Fullup                            ║
    ╚═══════════════════════════════════════════════╝
    """)

def menu():
    print("""
    ╔═══════════════════════════════════════════════╗
    ║                    [ MENU ]                   ║
    ╠═══════════════════════════════════════════════╣
    ║  [ 01 ] SPAM OTP                             ║
    ║  [ 02 ] NGL SPAM                             ║
    ║  [ 03 ] SPAM EMAIL                           ║
    ║  [ 04 ] SPAM BOT TELEGRAM                    ║
    ║  [ 05 ] IP TRACKER                           ║
    ║  [ 06 ] PHONE INFO                           ║
    ║  [ 07 ] WIFI KILLER                          ║
    ║  [ 08 ] GANTI WARNA                          ║
    ║  [ 09 ] BUG WHATSAPP                         ║
    ║  [ 10 ] AI ASSISTANT                         ║
    ║  [ 11 ] TELEPHON SIM CARD                    ║
    ║  [ 12 ] INSTAGRAM STALKER                    ║
    ║  [ 00 ] KELUAR                               ║
    ╚═══════════════════════════════════════════════╝
    """)

def spam_otp():
    os.system("python otp_spam.py")
    input("\nTekan Enter untuk kembali...")

def ngl_spam():
    os.system("python ngl_spam.py")
    input("\nTekan Enter untuk kembali...")

def spam_email():
    os.system("python email_spam.py")
    input("\nTekan Enter untuk kembali...")

def spam_telegram():
    os.system("python telegram_bot_spam.py")
    input("\nTekan Enter untuk kembali...")

def ip_tracker():
    os.system("python ip_tracker.py")
    input("\nTekan Enter untuk kembali...")

def phone_info():
    os.system("python phone_info.py")
    input("\nTekan Enter untuk kembali...")

def wifi_killer():
    os.system("python wifi_killer.py")
    input("\nTekan Enter untuk kembali...")

def ganti_warna():
    os.system("python warna.py")
    input("\nTekan Enter untuk kembali...")

def bug_whatsapp():
    os.system("python whatsapp_bug.py")
    input("\nTekan Enter untuk kembali...")

def ai_assistant():
    os.system("python ai_assistant.py")
    input("\nTekan Enter untuk kembali...")

def telephon_sim():
    os.system("python sim_card.py")
    input("\nTekan Enter untuk kembali...")

def insta_stalker():
    os.system("python insta_stalker.py")
    input("\nTekan Enter untuk kembali...")

def main():
    while True:
        banner()
        menu()
        choice = input("    ────► PILIH : ").strip()
        
        if choice == "1" or choice == "01":
            spam_otp()
        elif choice == "2" or choice == "02":
            ngl_spam()
        elif choice == "3" or choice == "03":
            spam_email()
        elif choice == "4" or choice == "04":
            spam_telegram()
        elif choice == "5" or choice == "05":
            ip_tracker()
        elif choice == "6" or choice == "06":
            phone_info()
        elif choice == "7" or choice == "07":
            wifi_killer()
        elif choice == "8" or choice == "08":
            ganti_warna()
        elif choice == "9" or choice == "09":
            bug_whatsapp()
        elif choice == "10":
            ai_assistant()
        elif choice == "11":
            telephon_sim()
        elif choice == "12":
            insta_stalker()
        elif choice == "0" or choice == "00":
            print("\n    Keluar... Terima kasih sudah pakai tools ini!")
            sys.exit(0)
        else:
            print("\n    Pilihan salah! Coba lagi.")
            time.sleep(1)

if __name__ == "__main__":
    main()
