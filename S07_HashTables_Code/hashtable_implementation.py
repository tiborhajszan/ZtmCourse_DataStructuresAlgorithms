########################################################################################################################
### Data Structures and Algorithms :: Section 07
### Exercise: Implement A Hash Table
########################################################################################################################

### imports
from typing import Any

########################################################################################################################### HashTable Class
########################################################################################################################
class HashTable:

    ### constructor method #############################################################################################
    def __init__(self, size:int=10) -> None:
        if type(size) is not int or size <= 0: size = 10
        self.pData = [[] for _ in range(size)]
        print(self.pData)
        return
    
    def _hash(self, hashKey:str) -> int:
        if type(hashKey) is not str or len(hashKey) == 0: return -1
        hash = 0
        for index in range(len(hashKey)): hash = (hash + ord(hashKey[index]) * index) % len(self.pData)
        return hash
    
    def set(self, setKey:str, setValue:Any) -> Any:
        if type(setKey) is not str or len(setKey) == 0: return
        bucket_address = self._hash(hashKey=setKey)
        if bucket_address < 0: return
        self.pData[bucket_address].append([setKey, setValue])
        print(self.pData)
        return

myDict = HashTable(size=2)
myDict.set(setKey="key1", setValue="value1")
myDict.set(setKey="key2", setValue="value2")
myDict.set(setKey="key3", setValue="value3")
