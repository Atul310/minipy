# os module -- >>
'''
This module provides a portable way of using operating system dependent functionality
. If you just want to read or write a file see open(), if you want to manipulate paths,
 see the os.path module, and if you want to read all the lines in all the files on the
 command line see the fileinput module. For creating temporary files and directories see
  the tempfile module, and for high-level file and directory handling see the shutil module.
==============================================================================================
different method and  functions in os module ==>>
os.system '''
import os

if __name__ == "__main__":
    while True:
        X = input("what i want to say: ")
        if X == "@":
            break

    command = f"say {X}"
    os.system.playsound(command)





