########################################################################################################################
### Data Structures and Algorithms :: Section 07
### Exercise: Implement A Hash Table
########################################################################################################################

### imports
from typing import List, Any

########################################################################################################################### HashTable Class
########################################################################################################################

class HashTable:
    """
    Implements a basic hash table data structure.

    Attributes:
    - pData : List[List[str,Any]], internal storage for hash table data

    Methods:
    - __init__(initSize=10), initializes the hash table with specified size
    - _hash(hashKey=str()), computes the hash table index for a given key
    - set(setKey=str(), setValue=None), inserts a key/value pair into the hash table
    - get(getKey=str()), retrieves the value associated with a given key
    """

    ### constructor method #############################################################################################
    def __init__(self, initSize=10) -> None:
        """
        Args:
        - initSize : int, size of hash table, defaults to 10

        Validates the provided initSize, defaults to 10 if invalid.
        
        Fills the hash table with empty buckets.

        Returns:
        - None
        """

        ### verifying input --------------------------------------------------------------------------------------------

        if type(initSize) is not int or initSize <= 0: initSize = 10

        ### main logic -------------------------------------------------------------------------------------------------

        self.pData = [[] for _ in range(initSize)]
        return
    
    ### private hash method ############################################################################################
    def _hash(self, hashKey=str()) -> int:
        """
        Args:
        - hashKey : str, key to be hashed, defaults to empty string

        Validates the provided hashKey.

        Raises:
        - Exception, if hashKey is invalid

        Hashes the provided hashKey into a hash table index (rHash).

        Returns:
        - rHash : int, hash table index
        """

        ### verifying input --------------------------------------------------------------------------------------------

        if type(hashKey) is not str or len(hashKey) == 0:
            raise Exception(f"Key '{hashKey}' is not valid...\n")
        
        ### main logic -------------------------------------------------------------------------------------------------

        rHash = int()
        for index in range(len(hashKey)):
            rHash = (rHash + ord(hashKey[index]) * index) % len(self.pData)
        return rHash
    
    ### set method #####################################################################################################
    def set(self, setKey=str(), setValue=None) -> None:
        """
        Args:
        - setKey : str, key to be set, defaults to empty string
        - setValue : Any, value to be set, defaults to None

        Sets a key/value (setKey/setValue) pair in the hash table.

        Returns:
        - None
        """

        self.pData[self._hash(hashKey=setKey)].append([setKey, setValue])
        print("\n", self.pData)
        return
    
    ### get method #####################################################################################################
    def get(self, getKey=str()) -> Any:
        """
        Args:
        - getKey : str, key to be searched, defaults to empty string

        Finds a value in the hash table identified by getKey.

        Returns:
        - Any, value found in hash table

        Raises:
        - Exception, if getKey is not found
        """

        for item in self.pData[self._hash(hashKey=getKey)]:
            if item[0] == getKey: return item[1]
        raise Exception(f"Key '{getKey}' is not found...\n")
    
    ### keys method ####################################################################################################
    def keys(self) -> List[str]:
        """
        Retrieves all keys from the hash table to create a list of keys (rKeys).

        Returns:
        - rKeys : List[str], list of keys in the hash table
        """

        rKeys: List[str] = list()
        for bucket in self.pData:
            for item in bucket:
                rKeys.append(item[0])
        return rKeys

########################################################################################################################
### code tests
########################################################################################################################

myDict = HashTable(initSize=2)
print("\n", myDict._hash(hashKey="cardigans"))
print("\nKeys: ", myDict.keys())
myDict.set(setKey="apple")
myDict.set(setKey="banana", setValue="value2")
myDict.set(setKey="orange", setValue="value3")
myDict.set(setKey="grape", setValue="value4")
myDict.set(setKey="peach", setValue="value5")
print("\nValue of orange: ", myDict.get("orange"))
print("\nKeys: ", myDict.keys())
print()
