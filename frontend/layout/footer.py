# import <
from dash import html
import dash_bootstrap_components as dbc

from backend.resource import (
   
   socials,
   colWidth
   
)

# >


class footer:
   
   def __init__(self):
      '''  '''
      
      pass
   
   
   def component(self):
      '''  '''
      
      return dbc.Col(
         
         width = colWidth,
         style = {'backgroundColor' : '#F7F5F1'},
         children = [
            
            html.Hr(),
            html.H1(
               
               children = 'footer', 
               style = {'fontWeight' : 'bold', 'fontFamily' : 'Helvetica'})
            
         ]
         
      )