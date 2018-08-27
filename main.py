import sys
from xml import toXML
from csv_checker import csv_checker

if __name__ == '__main__':
  if len( sys.argv ) == 1 :
    fileName = input("File Name location: ")
    file = open(fileName)
    toXML( file )
  
  else:
    csv_checker(sys.argv[1])
    #toXML(sys.argv[1])
    
