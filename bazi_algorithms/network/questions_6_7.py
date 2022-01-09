from ..bazi_formulas.nobleman import find_nobleman
from ..persistence.models import NatalChart


def nobleman_star(table_data, natal_chart_id):
    """In future can check people's luck pillar, for now just 
    check their natal chart"""

    natal_chart = NatalChart.query.filter_by(id=natal_chart_id).one()
    noble_star = find_nobleman(natal_chart.day_s)
    filtered_data = []
    remarks = []
    for t in table_data:
        r = []
        for animal in noble_star:
            if animal == t.hour_e:
                r.append(f'{animal} found in Hour Pillar.')
            if animal == t.day_e:
                r.append(f'{animal} found in Day Pillar.')
            if animal == t.month_e:
                r.append(f'{animal} found in Month Pillar.')
            if animal == t.year_e:
                r.append(f'{animal} found in Year Pillar.')

        if r != []:
            filtered_data.append(t)
            remarks.append(r)
    return filtered_data, remarks


from ..bazi_formulas.peach_blossom import find_pb


def peach_blossom_me_to_others(table_data, natal_chart_id):
    """In future can check people's luck pillar, for now just 
    check their natal chart"""

    natal_chart = NatalChart.query.filter_by(id=natal_chart_id).one()
    animal = find_pb(natal_chart.day_e)
    filtered_data = []
    remarks = []
    for t in table_data:
        r = []
        if animal == t.hour_e:
            r.append(f'{animal} found in Hour Pillar.')
        if animal == t.day_e:
            r.append(f'{animal} found in Day Pillar.')
        if animal == t.month_e:
            r.append(f'{animal} found in Month Pillar.')
        if animal == t.year_e:
            r.append(f'{animal} found in Year Pillar.')

        if r != []:
            filtered_data.append(t)
            remarks.append(r)
    return filtered_data, remarks


def peach_blossom_others_to_me(table_data, natal_chart_id):
    """In future can check people's luck pillar, for now just 
    check their natal chart"""

    natal_chart = NatalChart.query.filter_by(id=natal_chart_id).one()
    pb_dict = {"Mao": ["Yin", "Wu", "Xu"], "Wu": ["Si", "Chou", "You"],
               "You": ["Shen", "Zi", "Chen"], "Zi": ["Hao", "Mao", "Wei"]}

    elements_i_attract = []
    for animal in [natal_chart.hour_e, natal_chart.day_e, natal_chart.month_e, natal_chart.year_e]:
        if animal == "Mao":
            elements_i_attract += pb_dict["Mao"]
        elif animal == "Wu":
            elements_i_attract += pb_dict["Wu"]
        elif animal == "You":
            elements_i_attract += pb_dict["You"]
        elif animal == "Zi":
            elements_i_attract += pb_dict["Zi"]

    filtered_data = []
    remarks = []
    for t in table_data:
        r = []
        for e in elements_i_attract:
            if t.hour_e == e:
                r.append(f'Hour Pillar {e} is attracted to your {find_pb(e)}.')
            if t.day_e == e:
                r.append(f'Day Pillar {e} is attracted to your {find_pb(e)}.')
            if t.month_e == e:
                r.append(f'Month Pillar {e} is attracted to your {find_pb(e)}.')
            if t.year_e == e:
                r.append(f'Year Pillar {e} is attracted to your {find_pb(e)}.')
        if r != []:
            filtered_data.append(t)
            remarks.append(r)
    return filtered_data, remarks
