class LogSystem:

    def __init__(self):
        self.__logs = []
        self.__gra = {'Year': 4, 'Month': 7, 'Day': 10, \
                              'Hour': 13, 'Minute': 16, 'Second': 19}
        
        

    def put(self, id: int, timestamp: str) -> None:
        self.__logs.append((id, timestamp))

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        i = self.__gra[gra]
        begin = s[:i]
        end = e[:i]
        return sorted(id for id, timestamp in self.__logs \
                      if begin <= timestamp[:i] <= end)
        

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)