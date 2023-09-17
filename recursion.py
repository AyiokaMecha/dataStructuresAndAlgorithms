# name='my name is DanMecha and this is who I am currently hopefully when the time comes I will change'


# def reverse(name):
#     if name=='':
#         return name
#     return reverse(name[1:])+name[0]

# eman=reverse(name)

# print(eman)


# def binary(number,result):
#     if number==0:
#         return result
#     new=number//2
#     result=str(number%2) +result
#     return(binary(new,result))


# number=4
# meh=''
# result=binary(number,meh)
# print(result)


"""the fibonacci series using recursion"""
def fib(n):
    if (n==0 or n==1):
        return n
    return(fib(n-1) +fib(n-2))


result=fib(15)
print(result)