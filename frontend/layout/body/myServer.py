# import <
from dash import html
import dash_bootstrap_components as dbc

from backend.resource import (
   
   colWidth
   
)

# >


class myServer:
   
   def __init__(self):
      '''  '''
      
      self.id = 'b3'
      self.title = 'My Servers'
      self.style = {
         
         
         
      }
   
   
   def board(self):
      '''  '''
      
      return [
         
         html.H1('my server')
         
      ]