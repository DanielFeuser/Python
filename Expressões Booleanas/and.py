'''
# Lembrando que para o operador "and" funcionar, os dois valores precisam ser True!
fizerSol = True
forFeriado = False
vouParaPraia = fizerSol and forFeriado # Como os 2 valores são verdadeiros, a resposta vai ser True!
print(vouParaPraia)
'''
tempo = input("Está com sol? (sim/não): ")
feriado = input("É feriado ? (sim/não): ")
if tempo == "sim" and feriado == "sim": # Aqui vemos um exemplo de (and) em um mini programa usando (else e if).
    print("Eba, vamos para a praia !!!")
else:
    print("Droga, não vamos para a praia")    