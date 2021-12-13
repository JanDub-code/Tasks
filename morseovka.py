MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}

def get_n():
    print("chcete šifrovat nebo dešifrovat ?")
    n = input("")
    return n
n = get_n()

key = MORSE_CODE_DICT.keys
value = MORSE_CODE_DICT.values

if n == "šifrovat":
    print("zadejte text pro zašifrování")
    k = input("")
    šifra = ""
    for letter in k:
        šifra += MORSE_CODE_DICT[letter]
    print(šifra)
        
elif n == "dešifrovat":
    print("zdejte morseovku pro dešifrování")
    k = input("")
    def morsetxt():
        code = [k for i in k.split() for k,v in MORSE_CODE_DICT.items() if i==v]
        newtxt = ''.join(code)
        print(newtxt)
    print(morsetxt())
    
else:
    print("Špatný input")
    
    