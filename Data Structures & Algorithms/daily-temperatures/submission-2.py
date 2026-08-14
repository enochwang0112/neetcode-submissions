class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # loop in reverse, remove all elements in the stack that are less than current temp
        result = [0] * len(temperatures)
        stack = [] #indices

        for i in range(len(temperatures) - 1, -1, -1):
            while stack != [] and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            
            if stack != []:
                result[i] = stack[-1] - i
            
            stack.append(i)
        
        return result