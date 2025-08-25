a=int(input())
divisible_5=(a%5==0)
divisible_7=(a%7==0)
less_than=(a<7)
if divisible_5 and divisible_7:
    print(a)
elif less_than:
    print(a)
else:
    print(a%5)
    print(a%7)
