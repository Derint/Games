import json, sys

def saveDict(dictionary, filename):
    with open(filename, "w") as fOut:
        json.dump(dictionary, fOut)
    print("  [+]  Data Saved Successfully....")
        
def openJsonFile(filename):
    with open(filename, "r") as fIn:
        return json.load(fIn)
    
def process_data(data):
    data = data.lower().strip().split(",") 
    data = list(filter(lambda x: x!='', data)) # filtering blank spaces
    return list(set([i.strip() for i in data]))



FILENAME = "HangManData.json"
categories = openJsonFile(FILENAME)

print("\n\n","Adding New Data".center(50), end='\n\n')
print('    Select the Category you want to insert data')
dict_keys = list(categories.keys()) + ['Another Category']
for i, key in enumerate(dict_keys):
    print(f"\t{i+1}. {key.capitalize()}")

uc = input("\n   Select  >> ")

try:
    uc = int(uc) - 1
    
    if uc==(len(dict_keys)-1):
        ctg = input("  >> Enter New Category Name: ").strip()
        if ctg in dict_keys:
            print(f"  {ctg} already exists....")
            
    elif not (0 <= uc < len(dict_keys)) :
        print(" !!! Invalid Category Selected....")
        sys.exit()

    ctg = ctg if uc==(len(dict_keys)-1) else dict_keys[uc]

    print(f"\n\n  INFO: You have selected category {ctg.capitalize()}")
    print('  NOTE: Enter data by adding comma(,) between the words\n')

    data = process_data(input("  DATA(words) >> "))
    tmpLen = len(categories[ctg])
    categories[ctg] = list(set(categories[ctg] + data))

    if tmpLen==len(categories[ctg]) and data:
        print("  NOTE: The Provided Data is already present in the database...")
    elif len(data):
        saveDict(categories, FILENAME)
    else:
        print("  NOTE: !! NO DATA WERE INSERTED....")
except Exception as e:
    print("EXCEPTION OCCURED: ", e)
