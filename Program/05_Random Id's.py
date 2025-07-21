"""
GENERATING RANDOM ID'S IN PYTHON

** Using random.randint()
** import random
** generate random integers within a specified range.
** this method guarantees that the generated numbers will fall between the given lower and upper bounds
"""

import random
#Generate 10 IDs between 1 an 100
res =  [random.randint(1, 47) for _ in range (5)]
comodin = [random.randint(1,27) for _ in range (1)]
primary = sorted(res)
print(f"Numeros a comprar: {primary}")
print(f"El comodin es: {comodin}")

print()
#->  [5, 78, 35, 48, 57, 19, 41, 14, 65, 42]

"""
USING UUID
if we need globally unique random ID's
"""
import uuid

# Generate 10 UUID random IDs
res = [str(uuid.uuid4()) for _ in range(2)]
print (res)

#-> ['14c726e5-bbb2-4d0a-b0f7-6091471ba970', 'dc971473-7430-4257-8218-3034819a9b01']
