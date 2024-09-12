import math
a,b,c = map(float,input().split())

conditions = [
    (b**2 - 4*a*c)<0,
    a == 0
]

if any(conditions):
    print("Impossivel calcular")
else:
    r1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    r2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")