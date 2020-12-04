from itertools import groupby
from pathlib import Path
from string import hexdigits

lines = (Path(__file__).parent / "day04.txt").read_text().splitlines()
passports_lines = [list(g) for k, g in groupby(lines, key=bool) if k]

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
hexdigits = frozenset(hexdigits)
eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

passports = []
passport = {}

for passport_lines in passports_lines:
    for line in passport_lines:
        for item in line.split():
            key, _, value = item.partition(":")
            passport[key] = value

    passports.append(passport)
    passport = {}

valid_basic = 0
valid = 0

for passport in passports:
    if required_fields - passport.keys():
        continue

    valid_basic += 1

    try:
        byr = int(passport["byr"])
    except ValueError:
        continue
    else:
        if byr < 1920 or byr > 2002:
            continue

    try:
        iyr = int(passport["iyr"])
    except ValueError:
        continue
    else:
        if iyr < 2010 or iyr > 2020:
            continue

    try:
        eyr = int(passport["eyr"])
    except ValueError:
        continue
    else:
        if eyr < 2020 or eyr > 2030:
            continue

    hgt_str, unit = passport["hgt"][:-2], passport["hgt"][-2:]

    try:
        hgt = int(hgt_str)
    except ValueError:
        continue
    else:
        if unit == "cm":
            if hgt < 150 or hgt > 193:
                continue
        else:
            if hgt < 59 or hgt > 76:
                continue

    hcl = passport["hcl"]

    if len(hcl) != 7 or hcl[0] != "#" or set(hcl[1:]) - hexdigits:
        continue

    if passport["ecl"] not in eye_colors:
        continue

    pid: str = passport["pid"]

    if len(pid) != 9 or not pid.isdigit():
        continue

    valid += 1

print(valid_basic)
print(valid)
