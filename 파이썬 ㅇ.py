start=int(input("시작값을 입력하시오:"))
end=int(input("끝값을 입력하시오:"))
baesu=int(input("배수를 입력하시오:"))


def baesu_sum(start,end,baesu):
    hap=0
    i=start
    while i<=end:
        if i%baesu==0:
            hap=hap+i
        i=i+1
    return hap
print("합계",baesu_sum(start, end,baesu))

