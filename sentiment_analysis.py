import pickle
import sklearn

with open('text_classifier', 'rb') as training_model:
    model = pickle.load(training_model)

def predict(s):
  s = s.replace('[^A-Za-z0-9\s]+', '')
  s = s.replace('http\S+|www.\S+', '', case=False)
  s = s.lower()
  print(best.predict([s]))

while 1:
  s = input('Insert text ')
  predict(s)
