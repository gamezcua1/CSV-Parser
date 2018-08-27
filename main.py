import sys
from to_xml import to_XML
from to_json import to_JSON

if __name__ == '__main__':
  if len( sys.argv ) == 1 :
    fileName = input("File Name location: ")
    to_XML(fileName)
    to_JSON(fileName)
  
  else:
    to_XML(sys.argv[1])
    to_JSON(sys.argv[1])
