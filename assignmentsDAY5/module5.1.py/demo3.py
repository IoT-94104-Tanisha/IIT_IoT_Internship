import os

print("Current Directory:", os.getcwd()) #to get current working directory

os.mkdir("firstDirectory") #to create a new directory
print("directory Created")

print("Files in current directory:") #to list files and folders
print(os.listdir())

os.rename("firstDirectory", "MyDirectory") #to rename directory
print("directory renamed")

os.rmdir("MyDirectory") #to remove directory
print("Directory Removed")
