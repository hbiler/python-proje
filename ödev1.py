a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]


b = []
def flatten(a):
    ## a = [input()]
    for i in a:
        if type(i) == list:
            flatten(i)
        else:
            b.append(i)

flatten(a)
print(b)