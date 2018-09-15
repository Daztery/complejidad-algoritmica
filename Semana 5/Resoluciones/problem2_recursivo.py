def quickselect(n,l,r,i,result):
    if n[0]/n[1] > i[0]/i[1]:
        result.append("R")
        quickselect(n,i,r,(i[0]+r[0],i[1]+r[1]),result)
    elif n[0]/n[1] < i[0]/i[1]:
        result.append("L")
        quickselect(n,l,i,(i[0]+l[0],i[1]+l[1]),result)
    return result

a=[]
while(True):
    t,d=[int(i) for i in input().split()]
    if t==1 and d==1:
        break
    a.append((t,d))
for i in a:print("".join(quickselect(i,(0,1),(1,0),(1,1),[])))
