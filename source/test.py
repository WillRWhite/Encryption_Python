ASCII_RANGE = range(33,127)

def main():
    #printASCII()
    modulo3()


def modulo():
    for i in range(30):
        # Require mode 8 starting at 4
        c=i+4
        c=c%(8+4)
        if c == 0:
            c = 4
        print(c)

def modulo3():
    # Require mod 94 starting at 33
    for i in range(300):
        c=i+15
        c=c%(120+4)
        if c == 0:
            c = 15
        print(c)



def modulo1():
    for i in range(300):
        c=i+33
        c=c%(95+33)
        if c == 0:
            c=33
        print(c, chr(c))
    
def modulo2(): 
    for i in range(300):
        c=i+33
        c=c%(127) 
        if c == 0:
            c = c+33 
        print(c)  




def printASCII():
    print("Hello from main")
    print("Begin")
    for c in ASCII_RANGE:
        print(c, chr(c))
    print("End")


if __name__ == "__main__":
    main()
