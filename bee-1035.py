a,b,c,d = map(int,input().split())

conditions = [
    b>c, d>a, (c+d)>(a+b), c>=0, d>=0, (a%2) == 0
]

if all(conditions):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")