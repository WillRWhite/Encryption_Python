import sys

def main():

    if len(sys.argv) < 5:
        print(" ")
        print("Usage:-")
        print("     code fn seed infile outfile")
        print(" ")
        print("          fn: 'e' = encode message file, 'd' = decode message file")
        print("          seed: cipher, an integer 1 to 50. The same must be used for decode")
        print("          The cipher needs to be transmitted seperatly to the recepient of the")
        print("          the message as securely as is possible")
        print("          infile: input file")
        print("          outfile: output file")
        print(" ")
        print("     Encoded message must be terminated by '>' otherwise the program will exit with an error")
 #       exit()
 #   if ((sys.argv[1] != 'e') and (sys.argv[1] != 'd')):
 #       print(" ")
 #       print("Incorrect coding function. Function must be either 'e' or 'd'")
        
    function = input("Encode (e) or decode (d): ")
    #seed = int(input("What is the seed (an int from 1 to 50): "))
    inputFile = input("What is the name of the input file: ")
    outputFile = input("What is the name of the output file: ")
        
    inFile=open(inputFile, "r")
    outFile = open(outputFile, 'w')

    while True:
        char = inFile.read(1)
        if not char:
            break
        outFile.write(char)




main()


