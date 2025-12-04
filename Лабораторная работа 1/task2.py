mbayt=1.44
bayt = mbayt * 1024 * 1024
stran = 100
strok = 50
simvol = 25
vec = 4
kniga = stran * strok * vec * simvol
result = int(bayt // kniga)


print("Количество книг, помещающихся на дискету:", result)
