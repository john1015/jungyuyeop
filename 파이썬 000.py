start=int(input("시작값을 입력하시오"))
end=int(input("끝값을 입력하시오"))
baesu=int(input("배수를 입력하시오"))

def cal_hap(start,end):
    hap=0
    i=start
    while i<=end:
        hap=hap+1
        i=i+1
    return hap
def baesu_sum(start,end,baesu):
    hap=0
    i=start
    while i<=end:
        if i%baesu==0:
            hap=hap+i
        i=i+1
    return hap
print(start,"에서",end,"까지의 합은",cal_hap(start,end))
print(start,"에서",end,"까지",baesu,"의 합은",baesu_sum(start,end,baesu))
