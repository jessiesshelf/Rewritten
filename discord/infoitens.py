import json

def ItemGet(name:str):
    with open(r"D:\Coders\rewritten\chapter1\itens.json") as f:
        data = json.load(f)
    
    _name = name.lower().replace(" ","")
    for itens in data:
        _itemname = itens["name"].lower().replace(" ","")
        if _itemname == _name:
            return itens
    else:
        return False

def InfoDescription(choice, alt=""):
    with open(r"D:\Coders\rewritten\chapter1\itens.json") as f:
        data = json.load(f)
    
    for itens in data:
        if choice == itens["name"]:
            if itens["alt"] is True and alt != "":
                for alts in itens:
                    if alts == alt:
                        return(itens[alts]["desc"])
                return(itens["desc"])
            else:
                return(itens["desc"])
    return("Item não encontrado.")

def InfoCreate(item, alt=""):
   with open(r"D:\Coders\rewritten\chapter1\itens.json") as f:
    data = json.load(f)

    if item and item["discovered"]:
        typesset = {
            "Weapon": lambda i: f'{i["dices"]} de Dano' if i["dices"] else None,
            "Additional": lambda i: f'+{i["dices"]} de Dano Adicional' if i["dices"] else None,
            "Notebook": lambda i: f'{i["pages"]} Páginas' if i["pages"] > 0 else None,
            "DFArmour": lambda i: f'{i["DF"]} DF' if i.get("DF", 0) > 0 else None,
            "VTArmour": lambda i: f'{i["VT"]} VT' if i["VT"] > 0 else None,
            "Magic": lambda i: f'{i["MG"]} MG' if i["MG"] > 0 else None,
            "Invincibility": lambda i: f'+{i["iframes"]} IFrames' if i["iframes"] > 0 else None,
            "Consumable": lambda i: f'Cura {i["heal"]} de HP' if i["heal"] > 0 else None,
        }

        _firstline = f'* {item["name"]} - ' 
        _secondline = f'* {InfoDescription(item["name"], alt)}'
        _status = []

        for types in typesset:
            if types in item["vtype"]:
                _status.append(typesset[types](item))
        
        if item.get("Effects",False):
            _status.append(item["effects"])

        while None in _status:
            _status.remove(None)

        _firstline += ", ".join(_status)

        if _status:
            _firstline += "."

        return _firstline + "\n" + _secondline

    else: return "Item não encontrado ou descorberto."

def ListInfoCreate(item):
    
    if item:
        typesset = {
            "Weapon": lambda i: f'{i["dices"]}' if i["dices"] else None,
            "Additional": lambda i: f'+{i["dices"]}' if i["dices"] else None,
            "Notebook": lambda i: f'{i["pages"]} Páginas' if i["pages"] > 0 else None,
            "DFArmour": lambda i: f'{i["DF"]} DF' if i.get("DF", 0) > 0 else None,
            "VTArmour": lambda i: f'{i["VT"]} VT' if i["VT"] > 0 else None,
            "Magic": lambda i: f'{i["MG"]} MG' if i["MG"] > 0 else None,
            "Invincibility": lambda i: f'+{i["iframes"]} IFrames' if i["iframes"] > 0 else None,
            "Consumable": lambda i: f'Cura {i["heal"]} de HP' if i["heal"] > 0 else None,
        }

        _firstline = f'{item["name"]} - ' 
        _status = []

        for types in typesset:
            if types in item["vtype"]:
                _status.append(typesset[types](item))
        
        if item.get("effects",False):
            _status.append(item["effects"])

        while None in _status:
            _status.remove(None)
        _firstline += ", ".join(_status)

        return _firstline

    else: return "Item não encontrado ou descorberto."

def ItemCreate(name:str,desc:str,alt:bool,
               AT:int,DF:int,MG:int,pages:int,
               VT:int,heal:int,iframes:float,dices:str,effects:str,
               type:str, vtype:str,disc:bool):
               
    with open(r"D:\Coders\rewritten\chapter1\itens.json") as f:
        data = json.load(f)

    _desc = desc.replace("\\n","\n")
    _new = {"name": name, "desc": _desc, "alt": alt,"discovered": disc}
    if AT > 0: _new["AT"] = AT
    if DF > 0: _new["DF"] = DF
    if MG > 0: _new["MG"] = MG
    if pages > 0: _new["pages"] = pages
    if VT > 0: _new["VT"] = VT
    if heal > 0: _new["heal"] = heal
    if iframes > 0: _new["iframes"] = iframes
    if dices: _new ["dices"] = dices
    if effects: _new ["effects"] = effects
    if vtype: _new["vtype"] = [vtype]
    if type: _new["type"] = type

    data.append(_new)

    with open(r"D:\Coders\rewritten\chapter1\itens.json", "w") as f:
        json.dump(data,f,indent=4)

def ItemListCreate(section:str):

    with open(r"D:\Coders\rewritten\chapter1\itens.json") as f:
        data = json.load(f)
    
    _weapons = []
    _ammo = []
    _armour = [] 
    _acce = []
    _consumable = []
    _extras = []

    for itens in data:
        if itens["discovered"]:
            if itens["type"] == "Weapon": _weapons.append(f'{ListInfoCreate(itens)}')
            elif itens["type"] == "Ammo": _ammo.append(f'{ListInfoCreate(itens)}')
            elif itens["type"] == "Armour": _armour.append(f'{ListInfoCreate(itens)}')
            elif itens["type"] == "Acce": _acce.append(f'{ListInfoCreate(itens)}')
            elif itens["type"] == "Consumable": _consumable.append(f'{ListInfoCreate(itens)}')
            elif itens["type"] == "Extra": _extras.append(f'{ListInfoCreate(itens)}')

    _list = f"# ITENS ({section})\n"
    if _weapons: _list += f'> # Armas \n' + "\n".join(_weapons)
    if _ammo: _list += f'\n> ## Munição\n' + "\n".join(_ammo)
    if _armour: _list += f'\n> # Armaduras\n' + "\n".join(_armour)
    if _acce: _list += f'\n> ## Acessórios\n' + "\n".join(_acce)
    if _consumable: _list += f'\n> # Consumíveis\n' + "\n".join(_consumable)
    if _extras: _list += f'\n> # Extras\n' + "\n".join(_extras)

    return _list