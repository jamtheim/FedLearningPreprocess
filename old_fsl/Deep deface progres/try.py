
import keras 
#Try loading the model into another variable then call the model.summary() function

model_2 = keras.models.load_model('./model.hdf5')
model_2.summary()
