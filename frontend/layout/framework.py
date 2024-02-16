# import <
from backend.resource import application

from time import sleep
from dash import (dcc, html)
import dash_bootstrap_components as dbc
from dash.dependencies import (Input, Output)

# >


class framework:
   
   def __init__(self):
      '''  '''
      
      # objects <
      # attributes <
      self.body = []
      self.header = None
      self.footer = None
      self.database = None
      
      self.colWidth = 8
      self.defaultBoard = 'b1'
      
      # >

   
   def framework(self):
      '''  '''
      
      return html.Div(
         
         style = {
            
            'width' : '100vw',
            'height' : '100vh',
            'paddingTop' : '1%',
            'overflow' : 'hidden',
            'paddingBottom' : '1%',
            'background' : '#181A1B'
            
         },                  
         children = [
            
            dcc.Interval(
               
               n_intervals = 0,
               id = 'templateIntervalId',
               interval = self.database.intervalRate
               
            ),
            html.Div(
               
               children = None,
               id = 'templateDivId'
            
            )
                        
         ]
         
      )
   
   
   def components(
      
      self, 
      pData,
      pRate,
      pStatus
      
   ):
      '''  '''

      return [
         
         # header <
         # body <
         # footer <
         dbc.Row(
            
            justify = 'center',
            children = self.header.component(
               
               pRate = pRate,
               pStatus = pStatus,
               pStyle = pData['style']['header'],
               pContent = pData['content']['header']
               
            )
            
         ),
         dbc.Row(
            
            id = 'bodyRowId',
            justify = 'center',
            children = dbc.Col(
               
               width = self.colWidth,
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
                        
                        item_id = v.id,
                        title = v.title,
                        style = v.style,
                        children = v.board()
                        
                     )
                     
                  for v in (self.body).values()]
                  
               )
               
            )
            
         ),
         dbc.Row(
            
            justify = 'center',
            children = self.footer.component(
               
               pStyle = pData['style']['footer'],
               pContent = pData['content']['footer']
               
            )
            
         )
         
         # >
         
      ]
   
   
   def registerIntervalCallback(self):
      '''  '''
      
      @application.callback(
         
         Output('templateDivId', 'children'),
         Input('templateIntervalId', 'n_intervals')
         
      )
      def intervalCallback(i):
         '''  '''
         
         return self.components(
            
            pRate = self.database.rate,
            pData = self.database.get(),
            pStatus = self.database.status
            
         )

      
   def registerBodyCallback(self):
      '''  '''
      
      @application.callback(
         
         Output('bodyAccordionId', 'active_item'),
         Input('bodyRowId', 'children')
         
      )
      def bodyCallback(i):
         '''  '''
         
         sleep(self.database.boardDelay)
         return self.defaultBoard