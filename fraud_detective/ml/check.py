import pickle
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np

text = ['Virat Kohli, AB de Villiers set to auction their \'Green Day\' kits from 2016 IPL match to raise funds']
model = pickle.load(open("fraud_detective/model.pkl", "rb"))
#prediction_model = model.predict(text)
#if np.any(prediction_model):
 #   prediction_model = "not-scam"
  #  print('The message: {} is {}'.format(text, prediction_model))
#print('bb')
print(model.predict(text))