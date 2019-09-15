import sys

data=sys.stdin.readline()
exp=data.split()

exp_stack=[]
error=""

for token in exp:
    if token.isdigit():
        exp_stack.append(int(token))
    elif (token=='true') or (token=='false'):
        if token=='true':
            exp_stack.append(True)
        else:
            exp_stack.append(False)
    else:
        if len(exp_stack)<2:
            error="SYNTAX ERROR"
            break
        else:
            op1=exp_stack.pop()
            op2=exp_stack.pop()
            if type(op1) != type(op2):
                error="TYPE ERROR"
                break
            elif (type(op1) is bool) & (token!='and') & (token!='or'):
                error="TYPE ERROR"
                break
            elif (type(op1) is int) & (token == 'and' or token== 'or'):
                error="TYPE ERROR"
                break
            else:
                #do the calculation
                curr_exp=str(op1)+" "+token+" "+str(op2)
                result=eval(curr_exp)
                exp_stack.append(result)

if len(exp_stack)==0 | len(exp_stack)>1:
    error="SYNTAX ERROR"

if error=="":
    print(exp_stack[0])
else:
    print(error)