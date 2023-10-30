from heapq import heappush, heapreplace

class Solution:
    def scheduleCourse(self, curso: List[List[int]]) -> int:
        heap = []
        dia = 0 

        for duracao, deadline in sorted(curso, key=lambda a: (a[-1], a[0])):
            if duracao > deadline:
                continue

            if dia + duracao > deadline:
                maior_duracao = -heap[0]

                if duracao > maior_duracao:
                    continue
                heapreplace(heap, -duracao)
                dia = dia - maior_duracao + duracao
            else:
                heappush(heap, -duracao)
                dia += duracao

        return len(heap)  