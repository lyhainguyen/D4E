teencode = {
    "hc": "hoc",
    "ng": "nguoi",
    "stt": "so thu tu",
    "lm": "lam",
    "trg": "truong",
    "vs": "voi"
}

def print_teencode():
    for key in teencode:   
        print(key, end = "\t")
    print()
    
while True:    
    print_teencode()
    yourcode = input('Enter your code: ')
    if yourcode in teencode:
        print('Translation: ', teencode[yourcode])
    else:
        contribute = input('Not found, do you want to contribute your word? (Y/N) ').upper()
        if contribute == "Y":
            teencode[yourcode] = input('Enter translation for your new word: ')
        else:
            print("Bye")
            break

