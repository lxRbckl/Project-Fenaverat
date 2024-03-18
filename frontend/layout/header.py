# import <
from .framework import framework

from dash import html
import dash_bootstrap_components as dbc

# >


class header(framework):
   
   def __init__(self): 
      
      super().__init__()
      self.file = 'header'
   
   
   def component(
      
      self,
      pStyle,
      pContent,
      pIntervalRate,
      
      pKey = 'component'
   
   ):
      '''  '''

      return dbc.Col(
         
         style = {
            
            'minWidth' : self.colWidth,
            'maxWidth' : self.colWidth,
            **pStyle[self.file][pKey]['col'],
            'background' : pStyle['framework']['colorWhite']
            
         },
         children = dbc.Row(
               
            justify = 'between',
            children = [
               
               # title <
               # loader <
               dbc.Col(
                  
                  width = 'auto',                  
                  children = html.H1(
                     
                     children = pContent[self.file]['title'],
                     style = {
                                                      
                        **pStyle[self.file][pKey]['titleH1'],
                        'background' : pStyle['framework']['colorWhite']
                        
                     }
                     
                  )
                  
               ),
               dbc.Col(
                  
                  width = 'auto',
                  style = pStyle[self.file][pKey]['loaderCol'],
                  children = [
                     
                     html.Div(
                        
                        id = 'headerTargetId',
                        style = pStyle[self.file][pKey]['loaderDiv'],
                        children = dbc.Spinner(
                           
                           size = 'sm',
                           id = 'headerSpinnerId',
                           color = pStyle['framework']['colorBlack'],
                           spinner_style = pStyle[self.file][pKey]['loaderSpinner']
                           
                        )
                        
                     ),
                     dbc.Tooltip(
                        
                        placement = 'bottom',
                        target = 'headerTargetId',
                        children = html.P(
                           
                           style = pStyle[self.file][pKey]['loaderTooltip'],
                           children = f'Updated every {pIntervalRate} minutes'
                        
                        )
                           
                     )
                     
                  ]
                  
               )
               
               # >
               
            ]
            
         )
                     
      )