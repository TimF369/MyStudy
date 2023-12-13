gc_com = input()    # gc composition
gc_com = gc_com.lower()
g = gc_com.count('g')
c = gc_com.count('c')
print((g + c) / len(gc_com) * 100)
