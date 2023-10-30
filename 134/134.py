class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        combustivel_restante = 0  
        ponto_partida = 0  
        combustivel_disponivel = 0  
        
        for i in range(len(gas)):
            
            diferenca = gas[i] - cost[i]  
            combustivel_disponivel += diferenca  
            combustivel_restante += diferenca  

            if combustivel_restante < 0:
                ponto_partida = i + 1  
                combustivel_restante = 0  
   
        if combustivel_disponivel >= 0:
            return ponto_partida  
        else:
            return -1  

