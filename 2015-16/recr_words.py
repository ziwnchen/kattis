import sys

word=sys.stdin.readline().strip()

def find_rep(string):
    if len(string)==1:
        return True
    elif len(string)==2:
        if string[0]==string[1]:
            return True
        else:
            return False
    else:
        length=len(string)
        c1=string[0]
        c2=string[length-1]
        sub_string=string[1:length-1]
        if c1!=c2:
            return False
        else:
            if find_rep(sub_string):
                return True
            else:
                return False


if find_rep(word):
    print("PALINDROME")
else:
    print("NOT PALINDROME")

