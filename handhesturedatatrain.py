from PIL import Image
import os, shutil

input_path = "D:/datacollection/images/traindata"
output_path = "D:/datacollection/images/newtraindata"

def rename_files(input_path):
    input_files = os.listdir(input_path)
    i = 1
    for folder in input_files:
        files_path = os.path.join(input_path, folder)
        current_src = os.listdir(files_path)

        for src in current_src:
            src_path = os.path.join(files_path, src)

            if f"fivefingerhand_{(i)}.jpeg" or f"fivefingerhand_{(i)}.png" in src_path:
                dst1 = 'fivefingerimg' + str(i) + '.jpeg'
                dst_1=os.path.join(files_path,dst1)
                os.rename(src_path, dst_1)
            elif f"fourfingerhand_{(i)}.jpeg" or f"fourfingerhand_{(i)}.png" in src_path:
                dst2 = 'fourfingerimg' + str(i) + '.jpeg'
                dst_2=os.path.join(files_path,dst2)
                os.rename(src_path, dst_2)
            elif f"onefingerhand_{(i)}.jpeg" or f"onefingerhand_{(i)}.png" in src_path:
                dst3 = 'onefingerimg' + str(i) + '.jpeg'
                dst_3=os.path.join(files_path,dst3)
                os.rename(src_path, dst_3)
            elif f"threefingerhand_{(i)}.jpeg" or f"threefingerhand_{(i)}.png" in src_path:
                dst4 = 'threefingerimg' + str(i) + '.jpeg'
                dst_4=os.path.join(files_path,dst4)
                os.rename(src_path, dst_4)
            elif f"twofingerhand_{(i)}.jpeg" or f"twofingerhand_{(i)}.png" in src_path:
                dst5 = 'twofingerimg' + str(i) + '.jpeg'
                dst_5=os.path.join(files_path,dst5)
                os.rename(src_path, dst_5)
            else:
                print(f"No matching pattern for {src}")

            i += 1

rename_files(input_path)
