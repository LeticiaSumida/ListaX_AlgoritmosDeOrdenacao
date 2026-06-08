import random
import time
import statistics


def merge_sort(vetor):

    movimentacoes = [0]

    def merge(esquerda, direita):

        resultado = []
        i = j = 0

        while i < len(esquerda) and j < len(direita):

            if esquerda[i] <= direita[j]:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1

            movimentacoes[0] += 1

        while i < len(esquerda):
            resultado.append(esquerda[i])
            movimentacoes[0] += 1
            i += 1

        while j < len(direita):
            resultado.append(direita[j])
            movimentacoes[0] += 1
            j += 1

        return resultado

    def ordenar(v):

        if len(v) <= 1:
            return v

        meio = len(v) // 2

        esquerda = ordenar(v[:meio])
        direita = ordenar(v[meio:])

        return merge(esquerda, direita)

    ordenado = ordenar(vetor)

    for i in range(len(vetor)):
        vetor[i] = ordenado[i]

    return movimentacoes[0]


def testar(tamanho):

    vetor_original = [
        random.randint(0, 100000)
        for _ in range(tamanho)
    ]

    tempos = []
    movimentacoes = 0

    for _ in range(3):
        vetor = vetor_original.copy()

        inicio = time.perf_counter()

        movimentacoes = merge_sort(vetor)

        fim = time.perf_counter()

        tempos.append(fim - inicio)

    print(f"\nTamanho: {tamanho}")
    print(f"Tempo 1: {tempos[0]:.6f}s")
    print(f"Tempo 2: {tempos[1]:.6f}s")
    print(f"Tempo 3: {tempos[2]:.6f}s")
    print(f"Média: {statistics.mean(tempos):.6f}s")
    print(f"Desvio padrão: {statistics.stdev(tempos):.6f}")
    print(f"Movimentações: {movimentacoes}")


for tamanho in [1000, 10000, 100000]:
    testar(tamanho)