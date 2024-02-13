# import <
from time import sleep
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
   application,
   defaultBoard
   
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
            
            'padding' : '2%',
            'width' : '100vw',
            'height' : '100vh',
            'background' : '#181A1B'
            
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
                     
                     'margin' : 0,
                     'padding' : 0
                     
                  },
                  children = dbc.Accordion(
                     
                     flush = True,
                     active_item = None,
                     always_open = True,
                     id = 'bodyAccordion',
                     children = [
                        
                        dbc.AccordionItem(
                           
                           item_id = i.id,
                           title = i.title,
                           style = i.style,
                           children = i.board()
                           
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
      

@application.callback(
   
   Output('bodyAccordion', 'active_item'),
   Input('headerColId', 'children')
   
)
def bodyCallback(i):
   
   sleep(2)
   return 'b1'