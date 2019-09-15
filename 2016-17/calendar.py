import sys

line=sys.stdin.readline()
date_line=list(map(int,line.split()))

def judge(date_line):
    if date_line[0]>31:
        return 'Format #3'
    elif (date_line[0]>12) & (date_line[0]<=31):
        if date_line[2]>31:
            return 'Format #2'
        else:
            return 'Ambiguous'
    else:
        if date_line[1]>12:
            return 'Format #1'
        else:
            return 'Ambiguous'

print(judge(date_line))