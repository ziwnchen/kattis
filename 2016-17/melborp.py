import sys
old_string=sys.stdin.readline()

def rev(string):
    if len(string)==1:
        rev_string=string
    else:
        rev_string=rev(string[1:])+string[0]
    return rev_string

print(rev(old_string))