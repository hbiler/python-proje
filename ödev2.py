l =  [[1, 2], [3, 4], [5, 6, 7]]

# output: [[7, 6, 5], [4, 3], [2, 1]]

def rev_list(l):
    for _ in l:
        if type(_) == list:
            _.reverse()
        l.reverse()
    return l

print(rev_list(l))
