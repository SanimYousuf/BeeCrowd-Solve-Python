a = int(input())

print(f"{a}")

a1,a2,a3,a4,a5,a6,a7 = 0,0,0,0,0,0,0

if a >= 100:
    a1 = a // 100
    a = a % 100
   
if a >= 50:
    a2 = a // 50
    a = a % 50
   
if a >= 20:
    a3 = a // 20
    a = a % 20  

if a >= 10:
    a4 = a // 10
    a = a % 10

if a >= 5:
    a5 = a // 5
    a = a % 5
    
if a >= 2:
    a6 = a // 2
    a = a % 2

if a >=1:
    a7 = a

print(f"{a1} nota(s) de R$ 100,00")
print(f"{a2} nota(s) de R$ 50,00")
print(f"{a3} nota(s) de R$ 20,00")
print(f"{a4} nota(s) de R$ 10,00")
print(f"{a5} nota(s) de R$ 5,00")
print(f"{a6} nota(s) de R$ 2,00")
print(f"{a7} nota(s) de R$ 1,00")