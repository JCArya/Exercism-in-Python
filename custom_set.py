
class CustomSet:
    # Using list as the structure. Avoiding set functionality altogether
    # Performance not considered that much
    def __init__(self, elements=[]):
        uniq_elems = []
        prev_elem = None
        for elem in sorted(elements):
            if prev_elem is not None and elem == prev_elem:
                continue
            uniq_elems.append(elem)
            prev_elem = elem
        self.elements = uniq_elems
    def isempty(self):
        return len(self.elements) == 0
    def __contains__(self, element):
        return element in self.elements
    def issubset(self, other):
        # "self is subset of other"
        return all(elem in other for elem in self.elements)
    def isdisjoint(self, other):
        # "self and other are disjoint"
        return not any(elem in other for elem in self.elements)
    def __eq__(self, other):
        return len(self) == len(other) and self.issubset(other)
    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)
        
    def intersection(self, other):
        return CustomSet([elem for elem in self.elements 
                          if elem in other.elements]) 
    def __sub__(self, other):
        # Difference op
        # other.elements removed from self.elements
        return CustomSet([elem for elem in self.elements 
                          if elem not in other.elements])
    def __add__(self, other):
        # Union op
        return CustomSet(self.elements + other.elements)
    def __len__(self):
        # added this
        return len(self.elements)
