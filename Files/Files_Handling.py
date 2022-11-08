# -------------------
# "a" Append  Open File For Appending Values, Create File If Not Exists
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------


# لازم افتح فايل موجود جوا الوورك داير 
import os

# Main Current Working Directory
print(os.getcwd())   # اطبع الوورك داير 

# Directory For The Opened File
print(os.path.dirname(os.path.abspath(__file__)))   # الملف الي واقف فيه 

# Change Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))    # تغيير الوورك داير الى الملف الي واقف فيه 

print(os.getcwd())   

print(os.path.abspath(__file__))

#file = open(r"D:\Python\Files\nfiles\osama.txt")

file = open("taha.txt")  

