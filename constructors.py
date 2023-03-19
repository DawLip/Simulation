from data import objs, data

def cellConstructor(type="cell", x=0, y=0, energy=100, wait=100):
    objs.append({
        "id": data["id"],
        "type": type,
        "x": x,
        "y": y,
        "energy": energy,
        "wait": wait,
    })
    data["id"]+=1