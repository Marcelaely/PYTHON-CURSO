datos=10
nativa=100
print("estoy antes del if")
if datos==nativa:
    print("LAS VLAN son iguales")
    print("estoy dentro del if")
else:
    print("LAS VLAN son diferentes")

#ejercicio 2 interaccion
acl=int(input("Ingrese el # de ACL: "))
if acl>=1 and acl <=99:
    print("LA ACL es estandar ")
elif acl>=100 and acl <=199:
    print("LA ACL es extendida ")
else:
    print("No no es un # de ACL ")

