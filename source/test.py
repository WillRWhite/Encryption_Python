import sys

#ASCII_RANGE = range(33,126)
ASCII_MAX = 126
ASCII_MIN = 32
ASCII_RANGE = range(ASCII_MIN,ASCII_MAX)


def main():

    #inputFile = input("What is the name of the input file: ")
    #outputFile = input("What is the name of the output file: ")

    seed = 10
    coding = "d"

    #inFile=open("infile.txt", "r")
    #outFile = open("outfile.txt", 'w')

    inFile=open("outfile.txt", "r")
    outFile = open("outfile2.txt", 'w')



    if coding == "e":
        while True:
            char = inFile.read(1)
            if not char:
                break
            char = encode(ord(char),seed)
            outFile.write(chr(char))
    else:
        while True:
            char = inFile.read(1)
            if not char:
                break
            char = decode(ord(char),seed)
            outFile.write(chr(char))



# Note for functions encode and decode seed is an integer between 1 and 99
def encode(c,seed):
    c = c + seed
    if c > ASCII_MAX:
        #c = ASCII_MIN + c - ASCII_MAX
        c = c + (ASCII_MIN - ASCII_MAX)
    return c

def decode(c,seed):
    c = c - seed
    if c < ASCII_MIN:
        #c = ASCII_MAX + c - ASCII_MIN
        c = c + (ASCII_MAX - ASCII_MIN)
    return c

def printASCII():
    print("Begin ASCII Table")
    for c in ASCII_RANGE:
        print(c, chr(c))
    print("End ASCII Table")

def test():
    # printASCII()
    for c in ASCII_RANGE:
        e = encode(c,10)
        d = decode(e,10)
        print(c, chr(c), e, chr(e), end=" ")
        print(d, chr(d))



if __name__ == "__main__":
    main()
