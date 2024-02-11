# import <
from dash import html
import dash_bootstrap_components as dbc

from backend.resource import (
   
   colWidth
   
)

# >


class header:
   
   def __init__(self):
      '''  '''
      
      pass
   
   
   def component(self):
      '''  '''
      
      return dbc.Col(
         
         width = colWidth,
         style = {'backgroundColor' : 'white'},
         children = [
            
            html.H1(id = 'headerlogo', children = 'logo')
            
         ]
         
      )