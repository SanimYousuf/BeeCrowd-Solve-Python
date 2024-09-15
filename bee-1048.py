a = float(input())

if a <= 400:
    r = (a/20)*3
    n = a + r
    print(f"Novo salario: {n:.2f}")
    print(f"Reajuste ganho: {r:.2f}")
    print("Em percentual: 15 %")

elif 400 < a <= 800:
    r = (a/50)*6
    n = a + r
    print(f"Novo salario: {n:.2f}")
    print(f"Reajuste ganho: {r:.2f}")
    print("Em percentual: 12 %") 

elif 800 < a <= 1200:
    r = (a/10)
    n = a + r
    print(f"Novo salario: {n:.2f}")
    print(f"Reajuste ganho: {r:.2f}")
    print("Em percentual: 10 %") 

elif 1200 < a <= 2000:
    r = (a/100)*7
    n = a + r
    print(f"Novo salario: {n:.2f}")
    print(f"Reajuste ganho: {r:.2f}")
    print("Em percentual: 7 %") 

else:
    r = (a/50)*2
    n = a + r
    print(f"Novo salario: {n:.2f}")
    print(f"Reajuste ganho: {r:.2f}")
    print("Em percentual: 4 %")  