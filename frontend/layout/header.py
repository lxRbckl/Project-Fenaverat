# import <
from dash import html
import dash_bootstrap_components as dbc

from backend.resource import (
   
   colWidth,
   tooltipResponse
   
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
         style = {
            
            'paddingTop' : '1%',
            'background' : '#F7F5F1'
            
         },
         children = dbc.Row(
               
            justify = 'between',
            children = [
               
               # title <
               # loader <
               dbc.Col(
                  
                  width = 'auto',
                  children = html.H1(
                     
                     children = 'Alex Arbuckle',
                     style = {
                              
                        'margin' : 0,     
                        'fontSize' : 85,
                        'lineHeight' : 0.9,
                        'color' : '#181A1B',
                        'fontFamily' : 'Helveticamazing'
                        
                     }
                     
                  )
                  
               ),
               dbc.Col(
                  
                  width = 'auto',
                  style = {'marginTop' : -5},
                  children = [
                     
                     html.Div(
                        
                        id = 'headerTargetId',
                        children = dbc.Spinner(
                           
                           size = 'sm',
                           color = '#181A1B',
                           id = 'headerSpinnerId',
                           spinner_style = {
                              
                              'border-width' : 1.5, 
                              'animation-play-state' : 'running'
                              
                           }
                           
                        )
                        
                     ),
                     dbc.Tooltip(
                        
                        placement = 'left',
                        target = 'headerTargetId',
                        children = tooltipResponse
                        
                     )
                     
                  ]
                  
               )
               
               # >
               
            ]
            
         )
                     
      )