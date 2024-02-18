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
      
      self.defaultBoard = 'b1'
      self.colWidth = 'col-sm-11 col-md-8 col-lg-10 col-xl-9'
      
      # >

   
   def framework(self):
      '''  '''
      
      return html.Div(
         
         style = {
            
            'width' : '100vw',
            'height' : '100vh',
            'paddingTop' : '2%',
            'overflow-x' : 'hidden',
            'paddingBottom' : '1%',
            'background' : '#181A1B'
            
         },                  
         children = [
            
            dcc.Interval(
               
               n_intervals = 0,
               id = 'frameworkIntervalId',
               interval = self.database.intervalRate
               
            ),
            html.Div(
               
               children = None,
               id = 'frameworkDivId'
            
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
                        children = v.board(
                           
                           pContent = pData['content'][k],
                           pStyle = pData['style']['body']
                           
                        )
                        
                     )
                     
                  for k, v in (self.body).items()]
                  
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
      
      
   def registerBodyCallback(self):
      '''  '''
      
      @application.callback(
         
         Output('bodyAccordionId', 'active_item'),
         Input('bodyRowId', 'children')
         
      )
      def bodyCallback(i):
         '''  '''
                  
         sleep(self.database.bodyDelay)
         return self.defaultBoard
      
   
   def registerAboutMeCallback(self):
      '''  '''
   
      @application.callback(
         
         Output('backgroundVideoId', 'playing'),
         Input('bodyAccordionId', 'active_item')
         
      )
      def aboutMeCallback(i):
         '''  '''
         
         # <
         # <
         if (self.defaultBoard == i):
            
            sleep(self.database.aboutMeDelay)
            return True
         
         else: return False
         
         # >
   
   
   def registerIntervalCallback(self):
      '''  '''
      
      @application.callback(
         
         Output('frameworkDivId', 'children'),
         Input('frameworkIntervalId', 'n_intervals')
         
      )
      def intervalCallback(i):
         '''  '''
         
         return self.components(
            
            pRate = self.database.rate,
            pData = self.database.get(),
            pStatus = self.database.status
            
         )