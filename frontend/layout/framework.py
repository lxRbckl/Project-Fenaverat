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
      
      self.colWidth = 1000
      self.bodyLoadDelay = 0
      self.defaultBoard = 'b1'
      
      # >

   
   def framework(self):
      '''  '''
      
      return html.Div(
         
         style = {
                        
            'width' : '100vw',
            'height' : '100vh',
            'paddingTop' : '1%',
            'paddingBottom' : '1%',
            'overflow-x' : 'hidden',
            'background' : '#181A1B',
            'scrollbar-width' : 'thin'
            
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
      pUpdateRate
      
   ):
      '''  '''
            
      return [
         
         # header <
         # body <
         # footer <
         dbc.Row(
            
            justify = 'center',
            children = self.header.component(
               
               pUpdateRate = pUpdateRate,
               pStyle = pData['style']['header'],
               pContent = pData['content']['header']
               
            )
            
         ),
         dbc.Row(
            
            id = 'bodyRowId',
            justify = 'center',
            children = dbc.Col(
               
               style = {
                  
                  'paddingBottom' : 5,
                  'minWidth' : self.colWidth,
                  'maxWidth' : self.colWidth,
                  'backgroundColor' : '#F7F5F1'
                  
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
                           
                           pData = pData['data'],
                           pStyle = pData['style'],
                           pContent = pData['content']
                           
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
                  
         sleep(self.bodyLoadDelay)
         return self.defaultBoard
      
   
   def registerAboutMeCallback(self):
      '''  '''
   
      @application.callback(
         
         Output('backgroundVideoId', 'playing'),
         Input('bodyAccordionId', 'active_item')
         
      )
      def aboutMeCallback(i):
         '''  '''
         
         # if () <
         # else (then ) <
         if ((i) == self.body['aboutMe'].id):
            
            sleep(self.body['aboutMe'].waitVideo)
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
            
            pUpdateRate = self.database.updateRate,
            pData = self.database.get()
            
         )