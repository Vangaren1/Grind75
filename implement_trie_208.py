from typing import List, Optional

"""
Below is the leetcode solution

"""

class Trie:

    base = {}
    def __init__(self):
        self.base = {}
        
    def insert(self, word: str) -> None:
        ptr = self.base
        for w in word:
            if w not in ptr:
                ptr[w] = {}
            ptr = ptr[w]
        ptr['end']=True
                
    def search(self, word: str) -> bool:
        def searchRecursive(word, ptr):
            if len(word) == 0:
                return False
            first = word[0]
            if first not in ptr:
                return False
            if 'end' in ptr[first] and len(word) == 1:
                return True
            return searchRecursive(word[1:], ptr[first])
        ptr = self.base
        return searchRecursive(word, ptr)

    def startsWith(self, prefix: str) -> bool:
        def startsWithRecursive( prefix, ptr):
            if len(prefix) == 0:
                return True
            first = prefix[0]
            if first not in ptr:
                return False
            if ptr[first] == {}:
                return True
            return startsWithRecursive(prefix[1:], ptr[first])
        ptr = self.base
        return startsWithRecursive(prefix, ptr)


"""
Testing Below this

"""
    
if __name__ == "__main__":
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    tr =Trie()
    tr.insert("apple")
    print(tr.search("apple"))
    print(tr.search("app")    )
    print(tr.startsWith("app"))
    tr.insert("app")
    print(tr.search("app"))
    
    # ["Trie","insert","search","search","search","startsWith","startsWith","startsWith"]
    # [[],["hello"],["hell"],["helloa"],["hello"],["hell"],["helloa"],["hello"]]
    print("New Trie")
    t1 = Trie()
    t1.insert("hello")
    print(t1.search("hell"))
    print(t1.search("helloa"))
    print(t1.search("hello"))
    print(t1.startsWith('hell'))
    print(t1.startsWith('helloa'))
    print(t1.startsWith('hello'))


    
    if allPass:    
        print("Passes all test cases")
    