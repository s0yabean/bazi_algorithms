
def count_earth_clash(natal_earth, external_earth):
    count = 0
    natal_d = dict(collections.Counter(natal_earth))
    external_d = dict(collections.Counter(external_earth))
    
    if "Wu" in natal_d and "Zi" in external_d:
        print("Natal Wu Clashes with External Zi: x" + str(natal_d["Wu"] * external_d["Zi"]))
        count+=natal_d["Wu"] * external_d["Zi"]
    if "Zi" in natal_d and "Wu" in external_d:
        print("Natal Zi Clashes with External Wu: x" + str(natal_d["Zi"] * external_d["Wu"]))
        count+=natal_d["Zi"] * external_d["Wu"]
    if "Chou" in natal_d and "Wei" in external_d:
        print("Natal Chou Clashes with External Wei: x" + str(natal_d["Chou"] * external_d["Wei"]))
        count+=natal_d["Chou"] * external_d["Wei"]
    if "Wei" in natal_d and "Chou" in external_d:
        print("Natal Wei Clashes with External Chou: x" + str(natal_d["Wei"] * external_d["Chou"]))
        count+=natal_d["Wei"] * external_d["Chou"]
    
    if "Yin" in natal_d and "Shen" in external_d:
        print("Natal Yin Clashes with External Shen: x" + str(natal_d["Yin"] * external_d["Shen"]))
        count+=natal_d["Yin"] * external_d["Shen"]
    if "Shen" in natal_d and "Yin" in external_d:
        print("Natal Shen Clashes with External Yin: x" + str(natal_d["Shen"] * external_d["Yin"]))
        count+=natal_d["Shen"] * external_d["Yin"]
        
    if "Mao" in natal_d and "You" in external_d:
        print("Natal Mao Clashes with External You: x" + str(natal_d["Mao"] * external_d["You"]))
        count+=natal_d["Mao"] * external_d["You"]
    if "You" in natal_d and "Mao" in external_d:
        print("Natal You Clashes with External Mao: x" + str(natal_d["You"] * external_d["Mao"]))
        count+=natal_d["You"] * external_d["Mao"]
        
    if "Si" in natal_d and "Hai" in external_d:
        print("Natal Si Clashes with External Hai: x" + str(natal_d["Si"] * external_d["Hai"]))
        count+=natal_d["Si"] * external_d["Hai"]
    if "Hai" in natal_d and "Si" in external_d:
        print("Natal Hai Clashes with External Si: x" + str(natal_d["Hai"] * external_d["Si"]))
        count+=natal_d["Hai"] * external_d["Si"]
        
    return count

def count_stem_clash(natal_stem, external_stem): 
    count = 0
    natal_d = dict(collections.Counter(natal_stem))
    external_d = dict(collections.Counter(external_stem))
    
    if "Geng" in natal_d and "Jia" in external_d:
        print("Natal Geng Clashes with External Jia: x" + str(natal_d["Geng"] * external_d["Jia"]))
        count+=natal_d["Geng"] * external_d["Jia"]
    if "Jia" in natal_d and "Geng" in external_d:
        print("Natal Jia Clashes with External Geng: x" + str(natal_d["Jia"] * external_d["Geng"]))
        count+=natal_d["Jia"] * external_d["Geng"]
    
    if "Yi" in natal_d and "Xin" in external_d:
        print("Natal Yi Clashes with External Xin: x" + str(natal_d["Yi"] * external_d["Xin"]))
        count+=natal_d["Yi"] * external_d["Xin"]
    if "Xin" in natal_d and "Yi" in external_d:
        print("Natal Xin Clashes with External Yi: x" + str(natal_d["Xin"] * external_d["Yi"]))
        count+=natal_d["Xin"] * external_d["Yi"]
        
    if "Bing" in natal_d and "Ren" in external_d:
        print("Natal Bing Clashes with External Ren: x" + str(natal_d["Bing"] * external_d["Ren"]))
        count+=natal_d["Bing"] * external_d["Ren"]
    if "Ren" in natal_d and "Bing" in external_d:
        print("Natal Ren Clashes with External Bing: x" + str(natal_d["Ren"] * external_d["Bing"]))
        count+=natal_d["Ren"] * external_d["Bing"]
        
    if "Ding" in natal_d and "Gui" in external_d:
        print("Natal Ding Clashes with External Gui: x" + str(natal_d["Ding"] * external_d["Gui"]))
        count+=natal_d["Ding"] * external_d["Gui"]
    if "Gui" in natal_d and "Ding" in external_d:
        print("Natal Gui Clashes with External Ding: x" + str(natal_d["Gui"] * external_d["Ding"]))
        count+=natal_d["Gui"] * external_d["Ding"]
        
    if "Jia" in natal_d and "Wu" in external_d:
        print("Natal Jia Clashes with External Wu: x" + str(natal_d["Jia"] * external_d["Wu"]))
        count+=natal_d["Jia"] * external_d["Wu"]
    if "Wu" in natal_d and "Jia" in external_d:
        print("Natal Wu Clashes with External Jia: x" + str(natal_d["Wu"] * external_d["Jia"]))
        count+=natal_d["Wu"] * external_d["Jia"]
    
    if "Yi" in natal_d and "Ji" in external_d:
        print("Natal Yi Clashes with External Ji: x" + str(natal_d["Yi"] * external_d["Ji"]))
        count+=natal_d["Yi"] * external_d["Ji"]
    if "Ji" in natal_d and "Yi" in external_d:
        print("Natal Ji Clashes with External Yi: x" + str(natal_d["Ji"] * external_d["Yi"]))
        count+=natal_d["Ji"] * external_d["Yi"]
    
    if "Bing" in natal_d and "Geng" in external_d:
        print("Natal Bing Clashes with External Geng: x" + str(natal_d["Bing"] * external_d["Geng"]))
        count+=natal_d["Bing"] * external_d["Geng"]
    if "Geng" in natal_d and "Bing" in external_d:
        print("Natal Geng Clashes with External Bing: x" + str(natal_d["Geng"] * external_d["Bing"]))
        count+=natal_d["Geng"] * external_d["Bing"]
        
    if "Ding" in natal_d and "Xin" in external_d:
        print("Natal Ding Clashes with External Xin: x" + str(natal_d["Ding"] * external_d["Xin"]))
        count+=natal_d["Ding"] * external_d["Xin"]
    if "Xin" in natal_d and "Ding" in external_d:
        print("Natal Xin Clashes with External Ding: x" + str(natal_d["Xin"] * external_d["Ding"]))
        count+=natal_d["Xin"] * external_d["Ding"]
        
    if "Wu" in natal_d and "Ren" in external_d:
        print("Natal Wu Clashes with External Ren: x" + str(natal_d["Wu"] * external_d["Ren"]))
        count+=natal_d["Wu"] * external_d["Ren"]
    if "Ren" in natal_d and "Wu" in external_d:
        print("Natal Ren Clashes with External Wu: x" + str(natal_d["Ren"] * external_d["Wu"]))
        count+=natal_d["Ren"] * external_d["Wu"]
        
    if "Ji" in natal_d and "Gui" in external_d:
        print("Natal Ji Clashes with External Gui: x" + str(natal_d["Ji"] * external_d["Gui"]))
        count+=natal_d["Ji"] * external_d["Gui"]
    if "Gui" in natal_d and "Ji" in external_d:
        print("Natal Gui Clashes with External Ji: x" + str(natal_d["Gui"] * external_d["Ji"]))
        count+=natal_d["Gui"] * external_d["Ji"]
        
    return count
    