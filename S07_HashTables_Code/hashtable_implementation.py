########################################################################################################################
### Data Structures and Algorithms :: Section 07
### Exercise: Implement A Hash Table
########################################################################################################################

### imports
from typing import Any

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

########################################################################################################################
### code tests
########################################################################################################################

myDict = HashTable(initSize=20)
print("\n", myDict._hash(hashKey="cardigans"))
myDict.set(setKey="key1")
myDict.set(setKey="key2", setValue="value2")
myDict.set(setKey="key3", setValue="value3")
print("\nValue of key1: ", myDict.get("key1"))
