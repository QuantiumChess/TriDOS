l1=[]
l2=[]
l3=[]
r=''
fast=''
fast_result=0
memory=[]
result=0
temp=0
temp2=0
count=0
def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
def processor(operation, arg1, arg2):
    global r, result, temp, count
    r=''
    result=0
    temp=0
    temp2=0
    count=0
    l1=[]
    l2=[]
    l3=[]
    t1=convert_base(arg1, to_base=3, from_base=10)
    t2=convert_base(arg2, to_base=3, from_base=10)
    if len(t1)>len(t2):
        for i in range(len(t1)-len(t2)):
            t2="0"+t2
    elif len(t2)>len(t1):
        for i in range(len(t2)-len(t1)):
            t1="0"+t1
    for j in t1:
        l1.append(int(j))
    for k in t2:
        l2.append(int(k))
    l1.insert(0,0)
    l2.insert(0,0)    
    if operation=="sum":
        for o in range(len(l1)):
            l3.append(l1[o]+l2[o])
        for pp in range(len(l3)):
            for p in range(len(l3)):
                if l3[p]>2:
                    l3[p]=l3[p]-3
                    l3[p-1]=l3[p-1]+1
        for e in range(len(l3)):
            r=r+str(l3[e])
        result=int(r, 3)
    elif operation=="dif" and not(arg2>arg1):
        for o in range(len(l1)):
            l3.append(l1[o]-l2[o])
        for pp in range(len(l3)):
            for p in range(len(l3)):
                if l3[p]<0:
                    l3[p]=l3[p]+3
                    l3[p-1]=l3[p-1]-1
        for e in range(len(l3)):
            r=r+str(l3[e])
        result=int(r,3)
    elif operation=="dif" and arg2>arg1:
        result=arg1-arg2
    elif operation=="mul":
        temp=arg2
        while True:
            if temp%3==0:
                temp=temp/3
                count=count+1
            else:
                break
        l3=l1
        for o in range(count):
            l3.append(0)
        for e in range(len(l3)):
            r=r+str(l3[e])
        result=int(r, 3)
        for p in range(int(arg2/(3**count))):
            processor("sum", result, arg1)
        result=result-arg1
    elif operation=="car":
        if arg1%arg2==0:
            result=int(arg1/arg2)
        else:
            result=arg1/arg2
    elif operation=="xor":
        for i in range(len(l1)):
            if (l1[i]==0 and l2[i]==1) or (l2[i]==0 and l1[i]==1):
                l3.append(0)
            elif (l1[i]==0 and l2[i]==2) or (l1[i]==2 and l2[i]==0):
                l3.append(1)
            elif (l1[i]==1 and l2[i]==2) or (l1[i]==2 and l2[i]==1):
                l3.append(2)
            else:
                l3.append(int(l1[i]))
        for e in range(len(l3)):
            r=r+str(l3[e])
        result=int(r,3)
def ram(typeof, value):
    if typeof=="int":
        value=int(value)
        memory.append(convert_base(value, 3, 10))
    if typeof=="str":
        for m in value:
            memory.append("str"+convert_base(ord(m)))
def fast_convert(arg):
    global fast, fast_result
    number9=convert_base(arg, 9, 10)
    for z in number9:
        if z=="0":
            fast=fast+"00"
        elif z=="1":
            fast=fast+"01"
        elif z=="2":
            fast=fast+"02"
        elif z=="3":
            fast=fast+"10"
        elif z=="4":
            fast=fast+"11"
        elif z=="5":
            fast=fast+"12"
        elif z=="6":
            fast=fast+"20"
        elif z=="7":
            fast=fast+"21"
        elif z=="8":
            fast=fast+"22"
    fast_result=int(fast)
processor(input(), int(input()), int(input()))
ram(input(), input())
fast_convert(int(input()))
print(result)
print(memory)
print(fast_result)
