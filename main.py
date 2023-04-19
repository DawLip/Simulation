import threading
from model.model import model

from App import App
def appStart():
    app = App()
    app.mainloop()

if __name__ =="__main__":
    modelT = threading.Thread(target=model)
    appT = threading.Thread(target=appStart)
    # debugT = threading.Thread(target=debug)
 
    modelT.start()
    appT.start()
    # debugT.start()
    # appT.join()