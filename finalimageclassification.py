from keras.models import model_from_json
import numpy as np
from keras.preprocessing import image
import os

# First, import the trained model using json
json_file = open('trainingdata.json', "r")
loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)
model.load_weights('best_model.h5')

# Next, get testing data in the system using os library
path = 'C:/Users/Saravanan R/Desktop/pythonwork/images/testdata'

files = []  # an empty list is used for adding or removing values

for root, dirs, filenames in os.walk(path):
    for file in filenames:
        if '.jpeg' in file:
            file_path = os.path.join(root, file)
            files.append(file_path)
            #print(files)
#initialzing the empty dictionary for storing the value before the loop            
checking_prediction={}
label1='joker'
label2='badman'
def testing_function(img_file,threshold=0.5):
    img_container = img_file
    test_image = image.load_img(img_container, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)
   # print(result)

    binary_change=np.where(result>=threshold ,1,0)
    if binary_change==1:
       checking_prediction[img_file]=binary_change
    else:
       checking_prediction[img_file]=binary_change
for file_path in files:
    testing_function(file_path)

print("the result of checking prediction dictionary:")
print(checking_prediction)
