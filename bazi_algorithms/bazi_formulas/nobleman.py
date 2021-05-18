
def find_nobleman(dm):
    if dm in ["Jia", "Wu", "Geng"]:
        return ["Chou", "Wei"]
    elif dm in ["Yi", "Ji"]:
        return ["Zi", "Shen"]
    elif dm in ["Bing", "Ding"]:
        return ["Hai", "You"]
    elif dm in ["Ren", "Gui"]:
        return ["Mao", "Si"]
    else:# ["Xin"]:
        return ["Wu", "Yin"]    

