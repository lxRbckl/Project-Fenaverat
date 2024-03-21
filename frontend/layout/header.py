# import <
from .framework import framework

from dash import dcc, html
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
      pUpdateRate,
      
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
               
               # left <
               # right <
               dbc.Col(
                  
                  width = 'auto',    
                  children = dbc.Stack(
                     
                     gap = 3,
                     direction = 'horizontal',
                     children = [
                        
                        # title <
                        # profiles <
                        html.H1(
                           
                           children = pContent[self.file]['title'],
                           style = {
                              
                              **pStyle[self.file][pKey]['titleH1'],
                              'background' : pStyle['framework']['colorWhite']
                              
                           }
                           
                        ),
                        *[
                           
                           html.Img(
                              
                              src = i,
                              style = {
                                 
                                 **pStyle[self.file][pKey]['titleImg'],
                                 'border' : pStyle['framework']['borderBlack']
                                 
                              }
                              
                           )
                           
                        for i in pContent[self.file]['profiles']]
                        
                        # >
                        
                     ]
                     
                  )
                  
               ),
               dbc.Col(
                  
                  width = 'auto',
                  style = pStyle[self.file][pKey]['rightCol'],
                  children = [
                     
                     # loader <
                     html.Div(
                        
                        id = 'loaderDivId',
                        style = pStyle[self.file][pKey]['loaderDiv'],
                        children = dbc.Spinner(
                           
                           size = 'sm',
                           id = 'loaderSpinnerId',
                           color = pStyle['framework']['colorBlack'],
                           spinner_style = pStyle[self.file][pKey]['loaderSpinner']
                           
                        )
                        
                     ),
                     dbc.Tooltip(
                        
                        placement = 'bottom',
                        target = 'loaderDivId',
                        children = dcc.Markdown(
                           
                           style = pStyle[self.file][pKey]['loaderMarkdown'],
                           children = f'Refreshed every **{pUpdateRate}** minutes.'
                        
                        )
                           
                     )
                     
                     # >
                     
                  ]
                  
               )
               
               # >
               
            ]
            
         )
                     
      )