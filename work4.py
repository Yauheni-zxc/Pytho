'''
a=int(input())
b=int(input())
def func(a,b):
    if b == 0:
       return 1
    return a* func(a,b-1) 
print(func(a,b))
        

'''
a = int(input("Введите первое неотрицительное число "))
b = int(input("Введите второе неотрицательно число "))
def recursive_sum(a, b):
    if a == 0:
        return b
    
    return recursive_sum(a - 1, b + 1)


print(recursive_sum(a, b))

