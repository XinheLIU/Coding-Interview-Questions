class Solution:
    def toHexspeak(self, num: str) -> str:
        num = int(num)
        ret = ''
        while num > 0:
            num, cur = divmod(num, 16)
            if 2 <= cur <= 9: 
                return 'ERROR'
            if cur == 0: 
                ret += 'O'
            elif cur == 1: 
                ret += 'I'
            else:  
                ret += chr(cur - 10 + ord('A') )
        return ret[::-1]