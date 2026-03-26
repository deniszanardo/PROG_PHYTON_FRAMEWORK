#se tem colchetes é lista não é variável, 
saldo = [1500.0]


extrato = []

adicionando a soma 
extrato.append(sum(saldo))


saque =  float(input('Digite o saque: '))


transacao =  sum(saldo) - saque


extrato.append(saque)


saldo = [transacao]

# concatenando um dado literal com um valor numerico 
print('Saldo R$', saldo)

# tenho uma input do tipo floar que adiciona ao extrato e vou concatenar a um valor numerico 
deposito =  float(input('Digite o Deposito R$: '))


extrato.append(deposito)


transacao =  sum(saldo) + deposito


saldo = [transacao]


print('Saldo R$', saldo)


print(extrato)



