from random import randint
import time

elevador = [True, False, False, False, False]               #lista boleana para a posição do elevador
req = [0,0,0,0,0]                                           #lista para guardar as requisições de andares

def subir():                                                        #função para alternar os valores boleanos, fazendo com que o elevado suba
    if elevador[3] == True:
        elevador[3] = False
        elevador[4] = True
    elif elevador[2] == True:
        elevador[2] = False
        elevador[3] = True
    elif elevador[1] == True:
        elevador[1] = False
        elevador[2] = True
    elif elevador[0] == True:
        elevador[0] = False
        elevador[1] = True

def descer():                                                       #função para alternar os valores boleanos, fazendo com que o elevado desça
    if elevador[1] == True:
        elevador[1] = False
        elevador[0] = True
    elif elevador[2] == True:
        elevador[2] = False
        elevador[1] = True
    elif elevador[3] == True:
        elevador[3] = False
        elevador[2] = True
    elif elevador[4] == True:
        elevador[4] = False
        elevador[3] = True

def ui():                                                       #função para exibir a interface do elevador
    for i in range(4, -1, -1):
        a=i
        if a == 0:
            a = ('T')
        b=req[i]
        if b == 0:
            b = ('T')
        if req[i] != str('Nenhuma Requisição') and elevador[i] == True:
            print('__{}__||__{}__||👤_>_{}'.format(a,gentenoelevador*'👤' ,b))
        elif req[i] != str('Nenhuma Requisição') and elevador[i] != True:
            print('__{}__||  {}  ||👤_>_{}'.format(a,'  '*gentenoelevador ,b))
        elif req[i] == str('Nenhuma Requisição') and elevador[i] == True:
            print('__{}__||__{}__||____'.format(a,gentenoelevador*'👤'))
        elif req[i] == str('Nenhuma Requisição') and elevador[i] != True:
            print('__{}__||  {}  ||____'.format(a,'  '*gentenoelevador))

while True:

    ondpediu = []  # andares onde pediram o elevador
    onddecer = []  # onde as pessoas que pediram o elevador ^^^^^ querem descer
    gentenoelevador = int(0)     #variável que guarda quantas pessoas tem no elevador
    destinodquementro = []        #lista que guarda os destinos de quem já entrou

    for i in range(5):             #laço para escolher aleatoriamente as requisições de andares
        while True:
            req[i] = randint(0, 5)
            if req[i] != i:  # isso é para a requisição de um andar não ser igual ao de onde ele é pedido, afinal alguem no térreo não iria pegar um elevador pro térreo, certo?
                break

    for i in range(5):  # esse laço é para ir passando por cada termo da lista procurando os que sejam diferente de 5, pois o 5 vale como um "vazio"
        if req[i] != 5:
            ondpediu.append(i)  # adiciona onde as pessoas pediram o elevador
            onddecer.append(req[i])  # adiciona destinos onde as pessoas querem descer
        else:
            req[i] = ('Nenhuma Requisição')

    print('\nONDE PEDIRAM:', ondpediu)
    print('\nONDE VÃO DESCER:', onddecer)

#terreo
    ui()
    time.sleep(2)
    if req[0] != str('Nenhuma Requisição') and elevador[0] == True:  # comando para entrar 1 pessoa
        gentenoelevador += 1
        destinodquementro.append(req[0])
        req[0] = str('Nenhuma Requisição')
        print('Subiu uma pessoa neste andar')
    else:
        print('Ninguém subiu neste andar')
    time.sleep(2)
    subir()

    print('\n' * 20)

#1 andar
    ui()                #chamando a ui antes da execução
    time.sleep(2)       #chamamos uma função da biblioteca time que pausa o código por alguns segundos que nós delimitamos
    if req[1] > 1:      #comando para definir a prioridade, se a requisição for de um andar acima do que está pedindo, a pessoa irá na subida, se não, ela irá esperar a descida
        if req[1] != str('Nenhuma Requisição') and elevador[1] == True:                             # comando para entrar 1 pessoa
            gentenoelevador += 1                    #se passar no if, adicionamos uma pessoa ao elevador
            destinodquementro.append(req[1])        #colocamos na lista o valor do destino de quem acabou de entrar
            req[1] = str('Nenhuma Requisição')      #substituimos a requisição feita por "Nenhuma Requisição"
            print('Subiu uma pessoa neste andar')
        else:
            print('Ninguém subiu neste andar')
    else:
        print("Espere a descida!")
    time.sleep(2)
    subir()

    if 1 in destinodquementro and gentenoelevador != 0:                              # comando para descer pessoas
        gentenoelevador -= destinodquementro.count(1)                                # contamos quantos elementos querem descer no respectivo andar e removemos esse número do total de pessoas que tem dentro do elevador
        print('Uma pessoa ou mais pessoas irão descer nesse andar\n')
        time.sleep(2)
        destinodquementro.remove(1)                                                  # removemos os destinos desse que já foi vistado
    print('\n' * 20)

#2 andar
    ui()
    time.sleep(2)
    if req[2]>2:
        if req[2] != str('Nenhuma Requisição') and elevador[2] == True:               # comando para entrar 1 pessoa
            gentenoelevador += 1
            destinodquementro.append(req[2])
            req[2] = str('Nenhuma Requisição')
            print('Subiu uma pessoa neste andar')
        else:
            print('Ninguém subiu neste andar')
    else:
        print('Espere a descida!')
    time.sleep(2)
    subir()
                                                                                                # comando para descer pessoas
    if 2 in destinodquementro and gentenoelevador != 0:
        gentenoelevador -= destinodquementro.count(2)
        print('Uma pessoa ou mais pessoas irão descer nesse andar\n')
        time.sleep(2)
        destinodquementro.remove(2)
    print('\n' * 20)

#3 andar
    ui()
    time.sleep(2)
    if req[3]>3:
        if req[3] != str('Nenhuma Requisição') and elevador[3] == True:                         # comando para entrar 1 pessoa
            gentenoelevador += 1
            destinodquementro.append(req[3])
            req[3] = str('Nenhuma Requisição')
            print('Subiu uma pessoa neste andar')
        else:
            print('Ninguém subiu neste andar')
    else:
        print('Espere a descida!')
    time.sleep(2)
    subir()
                                                                                            # comando para descer pessoas
    if 3 in destinodquementro and gentenoelevador != 0:
        gentenoelevador -= destinodquementro.count(3)
        print('Uma pessoa ou mais pessoas irão descer nesse andar\n')
        time.sleep(2)
        destinodquementro.remove(3)
    print('\n' * 20)

#4 andar
    ui()
    time.sleep(2)
    if req[4] != str('Nenhuma Requisição') and elevador[4] == True:                          # comando para entrar 1 pessoa
        gentenoelevador += 1
        destinodquementro.append(req[4])
        req[4] = str('Nenhuma Requisição')
        print('Subiu uma pessoa neste andar')
    else:
        print('Ninguém subiu neste andar')
    time.sleep(2)
    subir()
                                                                                            # comando para descer pessoas
    if 4 in destinodquementro and gentenoelevador != 0:
        gentenoelevador -= destinodquementro.count(4)
        print('Uma pessoa ou mais pessoas irão descer nesse andar\n')
        time.sleep(2)
        destinodquementro.remove(4)
    print('\n' * 20)

                                            # parada para fazer o caminho inverso
    ui()
    time.sleep(2)
    descer()                                                                                      #começar a descer
    print('\n' * 20)

                                                                                                    # 3 andar
    ui()
    time.sleep(2)
    if req[3] != str('Nenhuma Requisição') and elevador[3] == True:                          # comando para entrar 1 pessoa
        gentenoelevador += 1
        destinodquementro.append(req[3])
        req[3] = str('Nenhuma Requisição')
        print('Subiu uma pessoa neste andar')
    else:
        print('Ninguém subiu neste andar')
    time.sleep(2)
    descer()
    if 3 in destinodquementro and gentenoelevador != 0:
        gentenoelevador -= destinodquementro.count(3)
        print('Uma pessoa ou mais pessoas irão descer nesse andar\n')
        time.sleep(2)
        destinodquementro.remove(3)
    print('\n' * 20)

                                                                                                    # 2 andar
    ui()
    time.sleep(2)
    if req[2] != str('Nenhuma Requisição') and elevador[2] == True:  # comando para entrar 1 pessoa
        gentenoelevador += 1
        destinodquementro.append(req[2])
        req[2] = str('Nenhuma Requisição')
        print('Subiu uma pessoa neste andar')
    else:
        print('Ninguém subiu neste andar')
    time.sleep(2)
    descer()
    if 2 in destinodquementro and gentenoelevador != 0:
        gentenoelevador -= destinodquementro.count(2)
        print('Uma pessoa ou mais pessoas irão descer nesse andar\n')
        time.sleep(2)
        destinodquementro.remove(2)
    print('\n' * 20)

                                                                                                    # 1 andar
    ui()
    time.sleep(2)
    if req[1] != str('Nenhuma Requisição') and elevador[1] == True:  # comando para entrar 1 pessoa
        gentenoelevador += 1
        destinodquementro.append(req[1])
        req[1] = str('Nenhuma Requisição')
        print('Subiu uma pessoa neste andar')
    else:
        print('Ninguém subiu neste andar')
    time.sleep(2)
    descer()
    if 1 in destinodquementro and gentenoelevador != 0:
        gentenoelevador -= destinodquementro.count(1)
        print('Uma pessoa ou mais pessoas irão descer nesse andar\n')
        time.sleep(2)
        destinodquementro.remove(1)
    print('\n' * 20)

                                                                                                    # terreo
    ui()
    time.sleep(2)
    descer()
    if 0 in destinodquementro and gentenoelevador != 0:
        gentenoelevador -= destinodquementro.count(0)
        print('Uma pessoa ou mais pessoas irão descer nesse andar\n')
        time.sleep(2)
        destinodquementro.remove(0)
    print('\n' * 20)

    ui()
    time.sleep(1)
                                                                        # final para reiniciar ou parar o código
    ctn = input('\nDar outra volta de elevador? S/N\n')
    if ctn.lower() == 'sim' or ctn.lower() == 's':
        continue
    elif ctn.lower() == 'nao' or ctn.lower() == 'não' or ctn.lower() == 'n':
        break
    else:
        break