import json
from champ_class import Champ


def createObj(choice):
    with open("stats.json", "r") as f:
        data = f.read()
    obj = json.loads(data)
    name = obj["data"][choice]["name"]
    hp = obj["data"][choice]["stats"]["hp"]
    range = obj["data"][choice]["stats"]["attackrange"]
    mana = obj["data"][choice]["stats"]["mp"]
    dmg = obj["data"][choice]["stats"]["attackdamage"]
    movespeed = obj["data"][choice]["stats"]["movespeed"]
    qCD = obj["data"][choice]["spells"][0]["cooldown"]
    wCD = obj["data"][choice]["spells"][1]["cooldown"]
    eCD = obj["data"][choice]["spells"][2]["cooldown"]
    rCD = obj["data"][choice]["spells"][3]["cooldown"]
    champ = Champ(name, hp, range, mana, dmg, movespeed, qCD, wCD, eCD, rCD)
    f.close()
    return champ