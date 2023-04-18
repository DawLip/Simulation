import threading
from model.model import model

from App import App
def appStart():
    app = App()
    app.mainloop()

if __name__ =="__main__":
    appT = threading.Thread(target=appStart)
    modelT = threading.Thread(target=model)
    # debugT = threading.Thread(target=debug)
 
    appT.start()
    modelT.start()
    # debugT.start()
    # appT.join()