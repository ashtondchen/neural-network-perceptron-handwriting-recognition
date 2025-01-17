import util
from Tkinter import *
import tkFont
MAX_ITERATIONS=5

class PerceptronClassifier:
  """
  Perceptron classifier.
  """
  def __init__( self, legalLabels):
    self.legalLabels = legalLabels
    self.type = "perceptron"
    self.weights = {}
    for label in legalLabels:
      self.weights[label] = util.Counter()
      
  def train( self, trainingData, trainingLabels, canvas):
    """
    The training loop for the perceptron passes through the training data several
    times and updates the weight vector for each label based on classification errors.
    See the project description for details.
    """
    for iteration in range(MAX_ITERATIONS):
      print "Starting iteration " + str(iteration) + "..."
      guess = []
      for i in range(len(trainingData)): # there are 100 data in each training set
        vectors = util.Counter()
        for l in self.legalLabels: # test with 10 legal labels
          #print l
          #print self.weights[l]
          vectors[l] = self.weights[l] * trainingData[i]
          
          
        if vectors.argMax() != trainingLabels[i]:
         # print vectors.argMax(), ' vs  ', trainingLabels[i]
          #print self.weights
          self.weights[vectors.argMax()] -= trainingData[i]
          self.weights[trainingLabels[i]] += trainingData[i]
          #print "leagal labels", self.legalLabels

  def classify(self, data, canvas):
    """
    Classifies each datum as the label that most closely matches the prototype vector
    for that label.  See the project description for details.
    """
    guesses = []
    for datum in data:
      vectors = util.Counter()
      for l in self.legalLabels:
        vectors[l] = self.weights[l] * datum
        #print vectors[l]
      guesses.append(vectors.argMax())
      canvas.create_text(400,400, text= "Gessed Digit", anchor=NW, font=tkFont.Font(size=-14))
      canvas.create_text(415,415, text= str(vectors.argMax()), anchor=NW, font=tkFont.Font(size=-14))
     # print vectors.argMax(), ' vs  ', datum
                
    return guesses
