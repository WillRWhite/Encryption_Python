import sys

# Constants
# Max of ASCII range supported
ASCII_MAX = 126
# Min of ASCII range supported
ASCII_MIN = 32
ASCII_RANGE = range(ASCII_MIN,ASCII_MAX)
# Line feed character
LF = chr(10)
# Carrage return character
CR = chr(13)

def main() -> int:

    if len(sys.argv) < 5:
        try:
            encoding: str = input("Encode (e) or decode (d): ")
            seed: int = int(input("What is the seed (an int from 1 to 50): "))
            inputFileName = input("What is the name of the input file: ")
            outputFileName = input("What is the name of the output file: ")
        except:
            printUsage()
    else:
        try:
            encoding: str = sys.argv[1]
            seed: int = int(sys.argv[2])
            inputFileName = sys.argv[3]
            outputFileName = sys.argv[4]
        except:
            printUsage()

    #encoding: str = "d"
    #seed: int = 10

    #inputFile = input("What is the name of the input file: ")
    #outputFile = input("What is the name of the output file: ")
    #inFile=open("infile.txt", "r")
    #outFile = open("outfile.txt", 'w')

    # Open input and output files
    inFile = open(inputFileName, "r")
    outFile = open(outputFileName, 'w')

    # Encode the file
    if encoding == "e":
        while True:
            char = inFile.read(1)
            if not char:
                break
            char = encode(char,seed)
            outFile.write(char)
    # Decode the file
    else
        while True:
            char = inFile.read(1)
            if not char:
                break
            char = decode(char,seed)
            outFile.write(char)

    return 0


def encode(c: str, seed: int) -> str:
    # Encode function to encode a character based on seed
    # 'c' is a single character to be encoded
    # 'seed' is an integer between 1 and 99
    if c in [LF,CR]:
        return c
    c = ord(c)
    c = c + seed
    if c > ASCII_MAX:
        c = c + (ASCII_MIN - ASCII_MAX)
    return chr(c)

def decode(c: str, seed: int) -> str:
    # Decode function to decode a character based on seed
    # 'c' is a single character to be decoded
    # 'seed' is an integer between 1 and 99
    if c in [LF,CR]:
        return c
    c = ord(c)
    c = c - seed
    if c < ASCII_MIN:
        c = c + (ASCII_MAX - ASCII_MIN)
    return chr(c)

def printASCII():
    # Print the ASCII table used
    # Test function not required for release
    print("Begin ASCII Table")
    for c in ASCII_RANGE:
        print(c, chr(c))
    print("End ASCII Table")

def test():
    # Test function not required for release
    for c in ASCII_RANGE:
        e = encode(c,10)
        d = decode(e,10)
        print(c, chr(c), e, chr(e), end=" ")
        print(d, chr(d))

def printUsage():
    # Usage instructions
    print(" ")
    print("Usage:-")
    print("     code fn seed infile outfile")
    print(" ")
    print("          encode/decode: 'e' = encode message file, 'd' = decode message file")
    print("          seed: cipher, an integer 1 to 50. The same must be used for decode")
    print("          The cipher needs to be transmitted seperatly to the recepient of the")
    print("          the message as securely as is possible")
    print("          infile: input file")
    print("          outfile: output file")
    print()
    sys.exit()


if __name__ == "__main__":
    main()
