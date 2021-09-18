from .combines import count_earth_combo, count_earth_six_harmony_combine, count_stem_combine
from .clashes import count_stem_clash, count_earth_clash
from .harm import count_earth_harm
from .destruction import count_earth_destroy
from .punish import count_earth_bully_punish, count_earth_uncivil_punish, count_earth_self_punish, count_earth_ungrateful_punish

def calc_comb_clash(natal_stem, natal_earth, dates):
    result = []
    for i in range(len(dates)):
        external_stem = []
        external_earth = []
        li = [dates[i].day_pillar, dates[i].month_pillar, dates[i].year_pillar]
        for item in li:
            s = item.split(' ')
            external_stem.append(s[0])
            external_earth.append(s[1])
     
        e_harmony_combine, bd = count_earth_six_harmony_combine(natal_earth, external_earth)
        e_combo_combine, bd = count_earth_combo(natal_earth, external_earth)
        s_combine, bd = count_stem_combine(natal_stem, external_stem)

        e_clash, bd = count_earth_clash(natal_earth, external_earth)
        s_clash, bd = count_stem_clash(natal_stem, external_stem)

        e_bp, bd = count_earth_bully_punish(natal_earth, external_earth)
        e_ucp, bd = count_earth_uncivil_punish(natal_earth, external_earth)
        e_sp, bd = count_earth_self_punish(natal_earth, external_earth)
        e_ugp, bd = count_earth_ungrateful_punish(natal_earth, external_earth)
        e_dest, bd = count_earth_destroy(natal_earth, external_earth)
        e_harm, bd = count_earth_harm(natal_earth, external_earth)

        row = {"s_combine":s_combine, "s_clash":s_clash, "e_combine":e_combo_combine + e_harmony_combine, "e_clash": e_clash + e_bp + e_ugp + e_sp + e_ucp + e_dest + e_harm}
        result.append(row)
    return result