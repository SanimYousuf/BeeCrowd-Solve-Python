a, b, c, d = map(int, input().split())

if b > d:
    d += 60
    a -= 1
    m = d - b

    if a > c:
        c += 24
        h = c - a
        print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")
    else:
        h = c - a
        print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")
