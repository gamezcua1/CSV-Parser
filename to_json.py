import json

def to_JSON(file):
    file.seek(0, 0)

    file_name = file.name
    headers = file.readline()
    records = file.readlines()
    
    field_type = []
    super_json = { "fields": [], "records": [] }

    for record in records:
        super_json["records"].append(record.replace('\n', '').split(','))

    for field in super_json["records"][1]:
        if field.isalnum() == True:
            field_type.append("integer")
        else:
            field_type.append("varchar")
    
    i = 0
    for head in headers.replace('\n','').split(','):
        super_json["fields"].append( { "name": head, "type": field_type[i] })
        i = i + 1
    
    with open(file_name.replace('csv', 'json'), 'w') as fp:
        json.dump(super_json, fp)
    
    print("CSV to JSON complate")