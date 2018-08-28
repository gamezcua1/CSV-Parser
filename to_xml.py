import csv


def to_XML( filename ):
  """
    Params -> string with the file name
  """

  # Open the CSV file
  pureFile = open(filename, newline='\n')
  file = csv.reader(pureFile , delimiter=',')

  # print(next(file))

  # Get the name of the file and at the same time the xml wraper
  fileName = filename.split('.')[0]

  # Create the new file .xml
  newFile = open( fileName + '.xml', 'w')

  #Get the fields that the xml will have
  fields = next(file)

  #Write the xml top
  newFile.write('<?xml version="1.0"?>\n')

  #We open the xml tag
  newFile.write(f'<{fileName}>\n')

  ##### Generate table #####

  for rows in file:
    # We get every field of the record and get rid of the \n
    
    # We open a new row
    newFile.write("\t<row>\n")
  
    # Put every field on the row
    for i in range( len(rows) ):
      newFile.write( f"\t\t<{fields[i]}>{rows[i]}</{fields[i]}>\n")
    
    # Close the row
    newFile.write("\t</row>\n")

  # Close the xml and file
  newFile.write(f'</{fileName}>') ; pureFile.close()


  print("XML generated correctly")
  print( f"XML file name : {fileName}.xml ")