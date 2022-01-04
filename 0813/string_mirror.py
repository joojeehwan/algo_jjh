
T = int(input())

for tc in range(1, T + 1):
    words = input()
    res =""
    for word in words:
        if word == "b":
           res = "d" + res

        elif word == "d":
            res = "b" + res

        elif word == "p":
            res = "q" + res

        else:
            res = "p" + res

    print(f"#{tc} {res}")