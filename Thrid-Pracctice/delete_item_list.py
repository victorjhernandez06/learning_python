items = ['A','B','C','D','E']

new_items = []

for item in items:
    if item == 'B':
        continue
    else:
        print(item)
        new_items.append(item)
# A
# C
# D
# E

