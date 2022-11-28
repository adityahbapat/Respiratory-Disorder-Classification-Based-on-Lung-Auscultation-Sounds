import os
import tensorflow
from tensorflow import keras
import numpy as np 
from tensorflow.keras.models import load_model
import librosa as lb

# load model
model = load_model('model/model.h5')

def getFeaturesForNeuralNetwork(path):
    soundArr,sample_rate=lb.load(path)
    mfcc=lb.feature.mfcc(y=soundArr,sr=sample_rate)
    cstft=lb.feature.chroma_stft(y=soundArr,sr=sample_rate)
    mSpec=lb.feature.melspectrogram(y=soundArr,sr=sample_rate)

    return mfcc,cstft,mSpec

def classificationResults(soundFilePath):
    print(soundFilePath)
    isExist = os.path.exists(soundFilePath)
    if(isExist):
        mfcc_test, croma_test, mspec_test = getFeaturesForNeuralNetwork(soundFilePath)
        mfcc,cstft,mSpec = [],[],[]
        mfcc.append(mfcc_test)
        cstft.append(croma_test)
        mSpec.append(mspec_test)

        mfcc_test = np.array(mfcc)
        cstft_test = np.array(cstft)
        mspec_test = np.array(mSpec)

        result = model.predict({"mfcc":mfcc_test,"croma":cstft_test,"mspec":mspec_test})

        diseaseArray = ['Asthma', 'Bronchiectasis', 'Bronchiolitis', 'COPD', 'Healthy', 'LRTI', 'Pneumonia', 'URTI']
        result = result.flatten()
        indexMax = np.argmax(result)
        indexSecMax = 0
        secMax = result[0]
        for smx in range(len(result)):
            if(result[smx] > secMax and result[smx] < result[indexMax]):
                indexSecMax = smx
                secMax = result[smx]
        res1 = "respiratory disorder detected: " + str(diseaseArray[indexMax]) + " with probability " + str(result[indexMax] * 100) + "%"
        res2 = "respiratory disorder detected: " + str(diseaseArray[indexSecMax]) + " with probability " + str(result[indexSecMax] * 100) + "%"
        res_list = []
        res_list.append(res1)
        res_list.append(res2)
        return res_list
    else:
        err1 = "Sorry, No File Found"
        err2 = "Please upload the file in .wav format"
        res_list.append(err1)
        res_list.append(err2)
        return res_list
