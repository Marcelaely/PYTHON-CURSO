#for
o=[ ]
lista=["a","b","c","d"]
texto="CEC EPN curso de Python ESS"
for item in range(10,0,-1):
    print(item)
print("\n"*2)
for i in texto:
    if "o" in i:
        o.append(i)
    print(i,end="")
print("\n"*2)
for elemento in lista:
    print(elemento,end=" * ")