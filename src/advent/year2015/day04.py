from hashlib import md5
from itertools import count


def mine(secret, start=1, size=5):
    check = "0" * size

    for i in count(start):
        prefix = md5(secret + str(i).encode("ascii")).hexdigest()[:size]

        if prefix == check:
            return i


p1 = mine(b"ckczppom")
print(p1)
print(mine(b"ckczppom", p1 + 1, 6))
