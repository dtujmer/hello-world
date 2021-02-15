import sys
def generate(x):
    print(x[0] + str(len(x[1:len(x)-1])) + x[len(x)-1])

generate("".join(sys.argv[1:]))
