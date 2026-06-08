import random
import time
import statistics


def quick_sort(vetor):

    trocas = [0]

    def particiona(inicio, fim):

        pivo = vetor[fim]
        i = inicio - 1

        for j in range(inicio, fim):

            if vetor[j] <= pivo:

                i += 1

                vetor[i], vetor[j] = vetor[j], vetor[i]

                if i != j:
                    trocas[0] += 1

        vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]

        if i + 1 != fim:
            trocas[0] += 1

        return i + 1

    def ordenar(inicio, fim):

        if inicio < fim:

            p = particiona(inicio, fim)

            ordenar(inicio, p - 1)
            ordenar(p + 1, fim)

    ordenar(0, len(vetor) - 1)

    return trocas[0]


def testar(tamanho):

    vetor_original = [
        random.randint(0, 100000)
        for _ in range(tamanho)
    ]

    tempos = []
    trocas = 0

    for _ in range(3):

        vetor = vetor_original.copy()

        inicio = time.perf_counter()

        trocas = quick_sort(vetor)

        fim = time.perf_counter()

        tempos.append(fim - inicio)

    print(f"\nTamanho: {tamanho}")
    print(f"Tempo 1: {tempos[0]:.6f}s")
    print(f"Tempo 2: {tempos[1]:.6f}s")
    print(f"Tempo 3: {tempos[2]:.6f}s")
    print(f"Média: {statistics.mean(tempos):.6f}s")
    print(f"Desvio padrão: {statistics.stdev(tempos):.6f}")
    print(f"Trocas: {trocas}")


for tamanho in [1000, 10000, 100000]:
    testar(tamanho)