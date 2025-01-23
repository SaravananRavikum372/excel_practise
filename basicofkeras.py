#keras basic
#adding layer
#model.add(Dense(12,input_dim=8,activation='relu'))  (Dense(hiddenlayer,inputlayer,activation='relu')
#model.add(Dense(8,activation='relu')) (Dense(hiddenlayer2,activation='relu'))
#compile model
#model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy']) using sigmoid means use binary_crossentropy
#and using softmax use catorical_crossentropy
#keras basic syntax
#save and load model
#save
#model_json=model.to_json()withopen("model.json","w")as json_file w means write it means save the json file
#model.save_weights("model.h5")
#load
#json_file=open('model.json","r") r means read the file like load the file
#loaded_model_json=json_file.read() and json_file.close()
