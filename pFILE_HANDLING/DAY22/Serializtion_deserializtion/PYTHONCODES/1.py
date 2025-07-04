
import json

def encode_special(obj):
    if isinstance(obj, tuple):
        return {"type":"tuple","items":[encode_special(i) for i in obj]}
    elif isinstance(obj, set):
        return {"type":"set","items":[encode_special(i) for i in obj]}
    elif isinstance(obj, list):
        return [encode_special(i) for i in obj]
    elif isinstance(obj,dict):
        return {k:encode_special(i) for k,i in obj.items()}
    else:return obj

mydata = {
    "tuple1": ("arun", 18, "CSE"),
    "tuple2": (2, 3, 4, 5, 6, 7, 8, 9),
    "set1": {"arun", 18, "CSE"},
    "set2": {"PYTHON", "AI"}
}


encodedformat=encode_special(mydata)
print(mydata)
print(encodedformat)

# Save
with open("mydata.json", "w") as f:
    json.dump(encodedformat, f,indent=1)





#DECODING THE DATABACK
def decoding(obj):
    if isinstance(obj,dict):
        if "type" in obj and "items" in obj:
            if obj["type"]=="tuple":
                return tuple(decoding(i) for i in obj["items"])
            elif obj["type"]=="set":
                return set(decoding(i) for i in obj["items"])
            else:
                return obj
        else:
            return {k:decoding(i) for k,i in obj.items()}
    elif isinstance(obj,list):
           return [decoding(i) for i in obj]
    else:return obj

#DECODING OUTSIDE
with open("mydata.json", "r") as f:
    data=json.load(f)

decoded_data=decoding(data)
print("\nDecoded",decoded_data)


#DECODING INSIDE THE LOAD
#object_hook=decoding tells json.load to call your decoding function on every dict it loads.
#Use json.load(f, object_hook=decoding) to decode as you load from the file.
#ONLY USEFUL WHEN YOU KNOW THAT DATA IS IN FORMAT DICTIONARY ,NOT WORK ON LISTS ,STRINGETC.
with open("mydata.json", "r") as f:
    newdata=json.load(f,object_hook=decoding)

print("\n\n",newdata)