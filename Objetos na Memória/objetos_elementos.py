#Esse comando is, que permite ver se duas referências, duas variáveis apontam para o mesmo objeto
a = "banana"
b = "banana"
c= "maça"
# Como o conteudo de a e b é o mesmo.
print(a is b) # a é(is) b = True.
# Como o conteudo de a e c não é o mesmo.
print(a is c) # a é(is) c = False
print()


# Aqui o conteudo é o mesmo, porem a variavé é uma só!
a = [81,82,83]
b = [81,82,93]

print(a is b)
# Comparação é ele vai ver se os conteúdos dos objetos são iguais,
print(a==b)