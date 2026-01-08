### Decomposition



## Modular Design
"""
A design principle: Isolate different parts of a program that address different concerns
A modular component can be developed and tested independently
"""
class Resturant:

    all = []

    def __init__(self, name, stars, reviewers):
        self.name = name
        self.stars = stars
        self.reviewers = reviewers
        Resturant.all.append(self)
    
    def similar(self, k, similarity = reviewed_both):
        """
        Return the k most similar resturants to self
        """
        others = list(Resturant.all)
        others.remove(self)
        return sorted(others, key = lambda r: -r.similarity(self, r))[:k]

    def __repr__(self):
        return '<' + self.name + '>'

def reviewed_both(r, s):
    return len([x for x in r.reviewers if x in s.reviewers])

def search(query, ranking = lambda r: -r.stars):
    results = [r for r in Resturant.all if query in r.name]
    return sorted(results, key = ranking)

r1 = Resturant('Thai Delight', 2)
r2 = Resturant('Thai Basil', 3)
r3 = Resturant('Top Dog', 5)

res = search('Thai')
for r in res:
    print(r, 'shares reviewers with', r.similar(3))


## Linear-Time Intersection of Sorted Lists
def fast_overlap(s, t):
    """
    Return the overlap beteween sorted s and t
    """
    i, j, count = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
            count += 1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    return count