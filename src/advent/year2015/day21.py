import itertools

weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]
armor = [
    None,
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
]
rings = [
    (None, None),
    *itertools.combinations(
        [
            None,
            (25, 1, 0),
            (50, 2, 0),
            (100, 3, 0),
            (20, 0, 1),
            (40, 0, 2),
            (80, 0, 3),
        ],
        2,
    ),
]

stats = set()

for w, a, (r1, r2) in itertools.product(weapons, armor, rings):
    cost = 0
    damage = 0
    armor = 0

    for e in (w, a, r1, r2):
        if e is not None:
            cost += e[0]
            damage += e[1]
            armor += e[2]

    stats.add((cost, damage, armor))

boss_hp = 109
boss_damage = 8
boss_armor = 2

outcomes = []

for cost, damage, armor in sorted(stats, key=lambda x: x[0]):
    player_attack = max(1, damage - boss_armor)
    boss_attack = max(1, boss_damage - armor)
    player_hits = 100 // boss_attack + (100 % boss_attack > 0)
    boss_hits = boss_hp // player_attack + (boss_hp % player_attack > 0)
    outcomes.append((cost, boss_hits <= player_hits))

print(next(c for c, w in outcomes if w))
print(next(c for c, w in reversed(outcomes) if not w))
