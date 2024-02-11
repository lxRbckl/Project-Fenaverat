# import <
from dash import html
import dash_bootstrap_components as dbc

from backend.resource import (
   
   colWidth
   
)

# >


class myProject:
   
   def __init__(self):
      '''  '''
      
      self.id = 'b2'
      self.title = 'My Projects'
      self.style = {
         
         
         
      }
   
   
   def board(self):
      '''  '''
      
      return [
         
         html.H1('my project')
         
      ]