import threading
from model.model import model

from App import App
def appStart():
    app = App()

if __name__ =="__main__":
    appT = threading.Thread(target=appStart)
    modelT = threading.Thread(target=model)
    # debugT = threading.Thread(target=debug)
 
    modelT.start()
    appT.start()
    # debugT.start()
    # appT.join()