from ..bazi_formulas.combines import count_earth_six_harmony_combine, count_earth_combo
from ..persistence.models import NatalChart, ExternalPillars
from ..bazi_formulas.ten_gods import find_rw, find_dw, find_iw, find_7k, find_ho
def easiest_sell(table_data, start_date, end_date):
    """Only deals with month and year external pillar, no 
    dynamic luck pillar
    # this implementation uses stem, not branches
    """
    date_set = date_set_helper(start_date, end_date)
    
    filtered_data = []
    remarks = []
    for t in table_data:
        r = []
        for external_stem in date_set:
            rob_wealth = find_rw(t.day_s)
            external_stem_list = external_stem.split(" ")
            if rob_wealth in external_stem_list:
                if rob_wealth == external_stem_list[0]:
                    r.append(f'{rob_wealth} found in Month Pillar. ({external_stem} Period)')
                if rob_wealth == external_stem_list[1]:
                    r.append(f'{rob_wealth} found in Year Pillar. ({external_stem} Period)')

        if r != []:
            filtered_data.append(t)
            remarks.append(r)

    return filtered_data, remarks

def more_prod(table_data, start_date, end_date):
    """Only deals with month and year external pillar, no 
    dynamic luck pillar
    # this implementation uses stem, not branches
    """
    date_set = date_set_helper(start_date, end_date)

    filtered_data = []
    remarks = []
    for t in table_data:
        r = []
        for external_stem in date_set:
            dw = find_dw(t.day_s)
            iw = find_iw(t.day_s)
            external_stem_list = external_stem.split(" ")
            if dw in external_stem_list:
                if dw == external_stem_list[0]:
                    r.append(f'{dw} found in Month Pillar. ({external_stem} Period)')
                if dw == external_stem_list[1]:
                    r.append(f'{dw} found in Year Pillar. ({external_stem} Period)')
                if iw == external_stem_list[0]:
                    r.append(f'{dw} found in Month Pillar. ({external_stem} Period)')
                if iw == external_stem_list[1]:
                    r.append(f'{dw} found in Year Pillar. ({external_stem} Period)')

        if r != []:
            filtered_data.append(t)
            remarks.append(r)

    return filtered_data, remarks

def more_reckless(table_data, start_date, end_date):
    """Only deals with month and year external pillar, no 
    dynamic luck pillar
    # this implementation uses stem, not branches
    """
    date_set = date_set_helper(start_date, end_date)

    filtered_data = []
    remarks = []
    for t in table_data:
        r = []
        for external_stem in date_set:
            seven_k = find_7k(t.day_s)
            external_stem_list = external_stem.split(" ")
            if seven_k in external_stem_list:
                if seven_k == external_stem_list[0]:
                    r.append(f'{seven_k} found in Month Pillar. ({external_stem} Period)')
                if seven_k == external_stem_list[1]:
                    r.append(f'{seven_k} found in Year Pillar. ({external_stem} Period)')
                if seven_k == external_stem_list[0]:
                    r.append(f'{seven_k} found in Month Pillar. ({external_stem} Period)')
                if seven_k == external_stem_list[1]:
                    r.append(f'{seven_k} found in Year Pillar. ({external_stem} Period)')

        if r != []:
            filtered_data.append(t)
            remarks.append(r)

    return filtered_data, remarks

def more_rebellious(table_data, start_date, end_date):
    """Only deals with month and year external pillar, no 
    dynamic luck pillar
    # this implementation uses stem, not branches
    """
    date_set = date_set_helper(start_date, end_date)

    filtered_data = []
    remarks = []
    for t in table_data:
        r = []
        for external_stem in date_set:
            ho = find_ho(t.day_s)
            external_stem_list = external_stem.split(" ")
            if ho in external_stem_list:
                if ho == external_stem_list[0]:
                    r.append(f'{ho} found in Month Pillar. ({external_stem} Period)')
                if ho == external_stem_list[1]:
                    r.append(f'{ho} found in Year Pillar. ({external_stem} Period)')
                if ho == external_stem_list[0]:
                    r.append(f'{ho} found in Month Pillar. ({external_stem} Period)')
                if ho == external_stem_list[1]:
                    r.append(f'{ho} found in Year Pillar. ({external_stem} Period)')

        if r != []:
            filtered_data.append(t)
            remarks.append(r)

    return filtered_data, remarks

def date_set_helper(start_date, end_date):
    date_obj = ExternalPillars.query.filter(ExternalPillars.date >= start_date, ExternalPillars.date <= end_date).all()
    month_dates = [d.month_pillar for d in date_obj]
    year_dates = [d.year_pillar for d in date_obj]

    date_set = set()
    for i in range(len(month_dates)):
        date_str = month_dates[i].split(" ")[0] + " " + year_dates[i].split(" ")[0] 
        date_set.add(date_str)
    return list(date_set)

