# import <
from dash import (dcc, html)
import dash_bootstrap_components as dbc
from dash.dependencies import (Input, Output)

from backend.resource import application
from frontend.layout.header import header
from frontend.layout.footer import footer
from frontend.layout.body.aboutMe import aboutMe
from frontend.layout.body.myServer import myServer
from frontend.layout.body.myProject import myProject

# >


class template:
   
   
   def __init__(self):
      '''  '''
      
      self.content = [
         
         aboutMe(),
         myProject(),
         myServer()
         
      ]
      
   
   def component(self):
      '''  '''
      
      return html.Div(
         
         children = [
            
            # header <
            # body <
            # footer <
            dbc.Row(
               
               justify = 'center',
               children = header()
               
            ),
            dbc.Row(
               
               justify = 'center',
               children = dbc.Col(
                  
                  width = 5,
                  children = dbc.Accordion(
                     
                     style = {},
                     children = [
                        
                        dbc.AccordionItem(i)
                        
                     for i in self.content]
                     
                  )
                  
               )
            ),
            dbc.Row(
               
               justify = 'center',
               children = footer()
               
            )
            
            # >
            
         ]
         
      )