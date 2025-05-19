class Set:
    def __init__(self):
        self._elements = []

    def add(self, element):
        # add element in list if it doesn't exist already
        if element not in self._elements:
            self._elements.append(element)

    def remove(self, element):
        # remove element if it's a duplicate
        if element in self._elements:
            self._elements.remove(element)

    def contains(self, element):
        # return true if the elements list contains the element, return false if otherwise
        return element in self._elements

    def union(self, otherSet):
        # create set to hold union values
        unionSet = Set()
        for elem in self._elements:
            unionSet.add(elem)
        for elem in otherSet._elements:
            unionSet.add(elem)
        return unionSet

    def intersection(self, otherSet):
        # create set to hold intersection values 
        intersectionSet = Set()
        for elem in self._elements:
            if otherSet.contains(elem):
                intersectionSet.add(elem)
        return intersectionSet

    def difference(self, otherSet):
        # create set to hold unique values 
        uniqueSet = Set()
        for elem in self._elements:
            if not otherSet.contains(elem):
                uniqueSet.add(elem)
        return uniqueSet
