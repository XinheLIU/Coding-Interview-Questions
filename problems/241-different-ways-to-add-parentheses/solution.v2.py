import operator
class Solution(object):
    def diffWaysToCompute(self, input):
        tokens = re.split('(\D)', input)
        nums = map(int, tokens[::2])
        ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
        
        def build(l, r):
            if l == r:
                return [nums[l]]
            return [ops[i](a, b)
               for i in range(l, r)
               for a in build(l, i)
               for b in build(i + 1, r)]    
        return build(0, len(nums) - 1)
   
'''  
   diffWaysToCompute=d=lambda s,t:[eval(`a`+c+`b`)for i,c in enumerate(t)if
c<'0'for a in s.d(t[:i])for b in s.d(t[i+1:])]or[int(t)]
'''