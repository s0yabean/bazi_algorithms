import collections

def count_earth_destroy(natal_earth, external_earth):
    count = 0
    natal_d = dict(collections.Counter(natal_earth))
    external_d = dict(collections.Counter(external_earth))
    breakdown = []
    
    for pair in [["Zi", "You"], ["Shen", "Si"], ["Chen", "Chou"], ["Wu", "Mao"], ["Yin", "Hai"], ["Xu", "Wei"]]:
        if pair[0] in natal_d and pair[1] in external_d:
            breakdown.append(f"Natal {pair[0]} Destroys with External {pair[1]}: x{str(natal_d[pair[0]] * external_d[pair[1]])}")
            count+=natal_d[pair[0]] * external_d[pair[1]]
        if pair[1] in natal_d and pair[0] in external_d:
            breakdown.append(f"Natal {pair[1]} Destroys with External {pair[0]}: x{str(natal_d[pair[1]] * external_d[pair[0]])}")
            count+=natal_d[pair[1]] * external_d[pair[0]]
    return count, breakdown