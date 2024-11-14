rawstr =  2
try:
    ival = int(rawstr)
except:
    ival = -1
    
if ival > 0:
    print("Nice Work!")
else:
    print("Not a number")


big = max("Hello world")
print(big)


x = 5
print("Hello")
def print_lyrics():
    print("I am a lumberjack, and I'm okay")
    print("I sleep all night and i work all day")


print("Yo")
print_lyrics()
x = x + 2
print(x)    



def greet(lang):
    if lang =="es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"


print(greet("en"),"Glenn")
print(greet("es"),"Sally")
print(greet("fr"),"Michael")