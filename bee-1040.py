a,b,c,d = map(float,input().split())

m = (2*a + 3*b + 4*c + 1*d) / (2+3+4+1)

print(f"Media: {m:.1f}")

if m >= 7.0:
    print("Aluno aprovado.")

elif m < 5.0:
    print("Aluno reprovado.")

elif m >= 5.0 and m <= 6.9:
    print("Aluno em exame.")
    e = float(input())
    print(f"Nota do exame: {e:.1f}")

    n = (m+e) / 2
    if n >= 5.0:
        print("Aluno aprovado.")

    if n <= 4.9:
        print("Aluno reprovado.")
    
    print(f"Media final: {n:.1f}")