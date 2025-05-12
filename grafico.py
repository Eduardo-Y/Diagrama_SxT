import matplotlib.pyplot as plt
lista_de_parametros = [20]

class Corpo():
    def __init__(self, velocidade, Ponto_inicial, name='Objeto'):
        self.velocidade = velocidade
        self.Ponto_inicial = Ponto_inicial
        self.name = name


    def veloc(self):
        return self.velocidade
    

    def P0(self):
        return self.Ponto_inicial
    

    def __str__(self):
        return self.name
    

    def ponto_de_encontro(self, outro, t=10, c1=0, c2=0):
        V1 = self.velocidade
        V2 = outro.velocidade
        P1 = self.Ponto_inicial
        P2 = outro.Ponto_inicial

        xt = V1 + (V2 * (-1))
        xp = P2 + (P1 * (-1))

        if xp == 0 or xt == 0:
            tempo = 0
        else:
            tempo = xp / xt
        
        posicao = P1 + (V1 * tempo)
        resultado = (f'o {c1}º {self.name} ira colidir com o {c2}º {outro.name} no tempo:{tempo:.2f} na posição:{posicao:.2f}')

        if tempo <= 0 or tempo > t:
            return (0, f'nenhum {self.name} ira se colidir')
        else:
            return (posicao,resultado)

def diagrama_SxT(tempo, corpos):
    # tempo = float(input('digite o Tempo valor:'))
    lista_de_corpos = []
    enumeracao = []
    cores = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    PEs = []

    # define a posição inicial e a velocidade de cada corpo
    for numero in range(0, len(corpos)):
        So = corpos[numero].P0()
        v = corpos[numero].veloc()

        lista_de_corpos.append(corpos[numero])
        enumeracao.append(numero+1)

        posicao_final = So+(tempo*v)

        plt.plot([0, tempo],[So, posicao_final], c=cores[numero], marker='o', label=f'{numero+1}º {lista_de_corpos[numero].name}')

        plt.axhline(posicao_final, c='black', ls=':')

        # if posicao_final > So:
        #     diferenca = posicao_final - So
        # elif So > posicao_final:
        #     diferenca = So - posicao_final

        # if diferenca < 0:
        #     diferenca *= (-1)

        # if lista_de_parametros[0] < diferenca:
        #     lista_de_parametros[0] = diferenca

    
    tam = len(lista_de_corpos)

    for i in range(0, tam):
        PE = corpos[numero].ponto_de_encontro(lista_de_corpos[i-1], t=tempo, c1=i+1, c2=enumeracao[i-1])
        formatado = float(f'{PE[0]:.2f}')

        if formatado in PEs:
            continue
        else:
            PEs.append(formatado)
            plt.axhline(PE[0], c='red', ls='-.')
            print(PE[1])


    # define o tamanho do eixo X e Y
    # pr = lista_de_parametros[0]
    # plt.axis([-0.5, tempo*1.1, pr*-1.5, pr*1.5])
    
    # Personalização do gráfico (título, X do ponto 0, grade, legenda dos eixos)
    plt.title('Diagrama SxT')
    plt.axhline(0, c='black')
    plt.axvline(0, c='black')
    plt.grid(True)
    plt.ylabel('Posição (So)')
    plt.xlabel('Posição (t)')
    plt.legend(loc='best')
    plt.savefig('grafico')
    plt.show()

if __name__ == '__main__':
    aviao_1 = Corpo(100, 79, name='Avião')
    aviao_2 = Corpo(50, 20, name='Avião')

    diagrama_SxT(8, (aviao_1, aviao_2))