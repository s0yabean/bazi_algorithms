from ..bazi_formulas.combines import (count_earth_six_harmony_combine,
                                      count_earth_combo,
                                      )
from ..persistence.models import NatalChart


def career_plus(table_data, natal_chart_id):
    natal_chart = NatalChart.query.filter_by(id=natal_chart_id).one()
    natal_chart_ext = [natal_chart.month_e, natal_chart.year_e]

    filtered_data = []
    remarks = []

    for natal_obj in table_data:
        natal_comb_e = [natal_obj.month_e, natal_obj.year_e]

        e_harmony_combine, bd_1 = count_earth_six_harmony_combine(natal_chart_ext, natal_comb_e)
        e_combo_combine, bd_2 = count_earth_combo(natal_chart_ext, natal_comb_e)

        if e_harmony_combine + e_combo_combine > 0:
            if filtered_data == [] or filtered_data[-1].id != natal_obj.id:
                remarks += [bd_1 + bd_2]
                filtered_data.append(natal_obj)
            else:
                remarks[-1] += bd_1 + bd_2

    return filtered_data, remarks
