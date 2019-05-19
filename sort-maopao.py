'''a = input()
alist = [int(i) for i in a.split(' ')]'''
list1 = [1,4,2,0,8,4,2,3,10,1]

'''list1 = {'a':1,'b':4,'c':2,'d':0,'e':8,'f':4,'g':2,'h':3,'i':10,'j':1}'''
def sort_maopao(alist):
    if isinstance(alist,dict):
        vlist = list(alist.values())
        klist = list(alist.keys())
        result = { }
    else:
        vlist = alist

    for i in range(len(alist)-1):
        for j in range(i+1,len(alist)):
            if vlist[i] > vlist[j]:
                b = vlist[i]            
                vlist[i] = vlist[j]            
                vlist[j] = b
                if isinstance(alist,dict):
                    c = klist[i]
                    klist[i] = klist[j]
                    klist[j] = c
    if isinstance(alist,dict):
        for i in range(len(alist)):
            result[klist[i]] = vlist[i]
        return(result)
    else:
        return(vlist)

print(sort_maopao(list1))


