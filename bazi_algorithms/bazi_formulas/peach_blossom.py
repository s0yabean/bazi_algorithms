
def find_pb(day_earth):
    if day_earth in ["Yin", "Wu", "Xu"]:
        return "Mao"
    elif day_earth in ["Si", "Chou", "You"]:
        return "Wu"
    elif day_earth in ["Shen", "Zi", "Chen"]:
        return "You"
    else: #day_earth in ["Hao", "Mao", "Wei"]:
        return "Zi"
