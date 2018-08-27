import json

def to_JSON(filename):
    # sets the file position at the beginning
    file = open(filename)

    file.seek(0, 0)

    # get csv lines
    file_name = file.name
    headers = file.readline()
    records = file.readlines()
    
    # make the dictionary
    field_type = []
    super_json = { "fields": [], "records": [] }

    # split and validate the records
    for record in records:
        super_json["records"].append(record.replace('\n', '').split(','))

    # check the type of field
    for field in super_json["records"][1]:
        if field.isalnum() == True:
            field_type.append("integer")
        else:
            field_type.append("varchar")
    
    # merge the headers and the records into the dictionary
    i = 0
    for head in headers.replace('\n','').split(','):
        super_json["fields"].append( { "name": head, "type": field_type[i] })
        i += 1

    # conver the string to number
    i = 0
    for record in super_json["records"]:
        x = 0
        for field in record:
            if field_type[x] == 'integer':
                super_json['records'][i][x] = int(field)
            elif field_type[x] == 'decimal':
                super_json['records'][i][x] = float(field)
            x += 1
        i += 1

    # create the json file (we need this because we have export the file with doublequotes)
    with open(file_name.replace('csv', 'json'), 'w') as fp:
        json.dump(super_json, fp)
    
    print("CSV to JSON complate")