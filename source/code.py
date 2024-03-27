import sys
# seed must be <= maxchar

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
    exit()
if ((sys.argv[1] != 'e') and (sys.argv[1] != 'd')):
    print(" ")
    print("Incorrect coding function. Function must be either 'e' or 'd'")
    
fn = sys.argv[1]
seed = int(sys.argv[2])
infile = sys.argv[3]
outfile = sys.argv[4]

def chrTnum(chr):
    if chr == 'a': n = 1
    if chr == 'b': n = 2
    if chr == 'c': n = 3
    if chr == 'd': n = 4
    if chr == 'e': n = 5
    if chr == 'f': n = 6
    if chr == 'g': n = 7
    if chr == 'h': n = 8
    if chr == 'i': n = 9
    if chr == 'j': n = 10
    if chr == 'k': n = 11
    if chr == 'l': n = 12
    if chr == 'm': n = 13
    if chr == 'n': n = 14
    if chr == 'o': n = 15
    if chr == 'p': n = 16
    if chr == 'q': n = 17
    if chr == 'r': n = 18
    if chr == 's': n = 19
    if chr == 't': n = 20
    if chr == 'u': n = 21
    if chr == 'v': n = 22
    if chr == 'w': n = 23
    if chr == 'x': n = 24
    if chr == 'y': n = 25
    if chr == 'z': n = 26
    if chr == 'A': n = 27
    if chr == 'B': n = 28
    if chr == 'C': n = 29
    if chr == 'D': n = 30
    if chr == 'E': n = 31
    if chr == 'F': n = 32
    if chr == 'G': n = 33
    if chr == 'H': n = 34
    if chr == 'I': n = 35
    if chr == 'J': n = 36
    if chr == 'K': n = 37
    if chr == 'L': n = 38
    if chr == 'M': n = 39
    if chr == 'N': n = 40
    if chr == 'O': n = 41
    if chr == 'P': n = 42
    if chr == 'Q': n = 43
    if chr == 'R': n = 44
    if chr == 'S': n = 45
    if chr == 'T': n = 46
    if chr == 'U': n = 47
    if chr == 'V': n = 48
    if chr == 'W': n = 49
    if chr == 'X': n = 50
    if chr == 'Y': n = 51
    if chr == 'Z': n = 52
    if chr == ' ': n = 53
    if chr == '.': n = 54
    if chr == ',': n = 55
    if chr == '\n': n = 56
    if chr == '>': n = 1000
    return (n)

def numTchr(n):
    if n == 1: chr = 'a'
    if n == 2: chr = 'b'
    if n == 3: chr = 'c'
    if n == 4: chr = 'd'
    if n == 5: chr = 'e'
    if n == 6: chr = 'f'
    if n == 7: chr = 'g'
    if n == 8: chr = 'h'
    if n == 9: chr = 'i'
    if n == 10: chr = 'j'
    if n == 11: chr = 'k'
    if n == 12: chr = 'l'
    if n == 13: chr = 'm'
    if n == 14: chr = 'n'
    if n == 15: chr = 'o'
    if n == 16: chr = 'p'
    if n == 17: chr = 'q'
    if n == 18: chr = 'r'
    if n == 19: chr = 's'
    if n == 20: chr = 't'
    if n == 21: chr = 'u'
    if n == 22: chr = 'v'
    if n == 23: chr = 'w'
    if n == 24: chr = 'x'
    if n == 25: chr = 'y'
    if n == 26: chr = 'z'
    if n == 27: chr = 'A'
    if n == 28: chr = 'B'
    if n == 29: chr = 'C'
    if n == 30: chr = 'D'
    if n == 31: chr = 'E'
    if n == 32: chr = 'F'
    if n == 33: chr = 'G'
    if n == 34: chr = 'H'
    if n == 35: chr = 'I'
    if n == 36: chr = 'J'
    if n == 37: chr = 'K'
    if n == 38: chr = 'L'
    if n == 39: chr = 'M'
    if n == 40: chr = 'N'
    if n == 41: chr = 'O'
    if n == 42: chr = 'P'
    if n == 43: chr = 'Q'
    if n == 44: chr = 'R'
    if n == 45: chr = 'S'
    if n == 46: chr = 'T'
    if n == 47: chr = 'U'
    if n == 48: chr = 'V'
    if n == 49: chr = 'W'
    if n == 50: chr = 'X'
    if n == 51: chr = 'Y'
    if n == 52: chr = 'Z'  
    if n == 53: chr = ' '
    if n == 54: chr = '.'
    if n == 55: chr = ','
    if n == 56: chr = '\n'
    return (chr)

def readchr():
    chr = fin.read(n)
    n = chrTnum(chr)
    return n

maxchr = 56
fin=open(infile, "r")

orig_stdout = sys.stdout
fout = open(outfile, 'w')
sys.stdout = fout

if fn == 'e':   
    while True:
        n = readchr()
        if n == 1000:
            print('>', end = '')
            break
        n = n + seed
        if n > maxchr: n = n - maxchr
        chr = numTchr(n)
        print(chr, end = '')
else:
    while True:
        n = readchr()
        if n == 1000: break
        n = n - seed
        if n <= 0: n = n + maxchr
        chr = numTchr(n)
        print(chr, end = '') 
    
fin.close()
fout.close()

