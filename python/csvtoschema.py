import sys, json, re

schema_dict ={}
schema_fields = []
date_fields = []
date_fields.append('([1-2]{1}[0-9]{3})([-]?)([0-9]{2}([-]?)[0-9]{2})T[0-9]{2}([:]?)([0-9]{2})([:]?)([0-9]{2})(([.]?)([0-9]{3}))?(Z|([\+]([0-9]{2}):([0-9]{2})))')
date_fields.append('([0-9]{2}|[1-9])/([0-9]{2}|[1-9])/[0-9]{4}')
date_fields.append('([0-9]{2}|[1-9])/([0-9]{2}|[1-9])')
date_fields.append('([0-9]{2}|[1-9])-([0-9]{2}|[1-9])-[0-9]{4}')
date_fields.append('([0-9]{2}|[1-9])-([0-9]{2}|[1-9])')
date_fields.append('([0-9]{2}|[1-9]).([0-9]{2}|[1-9]).[0-9]{4}')
date_fields.append('([0-9]{2}|[1-9]).([0-9]{2}|[1-9])')
date_fields.append('(January|February|March|April|May|June|July|August|September|October|November|December) (([0-3][0-9])|[1-9]) [1-2][0-9]{3}')
date_fields.append('(January|February|March|April|May|June|July|August|September|October|November|December) (([0-3][0-9])|[1-9]), [1-2][0-9]{3}')
date_fields.append('(January|February|March|April|May|June|July|August|September|October|November|December) (([0-3][0-9])|[1-9])')
date_fields.append('(([0-3][0-9])|[1-9]) (January|February|March|April|May|June|July|August|September|October|November|December) [1-2][0-9]{3}')
date_fields.append('(([0-3][0-9])|[1-9]) (January|February|March|April|May|June|July|August|September|October|November|December), [1-2][0-9]{3}')
date_fields.append('(([0-3][0-9])|[1-9]) (January|February|March|April|May|June|July|August|September|October|November|December)')
date_fields.append('(([0-3][0-9])|[1-9]) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)( [1-2][0-9]{3})')
date_fields.append('(([0-3][0-9])|[1-9]) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(, [1-2][0-9]{3})')
date_fields.append('(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (([0-3][0-9])|[1-9])( [1-2][0-9]{3})')
date_fields.append('(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (([0-3][0-9])|[1-9])(, [1-2][0-9]{3})')
date_fields.append('(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (([0-3][0-9])|[1-9])')
date_fields.append('(Jan.|Feb.|Mar.|Apr.|May|Jun.|Jul.|Aug.|Sep.|Oct.|Nov.|Dec.) (([0-3][0-9])|[1-9])( [1-2][0-9]{3})')
date_fields.append('(Jan.|Feb.|Mar.|Apr.|May|Jun.|Jul.|Aug.|Sep.|Oct.|Nov.|Dec.) (([0-3][0-9])|[1-9])(, [1-2][0-9]{3})')
date_fields.append('(Jan.|Feb.|Mar.|Apr.|May|Jun.|Jul.|Aug.|Sep.|Oct.|Nov.|Dec.) (([0-3][0-9])|[1-9])')
email_re = '[\w-]+@[\w-]+(.[\w-]+)+'
def findtype(input):
    typereturn = "string"
    integer = re.compile('[-]?[1-9]+[0-9]*')
    float = re.compile('[-]?[1-9]+[0-9]*.[0-9]*')
    integercheck = integer.match(input)
    floatcheck = float.match(input)
    email = re.compile(email_re)
    emailcheck = email.match(input)
    if integercheck!= None and integercheck.group() == input:
        typereturn = "integer"
    elif floatcheck != None and floatcheck.group() == input:
        typereturn = "number"
    else:
        if emailcheck != None and emailcheck.group() == input:
            field_dict["format"] = "email"
        for element in date_fields:
            date_re = re.compile(element)
            datecheck = date_re.match(input)
            if datecheck != None and datecheck.group() == input:
                if element == '([1-2]{1}[0-9]{3})[-]([0-9]{2}-[0-9]{2})T[0-9]{2}:([0-9]{2})[.]([0-9]{3})Z':
                    field_dict["format"] = "date-time"
                field_dict["pattern"] = element
    return typereturn
csvfile = open(sys.argv[1])
headerlist = csvfile.readline().split(',')
line = csvfile.readline()
lineElements = line.split(',')
count = 0

for element in headerlist:
    field_dict = {}
    field_dict["type"] = findtype(lineElements[count].strip())
    field_dict["name"] = element.strip()
    field_dict["title"] = element.strip()
    schema_fields.append(field_dict)
    count += 1
csvfile.close()
schema_dict["fields"] = schema_fields
valid_json = json.dumps(schema_dict)
sys.stdout.write(valid_json)

#TODO Validate with JSON output using schemavalidator
#TODO Check with multiple lines (return string if it fits 2 or more, remove patterns and formats)
#TODO Other delimiters (, TAB, |)
#TODO Inspection row input (1-rows in file)
#TODO Place under service sub-application

