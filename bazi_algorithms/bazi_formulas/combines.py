import collections


def count_earth_six_harmony_combine(natal_earth, external_earth):
    count = 0
    natal_d = dict(collections.Counter(natal_earth))
    external_d = dict(collections.Counter(external_earth))

    breakdown = []
    if "Yin" in natal_d and "Hai" in external_d:
        breakdown.append("Natal Yin Combines with External Hai: x" + str(natal_d["Yin"] * external_d["Hai"]))
        count += natal_d["Yin"] * external_d["Hai"]
    if "Hai" in natal_d and "Yin" in external_d:
        breakdown.append("Natal Hai Combines with External Yin: x" + str(natal_d["Hai"] * external_d["Yin"]))
        count += natal_d["Hai"] * external_d["Yin"]

    if "Mao" in natal_d and "Xu" in external_d:
        breakdown.append("Natal Mao Combines with External Xu: x" + str(natal_d["Mao"] * external_d["Xu"]))
        count += natal_d["Mao"] * external_d["Xu"]
    if "Xu" in natal_d and "Mao" in external_d:
        breakdown.append("Natal Xu Combines with External Mao: x" + str(natal_d["Xu"] * external_d["Mao"]))
        count += natal_d["Xu"] * external_d["Mao"]

    if "Chen" in natal_d and "You" in external_d:
        breakdown.append("Natal Chen Combines with External You: x" + str(natal_d["Chen"] * external_d["You"]))
        count += natal_d["Chen"] * external_d["You"]
    if "You" in natal_d and "Chen" in external_d:
        breakdown.append("Natal You Combines with External Chen: x" + str(natal_d["You"] * external_d["Chen"]))
        count += natal_d["You"] * external_d["Chen"]

    if "Si" in natal_d and "Shen" in external_d:
        breakdown.append("Natal Si Combines with External Shen: x" + str(natal_d["Si"] * external_d["Shen"]))
        count += natal_d["Si"] * external_d["Shen"]
    if "Shen" in natal_d and "Si" in external_d:
        breakdown.append("Natal Shen Combines with External Si: x" + str(natal_d["Shen"] * external_d["Si"]))
        count += natal_d["Shen"] * external_d["Si"]

    return count, breakdown


def count_stem_combine(natal_stem, external_stem):
    count = 0
    natal_d = dict(collections.Counter(natal_stem))
    external_d = dict(collections.Counter(external_stem))
    breakdown = []
    if "Jia" in natal_d and "Ji" in external_d:
        breakdown.append("Natal Jia Combines with External Ji: x" + str(natal_d["Jia"] * external_d["Ji"]))
        count += natal_d["Jia"] * external_d["Ji"]
    if "Ji" in natal_d and "Jia" in external_d:
        breakdown.append("Natal Ji Combines with External Jia: x" + str(natal_d["Ji"] * external_d["Jia"]))
        count += natal_d["Ji"] * external_d["Jia"]

    if "Yi" in natal_d and "Geng" in external_d:
        breakdown.append("Natal Yi Combines with External Geng: x" + str(natal_d["Yi"] * external_d["Geng"]))
        count += natal_d["Yi"] * external_d["Geng"]
    if "Geng" in natal_d and "Yi" in external_d:
        breakdown.append("Natal Geng Combines with External Yi: x" + str(natal_d["Geng"] * external_d["Yi"]))
        count += natal_d["Geng"] * external_d["Yi"]

    if "Bing" in natal_d and "Xin" in external_d:
        breakdown.append("Natal Bing Combines with External Xin: x" + str(natal_d["Bing"] * external_d["Xin"]))
        count += natal_d["Bing"] * external_d["Xin"]
    if "Xin" in natal_d and "Bing" in external_d:
        breakdown.append("Natal Xin Combines with External Bing: x" + str(natal_d["Xin"] * external_d["Bing"]))
        count += natal_d["Xin"] * external_d["Bing"]

    if "Ding" in natal_d and "Ren" in external_d:
        breakdown.append("Natal Ding Combines with External Ren: x" + str(natal_d["Ding"] * external_d["Ren"]))
        count += natal_d["Ding"] * external_d["Ren"]
    if "Ren" in natal_d and "Ding" in external_d:
        breakdown.append("Natal Ren Combines with External Ding: x" + str(natal_d["Ren"] * external_d["Ding"]))
        count += natal_d["Ren"] * external_d["Ding"]

    if "Wu" in natal_d and "Gui" in external_d:
        breakdown.append("Natal Wu Combines with External Gui: x" + str(natal_d["Wu"] * external_d["Gui"]))
        count += natal_d["Wu"] * external_d["Gui"]
    if "Gui" in natal_d and "Wu" in external_d:
        breakdown.append("Natal Gui Combines with External Wu: x" + str(natal_d["Gui"] * external_d["Wu"]))
        count += natal_d["Gui"] * external_d["Wu"]

    return count, breakdown


def count_earth_combo(natal_earth, external_earth):
    count = 0
    ymc_count = 0
    sww_count = 0
    syx_count = 0
    hzc_count = 0
    szc_count = 0
    hmw_count = 0
    ywx_count = 0
    syc_count = 0
    breakdown_1 = []
    breakdown_2 = []
    breakdown_3 = []
    breakdown_4 = []
    breakdown_5 = []
    breakdown_6 = []
    breakdown_7 = []
    breakdown_8 = []
    breakdown_9 = []
    breakdown_10 = []
    breakdown_11 = []
    breakdown_12 = []
    breakdown_13 = []
    breakdown_14 = []
    breakdown_15 = []
    breakdown_16 = []

    s = set(natal_earth + external_earth)

    if "Yin" in s and "Mao" in s and "Chen" in s:
        ymc_count, breakdown_1 = earth_full_combo_finder(natal_earth, external_earth, ["Yin", "Mao", "Chen"])
    if ymc_count == 0:
        count, breakdown_2 = earth_two_third_combo_finder(natal_earth, external_earth, ["Yin", "Mao", "Chen"])

    if "Si" in s and "Wu" in s and "Wei" in s:
        sww_count, breakdown_3 = earth_full_combo_finder(natal_earth, external_earth, ["Si", "Wu", "Wei"])
    if sww_count == 0:
        count, breakdown_4 = earth_two_third_combo_finder(natal_earth, external_earth, ["Si", "Wu", "Wei"])

    if "Shen" in s and "You" in s and "Xu" in s:
        syx_count, breakdown_5 = earth_full_combo_finder(natal_earth, external_earth, ["Shen", "You", "Xu"])
    if syx_count == 0:
        count, breakdown_6 = earth_two_third_combo_finder(natal_earth, external_earth, ["Shen", "You", "Xu"])

    if "Hai" in s and "Zi" in s and "Chou" in s:
        hzc_count, breakdown_7 = earth_full_combo_finder(natal_earth, external_earth, ["Hai", "Zi", "Chou"])
    if hzc_count == 0:
        count, breakdown_8 = earth_two_third_combo_finder(natal_earth, external_earth, ["Hai", "Zi", "Chou"])

    if "Shen" in s and "Zi" in s and "Chen" in s:
        szc_count, breakdown_9 = earth_full_combo_finder(natal_earth, external_earth, ["Shen", "Zi", "Chen"])
    if szc_count == 0:
        count, breakdown_10 = earth_two_third_combo_finder(natal_earth, external_earth, ["Shen", "Zi", "Chen"])

    if "Hai" in s and "Mao" in s and "Wei" in s:
        hmw_count, breakdown_11 = earth_full_combo_finder(natal_earth, external_earth, ["Hai", "Mao", "Wei"])
    if hmw_count == 0:
        count, breakdown_12 = earth_two_third_combo_finder(natal_earth, external_earth, ["Hai", "Mao", "Wei"])

    if "Yin" in s and "Wu" in s and "Xu" in s:
        ywx_count, breakdown_13 = earth_full_combo_finder(natal_earth, external_earth, ["Yin", "Wu", "Xu"])
    if ywx_count == 0:
        count, breakdown_14 = earth_two_third_combo_finder(natal_earth, external_earth, ["Yin", "Wu", "Xu"])

    if "Si" in s and "Chou" in s and "You" in s:
        syc_count, breakdown_15 = earth_full_combo_finder(natal_earth, external_earth, ["Si", "Chou", "You"])
    if syc_count == 0:
        count, breakdown_16 = earth_two_third_combo_finder(natal_earth, external_earth, ["Si", "Chou", "You"])

    count = count + ymc_count + sww_count + syx_count + hzc_count + szc_count + hmw_count + ywx_count + syc_count
    breakdown = breakdown_1 + breakdown_2 + breakdown_3 + breakdown_4 + breakdown_5 + breakdown_6 + breakdown_7 + breakdown_8 + breakdown_9 + breakdown_10 + breakdown_11 + breakdown_12 + breakdown_13 + breakdown_14 + breakdown_15 + breakdown_16
    return count, breakdown


def earth_full_combo_finder(natal_earth, external_earth, tri):
    natal_d = dict(collections.Counter(natal_earth))
    external_d = dict(collections.Counter(external_earth))
    count = 0
    breakdown = []
    if tri[0] in natal_d and tri[1] in natal_d and tri[2] in external_d:
        breakdown.append(f"Natal {tri[0]} and {tri[1]} Combines with External {tri[2]}: x" + str(
            3 * natal_d[tri[0]] * natal_d[tri[1]] * external_d[tri[2]]))
        count += 3 * (natal_d[tri[0]] * natal_d[tri[1]] * external_d[tri[2]])
    if tri[1] in natal_d and tri[2] in natal_d and tri[0] in external_d:
        breakdown.append(f"Natal {tri[1]} and {tri[2]} Combines with External {tri[0]}: x" + str(
            3 * natal_d[tri[1]] * natal_d[tri[2]] * external_d[tri[0]]))
        count += 3 * (natal_d[tri[1]] * natal_d[tri[2]] * external_d[tri[0]])
    if tri[2] in natal_d and tri[0] in natal_d and tri[1] in external_d:
        breakdown.append(f"Natal {tri[2]} and {tri[0]} Combines with External {tri[1]}: x" + str(
            3 * natal_d[tri[2]] * natal_d[tri[0]] * external_d[tri[1]]))
        count += 3 * (natal_d[tri[2]] * natal_d[tri[0]] * external_d[tri[1]])

    if tri[0] in external_d and tri[1] in external_d and tri[2] in natal_d:
        breakdown.append(f"Natal {tri[2]} Combines with External {tri[0]} and {tri[1]}: x" + str(
            3 * natal_d[tri[2]] * external_d[tri[0]] * external_d[tri[1]]))
        count += 3 * (external_d[tri[0]] * external_d[tri[1]] * natal_d[tri[2]])
    if tri[1] in external_d and tri[2] in external_d and tri[0] in natal_d:
        breakdown.append(f"Natal {tri[0]} Combines with External {tri[1]} and {tri[2]}: x" + str(
            3 * natal_d[tri[0]] * external_d[tri[1]] * external_d[tri[2]]))
        count += 3 * (external_d[tri[1]] * external_d[tri[2]] * natal_d[tri[0]])
    if tri[2] in external_d and tri[0] in external_d and tri[1] in natal_d:
        breakdown.append(f"Natal {tri[1]} Combines with External {tri[2]} and {tri[0]}: x" + str(
            3 * natal_d[tri[1]] * external_d[tri[2]] * external_d[tri[0]]))
        count += 3 * (external_d[tri[2]] * external_d[tri[0]] * natal_d[tri[1]])
    return count, breakdown


def earth_two_third_combo_finder(natal_earth, external_earth, tri):
    natal_d = dict(collections.Counter(natal_earth))
    external_d = dict(collections.Counter(external_earth))
    count = 0
    breakdown = []
    if tri[0] in natal_d and tri[1] in external_d:
        breakdown.append(
            f"Natal {tri[0]} Combines with External {tri[1]}: x" + str(natal_d[tri[0]] * external_d[tri[1]]))
        count += natal_d[tri[0]] * external_d[tri[1]]
    if tri[1] in natal_d and tri[2] in external_d:
        breakdown.append(
            f"Natal {tri[1]} Combines with External {tri[2]}: x" + str(natal_d[tri[1]] * external_d[tri[2]]))
        count += natal_d[tri[1]] * external_d[tri[2]]
    if tri[2] in natal_d and tri[0] in external_d:
        breakdown.append(
            f"Natal {tri[2]} Combines with External {tri[0]}: x" + str(natal_d[tri[2]] * external_d[tri[0]]))
        count += natal_d[tri[2]] * external_d[tri[0]]
    if tri[0] in natal_d and tri[2] in external_d:
        breakdown.append(
            f"Natal {tri[0]} Combines with External {tri[2]}: x" + str(natal_d[tri[0]] * external_d[tri[2]]))
        count += natal_d[tri[0]] * external_d[tri[2]]
    if tri[1] in natal_d and tri[0] in external_d:
        breakdown.append(
            f"Natal {tri[1]} Combines with External {tri[0]}: x" + str(natal_d[tri[1]] * external_d[tri[0]]))
        count += natal_d[tri[1]] * external_d[tri[0]]
    if tri[2] in natal_d and tri[1] in external_d:
        breakdown.append(
            f"Natal {tri[2]} Combines with External {tri[1]}: x" + str(natal_d[tri[2]] * external_d[tri[1]]))
        count += natal_d[tri[2]] * external_d[tri[1]]

    return count, breakdown
