
import util
from Tkinter import *
import tkFont
## Constants
DATUM_WIDTH = 0 # in pixels
DATUM_HEIGHT = 0 # in pixels

## Module Classes

class Datum:

  def __init__(self, data,width,height):
    """
    Create a new datum from file input (standard MNIST encoding).
    """
    DATUM_HEIGHT = height
    DATUM_WIDTH=width
    self.height = DATUM_HEIGHT
    self.width = DATUM_WIDTH
    if data == None:
      data = [[' ' for i in range(DATUM_WIDTH)] for j in range(DATUM_HEIGHT)] 
    self.pixels = util.arrayInvert(convertToInteger(data)) 
  def getPixel(self, column, row):
    """
    Returns the value of the pixel at column, row as 0, or 1.
    """
   # print "column ", column 
   # print "row ", row
    return self.pixels[column][row]
      
  def getPixels(self):
    """
    Returns all pixels as a list of lists.
    """
    return self.pixels    
      
  def getAsciiString(self):
    """
    Renders the data item as an ascii image.
    """
    rows = []
    data = util.arrayInvert(self.pixels)
    for row in data:
      ascii = map(asciiGrayscaleConversionFunction, row)
      rows.append( "".join(ascii) )
    return "\n".join(rows)
    
  def __str__(self):
    return self.getAsciiString()
    


  
# Data processing, cleanup and display functions
    
def loadDataFile(filename,n,width,height,tye,canvas):
  """
  Reads n data images from a file and returns a list of Datum objects.
  """
  DATUM_WIDTH=width
  DATUM_HEIGHT=height
  fin = open(filename)
  items = []
  ok = []
  for i in range(n):
    data = []
    count = 100
    for j in range(height):
      temp = fin.readline()
      print "line"
      print temp
      if tye == "test":
        canvas.create_text(500,count, text= temp, anchor=NW, font=tkFont.Font(size=-14))
        count += 15
     # print list(temp)

      data.append(list(temp)[:-1])
    print "load Image"
    print data
    items.append(Datum(data,DATUM_WIDTH,DATUM_HEIGHT))
  fin.close()

  return items
  #return map(basicFeatureExtractorDigit,item)

def loadLabelsFile(filename, n):
  """
  Reads n labels from a file and returns a list of integers.
  """
  fin = open(filename)
  labels = []
  for i in range(n):
    labels.append(int(fin.readline()[0]))
  fin.close()
  return labels
  
def asciiGrayscaleConversionFunction(value):
  """
  Helper function for display purposes.
  """
  if(value == 0):
    return ' '
  elif(value == 1):
    return '+'
  elif(value == 2):
    return '#'    
    
def IntegerConversionFunction(character):
  """
  Helper function for file reading.
  """
  if(character == ' '):
    return 0
  elif(character == '+'):
    return 1
  elif(character == '#'):
    return 2    

def convertToInteger(data):
  """
  Helper function for file reading.
  """
  if type(data) != type([]):
    return IntegerConversionFunction(data)
  else:
    return map(convertToInteger, data)

# Testing


def _test():
  import doctest
  doctest.testmod() # Test the interactive sessions in function comments
  n = 1
#  items = loadDataFile("../facedata/facedatatrain", n,60,70)
#  labels = loadLabelsFile("../facedata/facedatatrainlabels", n)
  items = loadDataFile("../digitdata/trainingimages", n,28,28,'')
  labels = loadLabelsFile("../digitdata/traininglabels", n)
  for i in range(1):
    print 'cp1'
    print items[i]
    print 'cp2'
    print items[i]
    print (items[i].height)
    print (items[i].width)
    print dir(items[i])
    print items[i].getPixels()

if __name__ == "__main__":
  _test()  
