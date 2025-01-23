from numpy import loadtxt # it is used for load dataset in the program in loadtxt is function
from keras.models import Sequential  # it is used for arrange the data in order into the model Sequential() is function
from keras.layers import Dense  #it will used for adding model data into the layer Dense() is function
from keras.models import model_from_json #it is used for save the data into the json format

# Load the dataset from a CSV file (adjust the filename accordingly)
dataset = loadtxt('diabetes.csv', delimiter=',', skiprows=1)  # Assuming the header is present
#print(dataset)
# Split the data into input features and target variable
x = dataset[:, 0:8]  # input [rows, columns]
y = dataset[:, 8]    # output

print("Input:")
#print(x)
print("Output:")
#print(y)
#adding layers  like 0 means negative value is convert into positive value is 0 and 1 is output in this operation would activation =relu
'''Sequential is a class that represents a linear stack of layers.
It is a way to build a neural network model layer by layer in a step-by-step fashion.
The Sequential model is a plain stack of layers where each layer has exactly one input tensor and one output tensor.'''

model=Sequential()
'''
model = Sequential(): Initializes an empty Sequential model.
model.add(...): Adds layers to the model. In this case,
we added three layers – an input layer, a hidden layer, and
an output layer – using the Dense layer, which is a fully connected layer
'''
model.add(Dense(12,input_dim=8,activation='relu'))#dense is used to add layer 12 is hiddenlayer activation is used for that value relu is negative value means is convert positive and positive return
model.add(Dense(8,activation='relu'))# in 8 is also hidden layer2
model.add(Dense(1,activation='sigmoid'))# i will give one is an output layer and i will get the output is binary so use sigmoid

#modelcompile
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy']) # i will used sigmoid for output so use binary_crossentopy

#model training

model.fit(x, y,epochs=35,batch_size=10)# fit() is used for training and epochs is used for how much time will give training in hiddenlayer
# and batch_size is send the data like 10 and 10 vice x,y input and output

#modelevaluation
_, accuracy=model.evaluate(x,y)
print(f"accuracy of value {accuracy*100}")
#next save the model into json
model_json=model.to_json()# to_json() will convert model into the json format and next store variable
with open("model.json","w") as json_file:#with keyword statement of block is used to ensure the file is closed"model.json"is saving name
       json_file.write(model_json)
model.save_weights("model.h5")# this save_weights() save the weights means trained model in the neural network 
print("saved model to disk")
    


