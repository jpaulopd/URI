senha_correta = int(2002)
senha_digitada = 0
while(senha_digitada != senha_correta):
    senha_digitada = int(input())

    if(senha_correta == senha_digitada):
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
