import tkinter as Tkinter
import tkinter.filedialog as filedialog
import os
import sys

dir1 = ''
dir2 = ''

def show_main_menu():
    print("\n")
    print("Directory 1 is set to: ", dir1)
    print("Directory 2 is set to: ", dir2)
    print("\n")

    print("1. Set directory 1")
    print("2. Set directory 2")
    print("3. Dir 1 contained in dir 2?")
    print("4. Dir 2 contained in dir 1?")
    print("5. Exit")

def prompt_directory():
    root = Tkinter.Tk()
    root.withdraw() #use to hide tkinter window
    root.wm_attributes('-topmost', 1)

    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')

    return tempdir

def main():
    global dir1, dir2
    
    while True:
        show_main_menu()
        option = input("Enter an option: ")
        if option == "1":
            dir1 = prompt_directory()
        if option == "2":
            dir2 = prompt_directory()
        if option == "5":
            sys.exit(0)

main()
