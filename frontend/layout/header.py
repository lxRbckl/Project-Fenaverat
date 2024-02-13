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
            
            html.Div([
               
               html.Video(
                  
                  autoPlay = True,
                  controls = False,
                  src = 'https://static.videezy.com/system/resources/previews/000/038/652/original/alb_glitch1048_1080p_24fps.mp4',
                  style = {
                     
                     'width' : '100%',
                     'height' : '15vh',
                     'objectFit' : 'cover'
                     
                  }
                  # children = html.H3(
                     
                  #    id = 'headerlogo',
                  #    style = {'zindex' : 0, 
                  #             'background' : 'red'},
                  #    children = 'demodemodemode ome domed ome domed oemd oedm ')
                  
               ),
               html.H1('demo', className = 'overlay', style = {
                  
                  'padding' : '-50% 0 0 0'
                  
               })
               
         ])

            
         ]
         
      )