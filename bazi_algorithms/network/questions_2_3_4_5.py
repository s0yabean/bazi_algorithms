from ..bazi_formulas.combines import count_earth_six_harmony_combine, count_earth_combo
from ..persistence.models import NatalChart, ExternalPillars
from ..bazi_formulas.ten_gods import find_rw, find_dw, find_iw, find_7k, find_ho
def easiest_sell(table_data, start_date, end_date):
    """Only deals with month and year external pillar, no 
    dynamic luck pillar
    # this implementation uses stem, not branches
    """
    month_range = external_month_range(start_date, end_date)
    year_range = external_year_range(start_date, end_date)
    
    filtered_data = []
    remarks = []
    for t in table_data:
        r = []
        rob_wealth = find_rw(t.day_s)
        for range in month_range:
            if rob_wealth == range[0]:
                r.append(f'{rob_wealth} Stem found in External Month Pillar. (Period: {range[1]} - {range[2]})')
        for range in year_range:
            if rob_wealth == range[0]:
                r.append(f'{rob_wealth} Stem found in External Year Pillar. (Period: {range[1]} - {range[2]})')
        if r != []:
            filtered_data.append(t)
            remarks.append(r)

    return filtered_data, remarks

def more_prod(table_data, start_date, end_date):
    """Only deals with month and year external pillar, no 
    dynamic luck pillar
    # this implementation uses stem, not branches
    """
    month_range = external_month_range(start_date, end_date)
    year_range = external_year_range(start_date, end_date)

    filtered_data = []
    remarks = []
    for t in table_data:
        r = []
        dw = find_dw(t.day_s)
        iw = find_iw(t.day_s)
        for range in month_range:
            if dw == range[0]:
                r.append(f'{dw} Stem found in Month Pillar. (Period: {range[1]} - {range[2]})')
            if iw == range[0]:
                r.append(f'{iw} Stem found in Month Pillar. (Period: {range[1]} - {range[2]})')
        for range in year_range:
            if dw == range[0]:
                r.append(f'{dw} Stem found in Year Pillar. (Period: {range[1]} - {range[2]})')
            if iw == range[0]:
                r.append(f'{iw} Stem found in Year Pillar. (Period: {range[1]} - {range[2]})')
        if r != []:
            filtered_data.append(t)
            remarks.append(r)

    return filtered_data, remarks
    

def more_reckless(table_data, start_date, end_date):
    """Only deals with month and year external pillar, no 
    dynamic luck pillar
    # this implementation uses stem, not branches
    """
    month_range = external_month_range(start_date, end_date)
    year_range = external_year_range(start_date, end_date)

    filtered_data = []
    remarks = []
    for t in table_data:
        r = []
        seven_k = find_7k(t.day_s)
        for range in month_range:
            if seven_k == range[0]:
                r.append(f'{seven_k} Stem found in External Month Pillar. (Period: {range[1]} - {range[2]})')
        for range in year_range:
            if seven_k == range[0]:
                r.append(f'{seven_k} Stem found in External Year Pillar. (Period: {range[1]} - {range[2]})')
        if r != []:
            filtered_data.append(t)
            remarks.append(r)

    return filtered_data, remarks

def more_rebellious(table_data, start_date, end_date):
    """Only deals with month and year external pillar, no 
    dynamic luck pillar
    # this implementation uses stem, not branches
    """
    month_range = external_month_range(start_date, end_date)
    year_range = external_year_range(start_date, end_date)

    filtered_data = []
    remarks = []
    for t in table_data:
        r = []
        ho = find_ho(t.day_s)
        for range in month_range:
            if ho == range[0]:
                r.append(f'{ho} Stem found in External Month Pillar. (Period: {range[1]} - {range[2]})')
        for range in year_range:
            if ho == range[0]:
                r.append(f'{ho} Stem found in External Year Pillar. (Period: {range[1]} - {range[2]})')
        if r != []:
            filtered_data.append(t)
            remarks.append(r)

    return filtered_data, remarks

def external_month_range(start_date, end_date):
    date_obj = ExternalPillars.query.filter(ExternalPillars.date >= start_date, ExternalPillars.date <= end_date).all()
    dates = [d.date for d in date_obj]

    results = []
    min_index = 0
    max_index = 1
    
    #date_obj needs min 2 length. Add form validation
    for i in range(len(date_obj)):
        month_pillar = date_obj[i].month_pillar.split(" ")
        if i <= len(date_obj) - 2:

            if month_pillar[0] == date_obj[i+1].month_pillar.split(" ")[0]:
                max_index += 1
            else:

                min_date = min(dates[min_index: max_index])
                max_date = max(dates[min_index: max_index])
                results.append([month_pillar[0], min_date, max_date])
                min_index = max_index
                max_index += 1
        else:
            if month_pillar[0] == date_obj[i-1].month_pillar.split(" ")[0]:
                max_index += 1
                
                min_date = min(dates[min_index: max_index])
                max_date = max(dates[min_index: max_index])
                results.append([month_pillar[0], min_date, max_date])
            else:
                results.append([date_obj[i-1].month_pillar.split(" ")[0], min_date, max_date])
                max_index += 1
                results.append([month_pillar[0], max_date, max_date])
    return results

def external_year_range(start_date, end_date):
    date_obj = ExternalPillars.query.filter(ExternalPillars.date >= start_date, ExternalPillars.date <= end_date).all()
    dates = [d.date for d in date_obj]

    results = []
    min_index = 0
    max_index = 0
    
    #date_obj needs min 2 length. Add form validation
    for i in range(len(date_obj)):
        year_pillar = date_obj[i].year_pillar.split(" ")
        if i <= len(date_obj) - 2:
            if year_pillar[0] == date_obj[i+1].year_pillar.split(" ")[0]:
                max_index += 1
            else:
                min_date = min(dates[min_index: max_index])
                max_date = max(dates[min_index: max_index])
                results.append([year_pillar[0], min_date, max_date])
                min_index = max_index
                max_index += 1
        else:
            if year_pillar[0] == date_obj[i-1].year_pillar.split(" ")[0]:
                max_index += 1
                min_date = min(dates[min_index: max_index])
                max_date = max(dates[min_index: max_index])
                results.append([year_pillar[0], min_date, max_date])
            else:
                results.append([date_obj[i-1].year_pillar.split(" ")[0], min_date, max_date])
                max_index += 1
                results.append([year_pillar[0], max_date, max_date])

    return results

