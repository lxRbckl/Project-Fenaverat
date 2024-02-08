# import <
from dash import (dcc, html)
import dash_bootstrap_components as dbc
from dash.dependencies import (Input, Output)

from frontend.layout.header import header
from frontend.layout.footer import footer
from frontend.layout.body.aboutMe import aboutMe
from frontend.layout.body.myServer import myServer
from frontend.layout.body.myProject import myProject
from backend.resource import (
   
   colWidth,
   application
   
)

# >


class template:
   
   
   def __init__(self):
      '''  '''
      
      self.header = header()
      self.footer = footer()
      self.content = [
         
         aboutMe(),
         myProject(),
         myServer()
         
      ]
      
   
   def component(self):
      '''  '''
      
      return html.Div(
         
         style = {
            
            'width' : '100vw',
            'height' : '100vh',
            'overflow' : 'hidden',
            'background' : 'black'
            
         },
         children = [
            
            # header <
            # body <
            # footer <
            dbc.Row(
               
               justify = 'center',
               children = self.header.component()
               
            ),
            dbc.Row(
               
               justify = 'center',
               children = dbc.Col(
                  
                  width = colWidth,
                  style = {
                     
                     'background' : 'blue',
                     'margin' : 0,
                     'padding' : 0
                     
                  },
                  children = dbc.Accordion(
                     
                     flush = True,
                     always_open = True,
                     style = {
                        
                        'padding' : 0,
                        'margin' : 0,
                        'background' : 'green'
                        
                     },
                     children = [
                        
                        dbc.AccordionItem(
                           
                           children = i.page(),
                           style = {'background' : 'red'}
                        
                        )
                        
                     for i in self.content]
                     
                  )
                  
               )
            ),
            dbc.Row(
               
               justify = 'center',
               children = self.footer.component()
               
            )
            
            # >
            
         ]
         
      )