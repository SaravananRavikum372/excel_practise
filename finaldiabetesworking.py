from numpy import loadtxt
from keras.models import model_from_json
import numpy as np
#again load dataset into the variable

threshold=0.5  #0.5 is default threshold for common all any prediction value increase in that 0.5 means is 1 and otherwise 0

dataset=loadtxt('diabetes.csv', delimiter=',' , skiprows=1)

#next split dataset into input and output
x=dataset[:,0:8] #input
y=dataset[:,8] #output

# next load the predrained json file

json_file=open('model.json',"r")
load_model=json_file.read()
model=model_from_json(load_model)
model.load_weights("model.h5")   #The ".h5" extension is commonly used for HDF5 file format, which is a file format commonly used for storing large amounts of numerical data.
print("loaded model from disk")

predictions=model.predict(x)# predict is an it will give result of the output
#tolist() function is used to convert array or matrix as list
#prediction
#print("predictions:",predictions)
binary_prediction=np.where(predictions>=threshold ,1,0)    #1is true and 0 is false in this condition is satisfyed 
for i in range(5,15):
    print(f"the input is {x[i].tolist()} and the prediction {predictions[i]} in output is{binary_prediction[i]} and expected output is{y[i]}")
   # print(f"the input is {x[i].tolist}in the predictions{predictions[0][0]} expected output is{y[i]}")
