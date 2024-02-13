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
         id = 'headerColId',
         style = {
            
            'padding' : 0,
            'background' : '#F7F5F1'
            
         },
         children = [
         
            dbc.Row(
               
               justify = 'between',
               children = [
                  
                  dbc.Col(
                     
                     width = 'auto',
                     children = html.H1(
                        
                        children = 'Alex Arbuckle',
                        style = {
                           
                           'fontSize' : 85,
                           'color' : '#181A1B',
                           'margin' : '0 0 -10px 0',
                           'fontFamily' : 'Helveticamazing'
                           
                        }
                        
                     )
                     
                  ),
                  dbc.Col(
                     
                     width = 'auto',
                     style = {'paddingTop' : 10},
                     children = [
                        
                        dbc.Spinner(
                           
                           size = 'sm',
                           color = '#181A1B',
                           id = 'colSpinnerId',
                           spinner_style = {
                              
                              'border-width' : 1.5, 
                              'animation-play-state' : 'running' # running or paused #
                           
                           }
                           
                        ),
                        dbc.Tooltip(
                           
                           target = 'colSpinnerId',
                           children = 'example'
                           
                        )
                        
                     ]
                     
                  )
                  
               ]
               
            ),
            html.Div(style = {'borderBottom' : '1.5px solid #181A1B'})
            
         ]
         
      )