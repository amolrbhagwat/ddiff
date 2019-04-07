import tkinter as Tkinter
import tkinter.filedialog as filedialog
from colorama import Fore, Style
from colorama import init
import os
import sys

root = Tkinter.Tk()
root.withdraw() #use to hide tkinter window
root.wm_attributes('-topmost', 1)

init() # For colorama

source_dir = ''
target_dir = ''

def show_main_menu():
    print("1. Set source directory", "(Currently: ", source_dir, ")")
    print("2. Set target directory", "(Currently: ", target_dir, ")")
    print("3. Check if target contains files under source")
    print("4. Exit")

def prompt_directory(title):
    global root

    currdir = os.getcwd()
    return filedialog.askdirectory(parent=root, initialdir=currdir, title=title)

def create_index(directory):
    filename_dirs_map = {}
    for dirname, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename not in filename_dirs_map:
                filename_dirs_map[filename] = []
            filename_dirs_map[filename].append(dirname)

    return filename_dirs_map

def create_list_of_src_files(directory):
    file_list = []
    for dirname, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_list.append(filename)

    return file_list

def ddiff():
    global source_dir, target_dir
    total_found = 0
    total_missing = 0

    index = create_index(target_dir)
    src_list = create_list_of_src_files(source_dir)

    for filename in src_list:
        if filename in index:
            total_found += 1
            print(Fore.GREEN + filename + " is present in the target directory under " + str(index[filename]))
        else:
            total_missing += 1
            print(Fore.RED + filename + " IS MISSING FROM TARGET DIRECTORY!")

    print()
    print(Fore.GREEN + "Total found: " + str(total_found))
    print(Fore.RED + "Total missing: " + str(total_missing))
    print(Style.RESET_ALL)

def main():
    global source_dir, target_dir
    
    while True:
        show_main_menu()
        option = input("Enter an option: ")
        if option == "1":
            source_dir = prompt_directory('Select source directory')
        if option == "2":
            target_dir = prompt_directory('Select target directory')
        if option == "3":
            ddiff()
        if option == "4":
            sys.exit(0)

main()
