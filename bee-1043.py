a,b,c = map(float,input().split())

con = [
    a < b+c,
    b < a+c,
    c < a+b
]

if all(con):
    p = a+b+c
    print(f"Perimetro = {p:.1f}")

else:
    r = .5*(a+b)*c
    print(f"Area = {r:.1f}")