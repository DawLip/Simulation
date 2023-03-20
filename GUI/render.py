def renderMap():
    for obj in objs:
        img[obj["y"]][obj["x"]]=colors[obj["type"]]

    scaledImg = QPixmap(toQImg()).scaledToWidth(data["x"]*6)
    label.setPixmap(scaledImg)
    label2.setText(str(data["tick"]))