a = int(input())

a1, a2, a3 = 0,0,0

if a >= 3600:
    a1 = a // 3600
    a = a % 3600

if a >= 60:
    a2 = a // 60
    a = a % 60

a3 = a

print(f"{a1:.0f}:{a2}:{a3}")