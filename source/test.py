#ASCII_RANGE = range(33,127)
ASCII_MAX = 127
ASCII_MIN = 33
ASCII_RANGE = range(ASCII_MIN,ASCII_MAX)


def main():

    # printASCII()

    for c in ASCII_RANGE:
        e = encode(c,1)
        d = decode(e,1)
        print(c, chr(c), e, chr(e), end=" ")
        print(d, chr(d))

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


if __name__ == "__main__":
    main()
