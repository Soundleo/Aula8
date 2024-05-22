# importa bibliotecas
import os 
import time

# declaração de variável
numero = int(input('Lazarento, informe um número qualquer.\n'))
os.system('cls')


# loop
while numero > -1:
    print (f'Essa mensagem se auto destruirá em {numero}')
    time.sleep(1)
    os.system('cls')
    numero -= 1
print('booommmm')

########################################################################################################################

#usar o continue 

# cont = 0 

# while cont < 10:
    # cont += 1 
    # if cont %2 == 0:
        # print(cont)
    # else: 
        # continue
    # print ('continuando')
# 
# print('ACABOU')
        
