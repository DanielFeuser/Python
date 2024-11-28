#else
tempoDeJogo = int(input("Quanto tempo temos já jogado? ")) # Pedindo para o usuário um valor inteiro (int) para ser atribuido na variável tempoDeJogo.
if tempoDeJogo <= 90: # Se a variável (tempoDeJogo) for menor ou igual a 90.
    print("Temos tempo ainda!!") # Imprima "Temos tempo ainda!!".
    print("Amo muito futebol!!") # Imprima "Amo muito futebol!!".
else: #Caso contrario (A variável (tempoDeJogo) for maior que 90).
    print("Está acabando!!") # Imprima "Está acabando!!".
    print("Apita logo Juiz!!") # Imprima "Apita logo Juiz!!".