dict1 = {"小红":98,"小明":77,"小兰":86,"小花":30,"小惠":60,"二狗":60,"狗剩":77,"小华":80}
def grade(adict):
    s = 0
    bdict = { }
    cdict = { }
    klist = list(adict.keys())
    vlist = list(adict.values())
    for i in range(3):
        cdict[klist[i]] = vlist[i]
        for i in range(3,len(adict)):
            for j in cdict.keys():
                if vlist[i] > cdict[j]:
                    cdict[klist[i]] = vlist[i]
                    del cdict[j]
                    break
            
    for i in adict.keys():
        s += adict[i]
        if adict[i] < 60:
            bdict[i] = adict[i]
    average = s/len(adict)
    return (cdict,average,bdict)
print(grade(dict1))
    
