#------------- IMPORT -------------#
from os import system as c
import time
import os

#------------- COLOUR -------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

#------------- LOGO -------------#
def logo():
    c('clear')
    print(f"""{R}
 ▗▄▖ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄
▐▌ ▐▌ █   █   █   █   █ 
▐▛▀▜▌ █  ▄█▄  █   █   █ 
▐▌ ▐▌ █   █   █   █   █ 
 ▝ ▝  ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀
{C}   HACKING WORLD VIP FLASH TOOL
""")

#------------- CHECK ROOT -------------#
def check_root():
    if os.path.exists("/system/xbin/su") or os.path.exists("/system/bin/su"):
        return True
    else:
        logo()
        print(f"{R}[!] ROOT ACCESS NOT FOUND!")
        print(f"{Y}[!] This Tool Only Works On Rooted Devices.")
        input(f"\n{A}Press Enter To Exit...")
        exit()

#------------- ANIMATION -------------#
def loading(txt):
    logo()
    print(f"{P}{txt}\n")
    for i in range(1, 11):
        bar = f"{Y}[{G}{'█'*i}{A}>{' '*(10-i)}] {i*10}%"
        print(bar, end="\r")
        time.sleep(0.3)
    print(f"\n{G}[✓] DONE!\n")
    time.sleep(1)

def countdown(sec):
    while sec:
        print(f"{R}[!] Device Flashing In: {Y}{sec} Sec", end='\r')
        time.sleep(1)
        sec -= 1
    print()

#------------- FACTORY FLASH WITH NUMBER (Prank) -------------#
def factory_flash_number():
    logo()
    number = input(f"{C}ENTER TARGET PHONE NUMBER: {Y}+880")
    full_number = "+880" + number
    loading(f"Connecting to Device {full_number}...")
    c('espeak "Starting Factory Flash"')
    loading("Wiping System Data...")
    loading("Erasing Internal Storage...")
    countdown(10)
    c('espeak "Phone Flashed Successfully"')
    print(f"{G}[✓] Device {full_number} Successfully Flashed (Prank)!")
    print(f"{C}All Data and Settings Erased from {full_number}!")
    time.sleep(2)
    input(f"\n{A}Press Enter to Return to Menu...")
    menu()

#------------- MAIN MENU -------------#
def menu():
    logo()
    print(f"{Y}[1] {C}START Factory Flash by Number (Prank)")
    print(f"{Y}[0] {C}EXIT VIP TOOL")
    print(f"{C}--------------------------------------------")
    choice = input(f"{P}[?] SELECT OPTION: ")
    if choice == '1':
        factory_flash_number()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] Invalid Option!")
        time.sleep(1)
        menu()

#------------- START TOOL -------------#
check_root()
menu()