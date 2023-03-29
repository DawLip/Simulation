from data import data, GUI
from .section import Section
from .txt import Txt

class Button(Section):
    def __init__(
            # Section attrs
            self, name="", parent=None,
            size=(100, 100), position=(0,0), 
            bgc=(255,255,255), 

            # Button attrs
            txt="Button1",
            action=None,
        ):
        
        super().__init__(name, parent, size, position, bgc)
        
        self.txt=txt
        self.action=action

        self.clickable=True
        Section.clickableSectionsList.append(self)

        Txt(
            name=f'{self.name} txt',
            parent=self.name,
            txt=self.txt,
        )
