ent = input()
ent = ent.split()

s = int(ent[0])
t = int(ent[1])
f = int(ent[2])


soma = s + t + f

if soma >= 24:
    soma = soma - 24

elif soma < 0:
    soma = soma + 24

print("{}".format(abs(soma)))

