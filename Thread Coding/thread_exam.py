# single thread example
def mul_two(li):
    for idx in range(len(li)):
        li[idx]*=2

n = 1000
li = [i+1 for i in range(n)]

mul_two(li)

print(li)