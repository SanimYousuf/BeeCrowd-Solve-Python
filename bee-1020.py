a = int(input())

a1, a2, a3 = 0,0,0

if a >= 365:
    a1 = a // 365
    a = a % 365

if a >= 30:
    a2 = a // 30
    a = a % 30

a3 = a

print(f"{a1} ano(s)\n{a2} mes(es)\n{a3} dia(s)")