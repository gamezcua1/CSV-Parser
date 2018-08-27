def toXML( filename ):
  """
    Params -> string with the file name
  """

  # Open the CSV file
  file = open(filename)

  # Get the name of the file and at the same time the xml wraper
  fileName = file.name.split('.')[0]

  # Create the new file .xml
  newFile = open( fileName + '.xml', 'w')

  #Get the fields that the xml will have
  fields = file.readline().replace('\n','').split(',')

  #Write the xml top
  newFile.write('<?xml version="1.0"?>\n')

  #We open the xml tag
  newFile.write(f'<{fileName}>\n')

  ##### Generate table #####

  # read the first line
  line = file.readline()

  # While there are no more lines
  while line != "" and line != None:
    
    # We get every field of the record and get rid of the \n
    rows = line.replace('\n', '').split(',')

    # We open a new row
    newFile.write("\t<row>\n")
    
    # Put every field on the row
    for i in range( len(rows) ):
      newFile.write( f"\t\t<{fields[i]}>{rows[i]}</{fields[i]}>\n")
    
    # Close the row
    newFile.write("\t</row>\n")

    # Read the next line
    line = file.readline()

  # Close the xml and file
  newFile.write(f'</{fileName}>') ; file.close()


  print("XML generated correctly")
  print( f"XML file name : {fileName}.xml ")

