import collections

def count_earth_uncivil_punish(natal_earth, external_earth):
    count = 0
    natal_d = dict(collections.Counter(natal_earth))
    external_d = dict(collections.Counter(external_earth))
    breakdown = []
    
    for pair in [["Zi", "Mao"]]:
        if pair[0] in natal_d and pair[1] in external_d:
            breakdown.append(f"Natal {pair[0]} Punishes with External {pair[1]}: x{str(natal_d[pair[0]] * external_d[pair[1]])}")
            count+=natal_d[pair[0]] * external_d[pair[1]]
        if pair[1] in natal_d and pair[0] in external_d:
            breakdown.append(f"Natal {pair[1]} Punishes with External {pair[0]}: x{str(natal_d[pair[1]] * external_d[pair[0]])}")
            count+=natal_d[pair[1]] * external_d[pair[0]]
    return count, breakdown

def count_earth_self_punish(natal_earth, external_earth):
    count = 0
    natal_d = dict(collections.Counter(natal_earth))
    external_d = dict(collections.Counter(external_earth))
    breakdown = []
    
    for pair in [["Chen", "Chen"], ["Wu", "Wu"], ["You", "You"], ["Hai", "Hai"]]:
        if pair[0] in natal_d and pair[1] in external_d:
            breakdown.append(f"Natal {pair[0]} Punishes with External {pair[1]}: x{str(natal_d[pair[0]] * external_d[pair[1]])}")
            count+=natal_d[pair[0]] * external_d[pair[1]]
        if pair[1] in natal_d and pair[0] in external_d:
            breakdown.append(f"Natal {pair[1]} Punishes with External {pair[0]}: x{str(natal_d[pair[1]] * external_d[pair[0]])}")
            count+=natal_d[pair[1]] * external_d[pair[0]]
    return count, breakdown

def earth_full_bully_punish_finder(natal_earth, external_earth, tri):
    natal_d = dict(collections.Counter(natal_earth))
    external_d = dict(collections.Counter(external_earth))
    count = 0
    breakdown = []
    if tri[0] in natal_d and tri[1] in natal_d and tri[2] in external_d:
        breakdown.append(f"Natal {tri[0]} and {tri[1]} Bully Punishes with External {tri[2]}: x" + str(3 * natal_d[tri[0]] * natal_d[tri[1]] * external_d[tri[2]]))
        count+=3 * (natal_d[tri[0]] * natal_d[tri[1]] * external_d[tri[2]])
    if tri[1] in natal_d and tri[2] in natal_d and tri[0] in external_d:
        breakdown.append(f"Natal {tri[1]} and {tri[2]} Bully Punishes with External {tri[0]}: x" + str(3 * natal_d[tri[1]] * natal_d[tri[2]] * external_d[tri[0]]))
        count+=3 * (natal_d[tri[1]] * natal_d[tri[2]] * external_d[tri[0]])
    if tri[2] in natal_d and tri[0] in natal_d and tri[1] in external_d:
        breakdown.append(f"Natal {tri[2]} and {tri[0]} Bully Punishes with External {tri[1]}: x" + str(3 * natal_d[tri[2]] * natal_d[tri[0]] * external_d[tri[1]]))
        count+=3 * (natal_d[tri[2]] * natal_d[tri[0]] * external_d[tri[1]])    
    
    if tri[0] in external_d and tri[1] in external_d and tri[2] in natal_d:
        breakdown.append(f"Natal {tri[2]} Bully Punishes with External {tri[0]} and {tri[1]}: x" + str(3 * natal_d[tri[2]] * external_d[tri[0]] * external_d[tri[1]]))
        count+=3 * (external_d[tri[0]] * external_d[tri[1]] * natal_d[tri[2]])
    if tri[1] in external_d and tri[2] in external_d and tri[0] in natal_d:
        breakdown.append(f"Natal {tri[0]} Bully Punishes with External {tri[1]} and {tri[2]}: x" + str(3 * natal_d[tri[0]] * external_d[tri[1]] * external_d[tri[2]]))
        count+=3 * (external_d[tri[1]] * external_d[tri[2]] * natal_d[tri[0]])
    if tri[2] in external_d and tri[0] in external_d and tri[1] in natal_d:
        breakdown.append(f"Natal {tri[1]} Bully Punishes with External {tri[2]} and {tri[0]}: x" + str(3 * natal_d[tri[1]] * external_d[tri[2]] * external_d[tri[0]]))
        count+=3 * (external_d[tri[2]] * external_d[tri[0]] * natal_d[tri[1]])
    return count, breakdown
   
def earth_two_third_bully_punish_finder(natal_earth, external_earth, tri):
    natal_d = dict(collections.Counter(natal_earth))
    external_d = dict(collections.Counter(external_earth))
    count = 0
    breakdown=[]
    if tri[0] in natal_d and tri[1] in external_d:
        breakdown.append(f"Natal {tri[0]} Bully Punishes with External {tri[1]}: x" + str(natal_d[tri[0]] * external_d[tri[1]]))
        count+=natal_d[tri[0]] * external_d[tri[1]]
    if tri[1] in natal_d and tri[2] in external_d:
        breakdown.append(f"Natal {tri[1]} Bully Punishes with External {tri[2]}: x" + str(natal_d[tri[1]] * external_d[tri[2]]))
        count+=natal_d[tri[1]] * external_d[tri[2]]
    if tri[2] in natal_d and tri[0] in external_d:
        breakdown.append(f"Natal {tri[2]} Bully Punishes with External {tri[0]}: x" + str(natal_d[tri[2]] * external_d[tri[0]]))
        count+=natal_d[tri[2]] * external_d[tri[0]]
    if tri[0] in natal_d and tri[2] in external_d:
        breakdown.append(f"Natal {tri[0]} Bully Punishes with External {tri[2]}: x" + str(natal_d[tri[0]] * external_d[tri[2]]))
        count+=natal_d[tri[0]] * external_d[tri[2]]
    if tri[1] in natal_d and tri[0] in external_d:
        breakdown.append(f"Natal {tri[1]} Bully Punishes with External {tri[0]}: x" + str(natal_d[tri[1]] * external_d[tri[0]]))
        count+=natal_d[tri[1]] * external_d[tri[0]]
    if tri[2] in natal_d and tri[1] in external_d:
        breakdown.append(f"Natal {tri[2]} Bully Punishes with External {tri[1]}: x" + str(natal_d[tri[2]] * external_d[tri[1]]))
        count+=natal_d[tri[2]] * external_d[tri[1]]
        
    return count, breakdown

def count_earth_bully_punish(natal_earth, external_earth):
    count = 0
    wcx_count = 0
    breakdown_1 = []
    breakdown_2 = []

    s = set(natal_earth + external_earth)
    
    if "Wei" in s and "Chou" in s and "Xu" in s:
        wcx_count, breakdown_1 = earth_full_bully_punish_finder(natal_earth, external_earth, ["Wei","Chou","Xu"])
    if wcx_count == 0:
        count, breakdown_2 = earth_two_third_bully_punish_finder(natal_earth, external_earth, ["Wei","Chou","Xu"])
        
    count = count + wcx_count
    breakdown = breakdown_1 + breakdown_2
    return count, breakdown

def earth_full_ungrateful_punish_finder(natal_earth, external_earth, tri):
    natal_d = dict(collections.Counter(natal_earth))
    external_d = dict(collections.Counter(external_earth))
    count = 0
    breakdown = []
    if tri[0] in natal_d and tri[1] in natal_d and tri[2] in external_d:
        breakdown.append(f"Natal {tri[0]} and {tri[1]} Ungrateful Punishes with External {tri[2]}: x" + str(3 * natal_d[tri[0]] * natal_d[tri[1]] * external_d[tri[2]]))
        count+=3 * (natal_d[tri[0]] * natal_d[tri[1]] * external_d[tri[2]])
    if tri[1] in natal_d and tri[2] in natal_d and tri[0] in external_d:
        breakdown.append(f"Natal {tri[1]} and {tri[2]} Ungrateful Punishes with External {tri[0]}: x" + str(3 * natal_d[tri[1]] * natal_d[tri[2]] * external_d[tri[0]]))
        count+=3 * (natal_d[tri[1]] * natal_d[tri[2]] * external_d[tri[0]])
    if tri[2] in natal_d and tri[0] in natal_d and tri[1] in external_d:
        breakdown.append(f"Natal {tri[2]} and {tri[0]} Ungrateful Punishes with External {tri[1]}: x" + str(3 * natal_d[tri[2]] * natal_d[tri[0]] * external_d[tri[1]]))
        count+=3 * (natal_d[tri[2]] * natal_d[tri[0]] * external_d[tri[1]])    
    
    if tri[0] in external_d and tri[1] in external_d and tri[2] in natal_d:
        breakdown.append(f"Natal {tri[2]} Ungrateful Punishes with External {tri[0]} and {tri[1]}: x" + str(3 * natal_d[tri[2]] * external_d[tri[0]] * external_d[tri[1]]))
        count+=3 * (external_d[tri[0]] * external_d[tri[1]] * natal_d[tri[2]])
    if tri[1] in external_d and tri[2] in external_d and tri[0] in natal_d:
        breakdown.append(f"Natal {tri[0]} Ungrateful Punishes with External {tri[1]} and {tri[2]}: x" + str(3 * natal_d[tri[0]] * external_d[tri[1]] * external_d[tri[2]]))
        count+=3 * (external_d[tri[1]] * external_d[tri[2]] * natal_d[tri[0]])
    if tri[2] in external_d and tri[0] in external_d and tri[1] in natal_d:
        breakdown.append(f"Natal {tri[1]} Ungrateful Punishes with External {tri[2]} and {tri[0]}: x" + str(3 * natal_d[tri[1]] * external_d[tri[2]] * external_d[tri[0]]))
        count+=3 * (external_d[tri[2]] * external_d[tri[0]] * natal_d[tri[1]])
    return count, breakdown
   
def earth_two_third_ungrateful_punish_finder(natal_earth, external_earth, tri):
    natal_d = dict(collections.Counter(natal_earth))
    external_d = dict(collections.Counter(external_earth))
    count = 0
    breakdown=[]
    if tri[0] in natal_d and tri[1] in external_d:
        breakdown.append(f"Natal {tri[0]} Ungrateful Punishes with External {tri[1]}: x" + str(natal_d[tri[0]] * external_d[tri[1]]))
        count+=natal_d[tri[0]] * external_d[tri[1]]
    if tri[1] in natal_d and tri[2] in external_d:
        breakdown.append(f"Natal {tri[1]} Ungrateful Punishes with External {tri[2]}: x" + str(natal_d[tri[1]] * external_d[tri[2]]))
        count+=natal_d[tri[1]] * external_d[tri[2]]
    if tri[2] in natal_d and tri[0] in external_d:
        breakdown.append(f"Natal {tri[2]} Ungrateful Punishes with External {tri[0]}: x" + str(natal_d[tri[2]] * external_d[tri[0]]))
        count+=natal_d[tri[2]] * external_d[tri[0]]
    if tri[0] in natal_d and tri[2] in external_d:
        breakdown.append(f"Natal {tri[0]} Ungrateful Punishes with External {tri[2]}: x" + str(natal_d[tri[0]] * external_d[tri[2]]))
        count+=natal_d[tri[0]] * external_d[tri[2]]
    if tri[1] in natal_d and tri[0] in external_d:
        breakdown.append(f"Natal {tri[1]} Ungrateful Punishes with External {tri[0]}: x" + str(natal_d[tri[1]] * external_d[tri[0]]))
        count+=natal_d[tri[1]] * external_d[tri[0]]
    if tri[2] in natal_d and tri[1] in external_d:
        breakdown.append(f"Natal {tri[2]} Ungrateful Punishes with External {tri[1]}: x" + str(natal_d[tri[2]] * external_d[tri[1]]))
        count+=natal_d[tri[2]] * external_d[tri[1]]
        
    return count, breakdown

def count_earth_ungrateful_punish(natal_earth, external_earth):
    count = 0
    yss_count = 0
    breakdown_1 = []
    breakdown_2 = []

    s = set(natal_earth + external_earth)
    
    if "Yin" in s and "Si" in s and "Shen" in s:
        yss_count, breakdown_1 = earth_full_ungrateful_punish_finder(natal_earth, external_earth, ["Yin","Si","Shen"])
    if yss_count == 0:
        count, breakdown_2 = earth_two_third_ungrateful_punish_finder(natal_earth, external_earth, ["Yin","Si","Shen"])
        
    count = count + yss_count
    breakdown = breakdown_1 + breakdown_2
    return count, breakdown