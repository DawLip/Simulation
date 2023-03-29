import threading

from app.app import app
from model.model import model
from debug.debug import debug

if __name__ =="__main__":
    appT = threading.Thread(target=app)
    modelT = threading.Thread(target=model)
    debugT = threading.Thread(target=debug)
 
    appT.start()
    modelT.start()
    debugT.start()