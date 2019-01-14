exp=str(input())
exp_lst=list(exp)
exp_lst.insert(0,"d")
exp_lst.append("d")
#print(exp_lst)
alpha=["d", "x","/", "+", "-", "a", "b", "c", "d", "e"]

def oper(expression,operator):
    mult1=0
    mult2=[]
    mult2int=0
    subseq1_end=0
    subseq2_start=0
    sub1=[]
    sub2=[]
    new=["d"]
    for element in expression:
        if element == operator:
            for i in range (1,100):
                if expression[expression.index(element)-i] not in alpha:
                    mult1=mult1+float(expression[expression.index(element)-i])*pow(10,i-1)
                else:
                   subseq1_end=expression.index(element)-i
                   break
            for i in range (1,100):
                if expression[expression.index(element)+i] not in alpha:
                    mult2.append(expression[expression.index(element)+i])
                else:
                   subseq2_start=expression.index(element)+i-1
                   break
            break
    for i in range(1,subseq1_end+1):
        sub1.append(expression[i])
    for i in range(subseq2_start+1,len(expression)-1):
        sub2.append(expression[i])
    mult2.reverse()
    for i in range (0,len(mult2)):
        mult2int=mult2int+float(mult2[i])*pow(10,i)
    for element in sub1:
        new.append(element)
    if operator=="^":
        new.append(str(pow(mult1,mult2int)))
    if operator=="x" or operator=="*":
        new.append(str(mult1*mult2int))
    if operator=="/":
        new.append(str(mult1/mult2int))
    if operator=="+":
        new.append(str(mult1+mult2int))
    if operator=="-":
        new.append(str(mult1-mult2int))
    for element in sub2:
        new.append(element)
    new.append("d")
    return new

def calculate(exp):
    while "^" in exp:
        exp=oper(exp, "^")
    while "x" in exp:
        exp=oper(exp,"x")
    while "/" in exp:
        exp=oper(exp,"/")
    while "-" in exp:
        exp=oper(exp,"-")
    while "+" in exp:
        exp=oper(exp,"+")
    return exp[1]

print(calculate(exp_lst))
