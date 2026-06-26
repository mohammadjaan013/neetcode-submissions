class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        
        for i in range(len(temperatures)):
            c = 0
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result.append(c)
                    break
                else:
                    c += 1
            if len(result) < (i+1):
                result.append(0)
        return result

        