from ._anvil_designer import Form1Template
from anvil import *
import time
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    counter=0
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_2.text=self.text_box_1.text
    pass

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    xx=str(time.time_ns())
    counter=counter+1
    self.text_box_2.text=counter
    
    pass
