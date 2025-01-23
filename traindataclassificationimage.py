#image classification using cnn convolutional neural network
#image classification using binary classification is means true or false like 0or1
#first training the data
#from pygoogle_image import image as pi

#pi.download("badmanimage",limit=20)     # downloading image directly from google through this code

from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import plot_model as pm
from keras.callbacks import TensorBoard, ModelCheckpoint # for visualing the backend working process during the training of cnn

model=Sequential()
model.add(Conv2D(32,  (3,3) , input_shape=(64,64,3),activation='relu'))#3 is an rgb color
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(units=128,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])
#print the model summary before training
print("model_summary:")
print(model.summary())
#print the model visualation and save the model archecture

#pm(model,to_file='model_architecture.png', show_shapes=True, show_layer_names=True)
#using tensorBoard for visualing the backend process of working in a cnn of deep learning of my model

tensorboard_callback=TensorBoard(log_dir='C:/Users/Saravanan R/Desktop/pythonwork./logs', histogram_freq=1, write_graph=True,write_images=True)
# tensorboard --logdir='C:/Users/Saravanan R/Desktop/pythonwork./logs'  is an example of visualing the backend 
modelcheckpoint_call=ModelCheckpoint(filepath='best_model.h5', monitor='val_accuracy', save_best_only=True)
# the above using two callback function for some purpose
train_datagen=ImageDataGenerator(rescale=1./255,zoom_range=0.2,shear_range=0.2,horizontal_flip=True) #shearrange=angleprecription

val_datagen=ImageDataGenerator(rescale=1./255)

training_dataset=train_datagen.flow_from_directory('images/traindata',target_size=(64,64), batch_size=10,class_mode='binary')

validation_dataset=val_datagen.flow_from_directory('images/validationdata',target_size=(64,64),batch_size=10,class_mode='binary')

#training the data finally on next step

model.fit(training_dataset, steps_per_epoch=10,epochs=60,validation_data=validation_dataset,validation_steps=2 ,callbacks=[tensorboard_callback, modelcheckpoint_call] ) 

model_json=model.to_json()
with open('trainingdata.json',"w") as json_file:
       json_file.write(model_json)

#model.save_weights('best_model.h5')
























3

