sentence = "MuFoevIXCZzrpXeRmTssj lYSW U jM"

class Solution(object):
    def isCircularSentence():
        if sentence[0] != sentence[-1]:
            return False
        
        for i,n in enumerate(sentence):
            if n == '':
                if sentence[i-1] != sentence[i+1]:
                    return False
        
        return True





print(Solution.isCircularSentence())