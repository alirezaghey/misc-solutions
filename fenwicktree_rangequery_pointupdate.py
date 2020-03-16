# A Fenwick Tree (range query point update) implementation
#
#
# Author: Alireza Ghey

from typing import List

class FenwickTreeRangeQueryPointUpdate:
    
    def __init__(self, size: int, values: List[int]=None) -> int:
        """
        Initializes the Fenwick Tree
        size: if values is None, creates an empty tree of this size
        values: constructs a Fenwick Tree based on these values
        The values parameter MUST BE 1-BASED. Value at index 0 is ignored.
        values are copied and are not changed
        O(n) construction
        """
        self.tree = [el for el in values] if values else ([0] * (size + 1))
        self.size = (len(values)) if values else (size + 1)

        if values:
            for i in range(1, self.size):
                parent = i + self._lsb(i)
                if parent < self.size:
                    self.tree[parent] += self.tree[i]
        
    
    def _lsb(self, i : int) -> int:
        """
        Isolates the lowest set bit
        Examples:
        _lsb(108) = _lsb(0b1101100) = 0b100 = 4
        _lsb(104) = _lsb(0b1101000) = 0b1000 = 8
        _lsb(96) = _lsb(0b1100000) = 0b100000 = 32
        _lsb(64) = _lsb(0b1000000) = 0b1000000 = 64
        """

        return i & -i

    def _prefix_sum(self, i: int) -> int:
        """
        Calculates the prefix sum from [1, i], inclusive, in O(log n)
        i is one-based
        """
        pref_sum = 0
        while i > 0:
            pref_sum += self.tree[i]
            i &= ~self._lsb(i) # Equivalent to i -= _lsb(i)
        
        return pref_sum
    
    def range_sum(self, left: int, right: int) -> int:
        """
        Returns the sum of the interval [left, right], inclusive, in O(log n)
        left and right are 1-based
        """
        if right < left:
            raise ValueError("Right needs to be >= left")
        return self._prefix_sum(right) - self._prefix_sum(left - 1)

    def get(self, i: int) -> int:
        """
        Get the value at index i
        """
        return self.range_sum(i, i)
    

    def add(self, i: int, v: int) -> None:
        """
        Add 'v' to index 'i', O(log n)
        """
        while i < self.size:
            self.tree[i] += v
            i += self._lsb(i)
    
    def set(self, i: int, v: int) -> None:
        """
        Set index 'i' to the value 'v', O(log n)
        """
        self.add(i, v - self.range_sum(i, i))

    def __str__(self) -> str:
        return "[" + ", ".join(self.tree) + "]"