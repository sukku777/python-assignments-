def duplicate(samplelist):
    li=[]
    for i in samplelist:
        if i not in li:
            li.append(i)
    return li
samplelist=[87,45,41,65,94,41,99,94]
k=(duplicate(samplelist))
print(k)
s=tuple(k)
print(s)
print('min:',min(s))
print('max:',max(s))
