a,b = map(int,input().split())

con = [
    a % b == 0,
    b % a == 0
]

if any(con):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")