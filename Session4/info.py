person = {
    "NAME": "Ly", 
    "YOB": 2002, 
    "JOB": "Student",
    "BMI": {
        "Weight": 44,
        "Height": 155
    }
    }
#key_value
print("name" in person) #CHECK KEY IN DICTIONARY
person["Hair"] = "short" #CREATE
person["BMI"]["Weight"] = 75 #UPDATE
name = person["NAME"] #READ
bmi = person["BMI"]
print(bmi["Weight"])
for key in person:
    print(key, person[key])

del person["BMI"] #DELETE
print(key, person[key])
