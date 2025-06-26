# text = "Sure! Here is the more formla version"
text = "before was was was, was was is"
pattern = 'was'
lst = text.split()
for i in lst:
    # if i == pattern:
    print(i)
    if pattern in i:
        print(lst.index(i))
        lst[lst.index(i)] = "False"