import os
directory = "D:\dataset"
file_name = "micle"
# Joining path components to create a file path
file_path = os.path.join(directory, file_name) #os.path.join() this function create just path not create folder(directory)
#it means just join the into the exiting path not create directory(folder)
print("File Path:", file_path)
#os.mkdir() it means makedirectory it will create the folder in specified path in the arugument
#os.isdir() it will check any dir(folder) inthe mention specifiy path
#os.mkdir(file_path)
filelst=os.listdir(file_path)
print("filelst",filelst)

