
def myAddUniversal(*args):
    s = 0
    for i in range(len(args)):
        s += args[i]
    return s

print("added numbers" , myAddUniversal(1,3,5,7,8))