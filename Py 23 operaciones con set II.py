# Operaciones II
# Interseccion
a= {1,2,3,4,5,6}
b= {1,3,5}

e={1,3,5}
print("forma larga",a.intersection(e))
print("forma corta",a & e)

print("+++"*10)

# isdisjoint regresa true si tienen una interseccion nula o vacia.

e={1,3,5}
f={10,11,12}
print("isdisjoint",a.isdisjoint(e))
print("isdisjoint",a.isdisjoint(f))

print("+++"*10)

# issubset
s1={1,2,3,4,5,6,7,8,9,10}
s2={3,4,5}
s3={11,12,13,1}

print(s2.issubset(s1))
print(s1.issubset(s2))
print(s3.issubset(s1))
print(s1.issubset(s1))

print("+++"*10)

print(s2<=(s1)) # Forma abreviada
print(s1<=(s2))
print(s3<=(s1))
print(s1<=(s1))

print("+-+"*10)
# Superset / superconjunto

print(s2>=(s1))
print(s1>=(s2))
print(s3>=(s1))

print("+-+"*10)
# proper subeset, subconjunto propio. es un subconjunto de A que no es igual a A
print(s2<s1)
print(s1<s2)
print(s1<s1)

print("+/+"*10)
# proper superset, superconjunto propio. es un superconjunto de A que no es igual a A
s4={1,2,3,4,5,6,7,8,9,10,11,12}

print(s4>s1)    # s4 es un superconjunto de s1 lo es retorna true
print(s1>s4)
print(s1>s1)

print(" pop -"*6)
# Pop, obtiene y remueve un elemento lo elimina.
print(s4)
print(s4.pop())
print(s4.pop())
print(s4.pop())
print(s4)
