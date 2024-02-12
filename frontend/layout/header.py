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
            
            html.H1(id = 'headerlogo', children = 'logo', style = {'fontFamily' : 'YourCustomFont'}),
            html.Video(
               
               autoPlay = True,
               src = 'https://www.w3schools.com/html/mov_bbb.mp4',
               controls = False,
               
               style = {'width' : '50%', 'borderRadius' : 5}
               
            )
            
         ]
         
      )