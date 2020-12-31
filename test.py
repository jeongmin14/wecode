# 1부터 num까지의 숫자 중 짝수만 리스트로 담아 출력하기
def even_number(num):
    num = range(1, num+1)
    even_num = []
    for i in num:
        if i % 2 == 0:
            even_num.append(i)
        else :
            pass
    return even_num
        
print(even_number(50))