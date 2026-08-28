"""
Implementar um programa em Python para localizar um vetor menor dentro de um vetor maior,
ou seja, localizar subvetor ou segmento de vetor em outro vetor. Alem disso, o programa
deverá permitir deletar e substituir os subvetores localizados. Vamos trabalhar com vetor
tal como muitas das linguagens tradicionais, definindo um tamanho maximo da estrutura e
controlando o espaço utilizado. A ideia aqui é implementar as operações "no braço", percorrendo
todas as posições do vetor e fazendo as movimentações de elementos que forem necessárias,
sem usar recursos prontos da linguagem. O usuário deve fornecer os tamanhos necessários. O
vetor maior deve ser gerado aleatoriamente.
"""
from random import randint, seed


def geraVetor(vet: list, nElem: int)->None:
    """Gera vetor aleatoriamente, com valores dentro da faixa definida"""
    
    print("\nGerando elementos válidos do vetor ...")
    seed()
    for i in range(nElem):
        vet[i]=randint(1,5)

def mostraVetor(texto:str, vet: list, nElem: int)->None:
    """Mostra os elementos de um vetor, informando o nome dele"""
    print(f"\nElementos do {texto}:")
    for i in range(nElem-1):
        print(vet[i],", ",sep="",end="")
    if (nElem>0):
        print(vet[nElem-1])

def saoIguais(v1:list, pos:int, v2:list, tam2: int)->bool:
    """Verifica a ocorrencia de v2, de tamanho tam2, dentro de v1, a
       partir da posição pos. Cabe ao usuário checar se v1 possui elementos
       suficientes a partir de pos para fazer essa comparação. Retorna o
       resultado lógico da comparação (True ou False)"""
    
    print("\nVerificando a igualdade de subvetor ...")
    i=0
    while (i<tam2-1) and (v2[i]==v1[pos+i]):
        i=i+1
    iguais = (i==tam2-1) and (v2[i]==v1[pos+i])
    return iguais

def deletaSegmento(v: list, tam: int, pos:int, n: int)->int:
    """Deleta em v, de tamanho tam, um segmento iniciado em pos de tamanho n.
       Cabe ao usuário checar se v possui elementos suficientes a partir de pos
       para fazer essa deleção. Retorna o novo tamanho reduzido"""
    
    print(f"\nDeletando {n} elementos do vetor a partir de posição {pos} ...")
    i=pos
    while (i+n<tam):
        v[i]=v[i+n]
        i=i+1
    return i #novo tamanho

def insereSubvetor(v1: list, tam1: int, pos: int, v2: list, tam2: int)->int:
    """Insere dentro de v1, de tamanho tam1, o subvetor v2, de tamanho tam2,
       a partir da posição pos. Cabe ao usuário checar se o acrescimo no numero
       de elementos cabe dentro do espaço maximo reservado para o vetor v1"""
    
    print(f"\nInserindo subvetor de {tam2} elementos em vetor a partir de posição {pos}...")
    tam1=tam1+tam2
    i=tam1-1
    while (i-tam2>=pos):
        v1[i]=v1[i-tam2]
        i=i-1
    j=0
    for i in range(pos, pos+tam2,1):
        v1[i]=v2[j];
        j=j+1
    return tam1  #novo tamanho
    
def substituiSegmento(v1, tam1, pos, n, v2, tam2)->int:
    """Substitui em v1, de tam1, um segmento de tamanho n, localizado a partir de pos,
       pelo vetor v2, de tamanho tam2. Poderá haver acrescimo ou decrescimo no numero
       de elementos de v1. Cabe ao usuário checar a compatibilidade das medidas: se
       tem n elementos a partir de pos e se cabe a inserção de tam2 elementos dentro
       do espaço máximo alocado para v1. Retorna o novo tamanho de v1."""
    
    print(f"\nSubstituindo segmento de {n} elementos por subvetor de tamanho {tam2}...")
    tam1=deletaSegmento(v1, tam1, pos, n)
    tam1=insereSubvetor(v1, tam1, pos, v2, tam2)
    return tam1 #novo tamanho

def localizaSubvetor(v1:list,tam1:int, v2:list, tam2:int)->int:
    """Localiza em v1, de tamanho tam1, todas as ocorrências de v2, de tamanho tam2.
       São consideradas apenas as ocorrências não sobrepostas. As posições das ocorrências
       são inseridas no vetor de achados. Retorna o novo tamanho do vetor de achados."""
    
    print("\nLocalizando ocorrencias de subvetor ...")

    i=0
    pos=0    
    while (pos+tam2-1<tam1):
        if saoIguais(v1, pos, v2, tam2):
            vetorAchados[i]=pos
            pos=pos+tam2 #salta a posição para após a ocorrencia, para evitar sobreposição
            i=i+1
        else:
            pos=pos+1
        
    return i
    

if __name__ == "__main__":

    maxVetor=100
    vetorMaior=maxVetor*[0]   #definindo tamanho maximo
    subVetor=maxVetor*[0]     #definindo tamanho maximo
    vetorAchados=maxVetor*[0] #definindo tamanho maximo
    n=0 #definindo numero de elementos válidos do vetor maior (ocupação)
    m=0 #definindo numero de elementos válidos do subvetor
    nAchados=0 #definindo numero de subvetores achados

    print("\nPrograma para Localizar, Deletar e Substituir SubVetores:")
    
    resp=True
    while resp==True:    

        opcao=int(input("\nDigite uma opcao:"\
                        "\n<1>Definir Vetor"\
                        "\n<2>Definir Subvetor"\
                        "\n<3>Mostrar Vetores"\
                        "\n<4>Localizar Ocorrencias do Subvetor"\
                        "\n<5>Deletar Todas Ocorrências do Subvetor"\
                        "\n<6>Substituir Todas as Ocorrências do Subvetor"\
                        "\n<7>sair"\
                        "\n=> "))
        match opcao:
            case 1:
                n=int(input("\nDigite o tamanho do vetor => "))
                if n<1:
                    print("\nTamanho Inválido!")
                else:
                    geraVetor(vetorMaior,n)
                    print("\nVetor Gerado!")
                     
            case 2:
                m=int(input("\nQual o tamanho do subvetor? => "))
                if m<1 or m>n:
                    print("\nTamanho Inválido!")
                else:
                    subVetor=m*[0]
                    print("\nDigite os elementos:")
                    for i in range(m):
                        subVetor[i]=int(input(f"\nDigite o elemento {i} = "))
                        
            case 3:
                mostraVetor("Vetor Maior",vetorMaior,n)
                mostraVetor("SubVetor",subVetor,m)
                mostraVetor("Vetor de Achados",vetorAchados,nAchados)
                
            case 4:
                if (n<=0)or(m<=0)or(n<m):
                    print("\nDados Incompletos: Redefina Vetor e/ou Subvetor!")
                else:
                    nAchados=localizaSubvetor(vetorMaior,n,subVetor,m)
                    if (nAchados==0):
                        print("\nNenhuma ocorrencia encontrada!")
                    else:
                        print(f"\nOcorrencias encontradas = {nAchados}")
            case 5:
                if (nAchados==0):
                    print("\nNão ha ocorrencias registradas!") 
                else:
                    while (nAchados>0):
                        pos=vetorAchados[nAchados-1]
                        n=deletaSegmento(vetorMaior, n, pos, m)
                        nAchados=nAchados-1
                        
                    print("\nTodas as ocorrrencias foram deletadas!")
                    
            case 6:
                if (nAchados>0):
                    p=int(input("\nDigite o tamanho do vetor substituto => "))
                    if (p<1) or (n+p>maxVetor):
                        print("\nTamanho Inválido!")
                    else:
                        vetorSubs=p*[0]
                    for i in range(p):
                        vetorSubs[i]=int(input(f"\nDigite o elemento {i} = "))
                        
                    while (nAchados>0):    
                        pos=vetorAchados[nAchados-1]
                        n=substituiSegmento(vetorMaior, n, pos, m, vetorSubs, p)
                        nAchados=nAchados-1
                        
                    print("\nTodas as ocorrencias foram substituidas!")   
                else:
                    print("\nNão ha ocorrencias registradas!")
                    
        
        resp=(opcao!=7)
    
    x=input("\nPressione uma tecla para finalizar: ")
    exit(0)
    
