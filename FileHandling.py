f=open('file1.txt','w')
f.write("Eiffel Tower")
f.close()
f1=open("file1.txt","r")                       #check that the file is closed before opening it again
str=f1.read(3)
print(str)
print(f1.tell())
print(f.closed)

"""
file.closed- Returns true if file is closed, false otherwise.
file.mode- Returns access mode with which file was opened.
file.name- Returns name of the file.
ile.softspace- Returns false if space explicitly required with print, true otherwise

os functions (after importing os)
os.rename(current_file_name, new_file_name) to rename the file1
os.remove(file_name) to delete a file
"""
