import sys
from xml import toXML

if __name__ == '__main__':
  if len( sys.argv ) == 1 :
    fileName = input("File Name location: ")
    file = open(fileName)
  
  else:
    file = open(sys.argv[1])
    toXML( file )
