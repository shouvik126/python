item=['april 17 1997','shouvik pradhan',8.51]
print(item[2])
date,name,no=['april 17 1997','shouvik pradhan',8.51]
print(name)
def drop_first_last(grades):
    first,*middle,last=grades
    avg=sum(middle)/len(middle)
    print(avg)
drop_first_last([65,76,98,54,21,54,65,99,88,78])