# import <
from dash import html
import dash_bootstrap_components as dbc

from backend.resource import (
   
   colWidth,
   connections
   
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
         style = {
            
            'paddingBottom' : '0.5%',
            'backgroundColor' : '#F7F5F1'
         
         },
         children = dbc.Row(
            
            justify = 'between',
            children = [
               
               *[
                  
                  dbc.Col(
                     
                     width = 'auto',
                     children = html.A(
                        
                        href = j,
                        children = i,
                        target = '_blank',
                        style = {

                           'fontSize' : 16,
                           'color' : '#181A1B',
                           'fontFamily' : 'helvetica',
                           'textDecoration' : 'underline'
                           
                        }
                     
                     )
                     
                  )
                  
               for i, j in connections.items()]
            ]
            
         )
         
      )