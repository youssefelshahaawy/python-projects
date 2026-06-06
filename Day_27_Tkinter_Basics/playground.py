def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)
    
add(1,2,3,4,5,6,7,8,9)

def calc(**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calc(3,add=2,multiply=2))