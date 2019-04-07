import tkinter as Tkinter
import tkinter.filedialog as filedialog
import os
import sys

root = Tkinter.Tk()
root.withdraw() #use to hide tkinter window
root.wm_attributes('-topmost', 1)

source_dir = ''
target_dir = ''

def show_main_menu():
    print("\n")

    print("1. Set source directory", "(Currently: ", source_dir, ")")
    print("2. Set target directory", "(Currently: ", target_dir, ")")
    print("3. Check if target contains files under source")
    print("4. Exit")

def prompt_directory(title):
    global root

    currdir = os.getcwd()
    return filedialog.askdirectory(parent=root, initialdir=currdir, title=title)


def main():
    global source_dir, target_dir
    
    while True:
        show_main_menu()
        option = input("Enter an option: ")
        if option == "1":
            source_dir = prompt_directory('Select source directory')
        if option == "2":
            target_dir = prompt_directory('Select target directory')
        if option == "4":
            sys.exit(0)

main()
