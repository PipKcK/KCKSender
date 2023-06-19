import string
def printg(string):
    print("\033[92m[ \033[0m+\033[92m ]", string, "\033[0m")

def printr(string):
    print("\033[91m[ \033[0m-\033[91m ]", string, "\033[0m")

def printy(string):
    print("\033[93m[ ! ]", string, "\033[0m")

def printb(string):
    print("\033[34m[ > ]", string, "\033[0m")

def printp(string):
    print("\033[35m[ ! ]", string, "\033[0m")