import random
import time
import statistics


def insertion_sort(vetor):
    movimentacoes = 0

    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1

        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            movimentacoes += 1
            j -= 1

        vetor[j + 1] = chave
        movimentacoes += 1

    return movimentacoes


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

        movimentacoes = insertion_sort(vetor)

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