from advent.load import read_input

*replacement_strings, molecule = read_input()
molecules: set[str] = set()
replacements = {}

for item in replacement_strings:
    original, replacement = item.split(" => ")
    replacements[replacement] = original
    original_len = len(original)

    for i in range(len(molecule)):
        if molecule[i : i + original_len] == original:
            molecules.add(molecule[:i] + replacement + molecule[i + original_len :])

print(len(molecules))
steps = 0

while molecule != "e":
    for replacement, original in replacements.items():
        if replacement in molecule:
            steps += molecule.count(replacement)
            molecule = molecule.replace(replacement, original)

print(steps)
