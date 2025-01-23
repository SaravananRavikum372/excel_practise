#from pygoogle_image import image as pi

#pi.download("fivefingerhand", limit=500)
'''
print("before:", os.getcwd())# this function execute current working directory file path root

os.chdir("D:/Program Files/python2")  # this function change the current working directory location path and checking using getcwd function 

print("after:", os.getcwd())

os.chdir("C:/Users/Saravanan R/Desktop/pythonwork")

print("finalafter:", os.getcwd())
'''
import os
import shutil as sh
'''
def move_images_to_traindata(source_path, destination_path):
    if os.path.exists(source_path):
        print("the path already exist")
        if os.path.isdir(source_path):
            print("the path is an directory")
            s_path=os.listdir(source_path)
            for files in s_path:
                print("files:",files)
                source_path_files=os.path.join(source_path,files)
                destination_path_files= os.path.join(destination_path,files)
                print("source_path_files:",source_path_files)
                print("destination_path_files:",destination_path_files)
                sh.move(source_path_files,destination_path_files)
        else:
                print("the path is not directory")
    else:
            print("the path does not exist")
 '''     
#train data transmission one dir to another dir
source_path = "C:/Users/Saravanan R/Desktop/pythonwork/images/traindata" #traindata
destination_path = "D:/datacollection/images/traindata"#traindata
#move_images_to_traindata(source_path, destination_path)


#validation data transmission one dir to another dir
destination_val="D:/datacollection/images"
source_val="C:/Users/Saravanan R/Desktop/pythonwork/images/validationdata"
new_destination_val=os.path.join(destination_val,"validationdata")
print("new_destination_val:",new_destination_val)
'''
if os.path.isdir(new_destination_val):  # it consist of folder in the path means is indicate true and does not consists of folder in the path means it will indicate false
    print("the path is an directory")
else:
       os.mkdir(new_destination_val)
'''       
'''     
def validation_data_changedir(source_val, new_destination_val):
    if os.path.exists(source_val):
        print("the path already exist")
        if os.path.isdir(source_val):
            print("the path is an directory")
            s_val_list= os.listdir(source_val)
            for files in s_val_list:
               print("files:",files)
               source_new=os.path.join(source_val,files)
               print("source_new:",source_new)
               destination_new=os.path.join(new_destination_val,files)
               print("destination_new:",destination_new)
               sh.move(source_new,destination_new)
 '''              
#validation_data_changedir(source_val,new_destination_val)
  
#next move all files into the testdata is move on to another dir
source_testdata="C:/Users/Saravanan R/Desktop/pythonwork/images/testdata"
destination_testdata="D:/datacollection/images/testdata"

def move_testdata_operation(source_testdata,destination_testdata):
    t_source=os.listdir(source_testdata)
    for files in t_source:
        #print("files:",files)
       sh.move(source_testdata,destination_testdata)   
move_testdata_operation(source_testdata,destination_testdata)        






  
