from ..bazi_formulas.combines import count_earth_six_harmony_combine, count_earth_combo
from ..persistence.models import NatalChart, ExternalPillars
def career_plus(table_data, start_date, end_date):
    """Only deals with month and year external pillar, no 
    dynamic luck pillar"""
    date_obj = ExternalPillars.query.filter(ExternalPillars.date >= start_date, ExternalPillars.date <= end_date).all()
    month_dates = [d.month_pillar for d in date_obj]
    year_dates = [d.year_pillar for d in date_obj]

    date_set = set()
    for i in range(len(month_dates)):
        date_str = month_dates[i].split(" ")[1] + " " + year_dates[i].split(" ")[1]
        date_set.add(date_str)
    
    filtered_data = []
    remarks = []

    for natal_obj in table_data:
        for external_earth in list(date_set):
            natal_comb_e = [natal_obj.month_e, natal_obj.year_e]

            e_harmony_combine, bd_1 = count_earth_six_harmony_combine(natal_comb_e, external_earth.split(" "))
            e_combo_combine, bd_2 = count_earth_combo(natal_comb_e, external_earth.split(" "))

            if e_harmony_combine + e_combo_combine > 0:
                    for i in range(len(bd_1)):
                        bd_1[i] += " (" + external_earth + " Period)"
                    for i in range(len(bd_2)):
                        bd_2[i] += " (" + external_earth + " Period)"

                    if filtered_data == [] or filtered_data[-1].id != natal_obj.id:
                        remarks += [bd_1 + bd_2]
                        filtered_data.append(natal_obj)
                    else:
                        remarks[-1] += bd_1 + bd_2 

    return filtered_data, remarks
