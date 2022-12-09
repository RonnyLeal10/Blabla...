x=int(input("Tempo inicial em hora: "))
if x >= 0 and x < 24:
    y=int(input("Tempo inicial em minutos: "))
    if y >= 0 and y < 60:
        z=int(input("Duração do evento: "))
        Mt=y+z
        Ht=x+(Mt//60)
        Mt=Mt%60
        if Ht > 23:
            Ht = Ht % 24
        if len(str(Ht)) == 1 and len(str(Mt)) == 1:
            print("Tempo final: 0" +str(Ht)+":0"+str(Mt))
        elif len(str(Mt)) == 1:
            print("Tempo final: " +str(Ht)+":0"+str(Mt))
        elif len(str(Ht)) == 1:
            print("Tempo final: 0" +str(Ht)+":"+str(Mt))
        else:
            print("Tempo final: " +str(Ht)+":"+str(Mt))
    else:
        print("Os minutos têm que ser entre 0 e 59.")
else:
    print("A hora tem que ser entre 0 e 23.")
#njndfjnvfjvnjjfbb
x=int(input("Tempo inicial (horas 0..23): "))
y=int(input("Tempo inicial (minutos 0..59): "))
z=int(input("Duraçção do evento (minutos): "))
M=y+z
Horatotal=x+(M//60)
B=M%60
print("tempo final: ",str(Horatotal)+":"+str(B))
#byftuff
print("Batem, levemente,"," Levemente ,")
print("como quem chama por mim.\n","...")
#hbfvvhef
x=int(input("Prova 1? "))
y=int(input("Prova 2? "))
z=int(input("Prova 3? "))
m=((x*2)+(y*4)+(z*6))/12
print("Média =",m)
#IVA
x=int(input("Valor do dinheiro:"))
z=x//1.23
