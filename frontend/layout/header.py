# import <
from .framework import framework

from dash import html
import dash_bootstrap_components as dbc

# >


class header(framework):
   
   def __init__(self): super().__init__()
   
   
   def component(
      
      self,
      pRate,
      pStyle,
      pStatus,
      pContent
   
   ):
      '''  '''

      return dbc.Col(
         
         width = self.colWidth,
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
                     
                     children = pContent['title'],
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
                        style = {'padding' : '0.25%'},
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
                        
                        placement = 'bottom',
                        target = 'headerTargetId',
                        children = [
                           
                           # rate <
                           # status <
                           html.P(
                              
                              children = f'Updated every {pRate} minutes.',
                              style = {
                                 
                                 'fontSize' : 13,
                                 'color' : '#F7F5F1',
                                 'fontFamily' : 'helvetica',
                                 'textDecoration' : 'underline'
                                 
                              }
                              
                           ),
                           *[
                              
                              html.Div(
                                 
                                 style = {'marginBottom' : 10},
                                 children = [
                                 
                                    html.P(
                                       
                                       children = k1.title(),
                                       style = {
                                          
                                          'margin' : 0,
                                          'fontSize' : 13,
                                          'color' : '#F7F5F1',
                                          'paddingBottom' : 5,
                                          'textAlign' : 'left',
                                          'textDecoration' : 'underline'
                                          
                                       }
                                       
                                    ),
                                    *[
                                       
                                       html.P(
                                          
                                          children = f'{k2}.json',
                                          style = {
                                             
                                             'margin' : 0,
                                             'fontSize' : 13,
                                             'paddingLeft' : 5,
                                             'textAlign' : 'left',
                                             'color' : {
                                                
                                                'local' : '#B22B27',
                                                'remote' : '#27B271'
                                                
                                             }[v]
                                             
                                          }
                                          
                                       )
                                       
                                    for k2, v in pStatus[k1].items()]
                                 
                                 ]
                                 
                              )
                              
                           for k1 in pStatus.keys()]
                           
                           # >
                           
                        ]
                        
                     )
                     
                  ]
                  
               )
               
               # >
               
            ]
            
         )
                     
      )