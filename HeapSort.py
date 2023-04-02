# foram declaradas duas listas onde i e j correspondem aos seus indices 
# aqui teremos nossa funcao de troca
# essa funcao recebe como parametro a lista que criamos, mais o i e o j 
# que correspondem aos seus indices 
def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

# essa funcao nos ajudara a acumular a lista 
# toda vez que quisermos extrair o maior elemento da nossa lista 
# podemos filtrar o elemento que trocamos com o maior elemento 
# para manter um heap maximo 
# sempre que quisermos peneirar um elemento especifico , quando estivermos empilhando a nossa lista
# queremos ser capazes  de mover o elemento superior para baixo, como foi explicado anteriormente 
# para que tenhamos o novo elemento superior sendo o maior 
def siftDown(lst, i, upper):
    # entao teremos um loop enquanto a condicao for verdadeira 
    # obs: nao usaremos recursao para que evitemos, porque se formos usar uma lista muito grande 
    # poderiamos acabar com um erro de recursao, porque vamos ate um certo limite 
    while(True): 
        # queremos filtrar nosso pai necessario para um dos filhos se houver filhos 
        # primeiro temos que obter os indices dos filhos 
        # representa o indice do pai atual e o no raiz da nossa arvore 
        # assim podemos nos referir ao filho de qualquer no pai em uma pilha 
        # esses sao os indices dos filhos esquerdo e direito 
        l, r = i*2+1, i*2+2
        # verificar se temos dois filhos para o no pai
        # upper: limite superior da nossa lista que pretendemos considerar como uma pilha 
        # pode estar entre 0 e o comprimento da lista 
        # se tivermos dois filhos entao: 
        if max(l, r) < upper:
                # vamos conferir se o pai é o maior que ambos os filhos 
                # se for verdade nao devemos fazer mais nada aqui 
                # podemos so dizer break, pois caso seja menor, nao havera troca
                if lst[i] >= max(lst[l], lst[r]): break
                # vamos trocar o pai pelo filho maior 
                # o filho esquerdo eh maior que o direito ou o direito eh maior que o esquerdo 
                # isso significa que queremos trocar o no pai com o filho esquerdo 
                elif lst[l] > lst[r]: 
                    # troca o i com o l da lista com o elemento da esquerda     
                    swap(lst, i, l)
                    # para mover o ponteiro para nosso no pai 
                    # atualizar o pai para refletir no novo pai 
                    i = l   
                else: 
                    # caso contrario vamos trocar o indice com o elemento da direita
                    swap(lst, i, r)
                    # o ponteiro muda para o indice R 
                    i = r 
        # conferir se existe apenas um filho 
        # vamos considerar o filho esquerdo 
        # se for menor que o superior, significa que temos um filho esquerdo 
        elif l < upper:
            # se esse filho eh maior que o pai 
            if lst[l] > lst[i]:
                # se sim, vamos trocar esses dois indices 
                swap(lst, i, l)
                # setar o novo no pai 
                i = l
            # nao eh mais necessario filtrar para sair desse loop 
            else: break
        # verificar se o filho direito existe
        elif r < upper: 
            if lst[r] > lst[i]:
                # trocar os indices 
                swap(lst, i, r)
                # setar o pai novo 
                i = r
            else: break
        # se nao houver filhos, nao ha peneiracao para fazer pois nao ha filhos para trocar com outro 
        else: break

# vamos definir uma funcao que tenha o heapsort como entrada e que o retorne
def heapsort(lst):
    # pilha maxima 
    # j no comprimento do intervalo 
    # esse indice se refere ao ultimo pai 
    for j in range((len(lst)-2)//2, -1, -1):
        #  acumula nossa lista 
         siftDown(lst, j, len(lst)) 

    # classificacao 
    # quando paramos no indice 0, todo o resto da lista ja esta classificado
    for end in range(len(lst)-1, 0, -1):
         swap(lst, 0, end)
        #  aqui nao queremos considerar nenhum item no nosso indice end ate o final da lista 
         siftDown(lst, 0, end)

lst = [5, 16, 18, 14, 20, 1, 26]
# crescente
lst = [i for i in range(10, 1, -1)]
heapsort(lst)
print(lst)