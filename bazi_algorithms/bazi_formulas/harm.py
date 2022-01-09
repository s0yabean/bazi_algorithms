import collections


def count_earth_harm(natal_earth, external_earth):
    count = 0
    natal_d = dict(collections.Counter(natal_earth))
    external_d = dict(collections.Counter(external_earth))
    breakdown = []

    for pair in [["Zi", "Wei"], ["Yin", "Si"], ["Shen", "Hai"], ["Chou", "Wu"], ["Mao", "Chen"], ["Xu", "You"]]:
        if pair[0] in natal_d and pair[1] in external_d:
            breakdown.append(
                f"Natal {pair[0]} Harms with External {pair[1]}: x{str(natal_d[pair[0]] * external_d[pair[1]])}")
            count += natal_d[pair[0]] * external_d[pair[1]]
        if pair[1] in natal_d and pair[0] in external_d:
            breakdown.append(
                f"Natal {pair[1]} Harms with External {pair[0]}: x{str(natal_d[pair[1]] * external_d[pair[0]])}")
            count += natal_d[pair[1]] * external_d[pair[0]]
    return count, breakdown
