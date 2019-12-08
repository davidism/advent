from itertools import chain

from more_itertools import windowed


def potential_password(value, skip_group=False):
    has_same = False
    group = None

    for x, y, z in windowed(chain(str(value), [None]), 3):
        if x == y == z:
            group = x

        if x == y and (not skip_group or x != group):
            has_same = True

        if y < x:
            return False

    return has_same


potential = [x for x in range(264793, 803935) if potential_password(x)]
print(len(potential))
print(len([x for x in potential if potential_password(x, True)]))
