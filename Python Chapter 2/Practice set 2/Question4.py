a = [1,2,30,32,43,765,675,342,5440]
# def div_5(num):
#     if num%5==0:
#         return True

div_5 = lambda num : num%5==0
print(list(filter(div_5,a)))