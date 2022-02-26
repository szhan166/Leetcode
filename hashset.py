class MyHashSet(object):  
    def __init__(self):
        self.hashCodeRange = 71993
        self.data = [None] * self.hashCodeRange

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.contains(key): 
            hc = self.hashCode(key)
            if self.data[hc] is None:
                self.data[hc] = []
            # till here, self.data[hc] = [] or [3, 3]
            self.data[hc].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            hc = self.hashCode(key)
            currentList = self.data[hc]
            currentList.remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        hc = self.hashCode[key]
        currentList = self.data[hc]
        if currentList is None:
            return False
        else: 
            for v in currentList:
                if v == key:
                    return True
            return False
        
    def hashCode(self, key):
        # map from key to a limit range hashCode 0-71992
        return key%self.hashCodeRange


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)