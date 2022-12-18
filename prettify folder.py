# The function will perform three tasks:
#
# First, it will check all the files present in the folder whose paths are given as an input argument.
# Then it will capitalize the first letter of each file. If the file’s name is present in a dictionary file, then it will not capitalize the first letter. It will only capitalize the first letter of the files, which are not present in the dictionary file.
# The function renames the file names to numbers in the range of 1 to100 whose format is the same as mentioned in the input parameter like 1.jpg.
# After performing these tasks, your folder will prettify as all the first letters of the files will be capitalized except for those whose names are present in the dictionary file. And the files having the same format as given in the input argument will rename to number in the range of 1-100.
import os
def soldier(path,file,format):
    os.chdir(path)
    i=1
    files=os.listdir(path)
    with open(files) as f:
        filelist=f.read().split("\n")
    for file in files:
        if file not in filelist:
            os.rename(file,file.capitalize())
        if os.path.splitext(file)[1]== format:
            os.rename(file,f"{i}.{format}")
            i+=1
if __name__ == '__main__':
    ch=input("Enter the path of file you want to rename:")
    p=input("Enter the path of the file you want to... ")
    pn=input("Enter the format of the file to numbering:")
    soldier(r"ch",r"p",pn)