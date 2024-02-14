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
      
      
   def loadHeader(self):
      '''  '''
      
      return dbc.Row(
         
         justify = 'center',
         children = self.header.component()
         
      )
   
   
   def loadBody(self):
      '''  '''
      
      return dbc.Row(
         
         justify = 'center',
         children = dbc.Col(
            
            width = colWidth,
            style = {
               
               'background' : '#F7F5F1',
               'paddingBottom' : '0.5%'
            
            },
            children = dbc.Accordion(
               
               flush = True,
               active_item = None,
               id = 'bodyAccordionId',
               style = {
                  
                  'borderTop' : '1px solid #181A1B',
                  'borderBottom' : '1px solid #181A1B'
                  
               },
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
         
      )

   
   def loadFooter(self):
      '''  '''

      return dbc.Row(
         
         justify = 'center',
         children = self.footer.component()
         
      )
   
   
   def component(self):
      '''  '''
      
      return html.Div(
         
         id = 'templateDivId',
         style = {
            
            'width' : '100vw',
            'height' : '100vh',
            'paddingTop' : '1%',
            'overflow' : 'hidden',
            'paddingBottom' : '1%',
            'background' : '#181A1B'
            
         },
         children = [
            
            # header <
            # body <
            # footer <
            self.loadHeader(),
            self.loadBody(),
            self.loadFooter()
            
            # >
            
         ]
         
      )
      
      
@application.callback(
   
   Output('bodyAccordionId', 'active_item'),
   Input('headerColId', 'children')
   
)
def bodyCallback(i):
   
   sleep(2)
   return defaultBoard