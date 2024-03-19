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
      self.file = 'framework'
      self.defaultBoard = 'b1'
      self.bodyLoadDelay = 1.5
      
      # >

   
   def framework(self):
      '''  '''

      return html.Div(
         
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
      pStyle,
      pContent,
      pIntervalRate
      
   ):
      '''  '''
            
      return [
         
         # header <
         # body <
         # footer <
         dbc.Row(
            
            justify = 'center',
            children = self.header.component(
               
               pStyle = pStyle,
               pContent = pContent,
               pIntervalRate = pIntervalRate
               
            )
            
         ),
         dbc.Row(
            
            id = 'bodyRowId',
            justify = 'center',
            children = dbc.Col(
               
               style = {
                  
                  'minWidth' : self.colWidth,
                  'maxWidth' : self.colWidth,
                  **pStyle[self.file]['bodyCol'],
                  'background' : pStyle[self.file]['colorWhite']
                  
               },
               children = dbc.Accordion(
                  
                  flush = True,
                  active_item = None,
                  id = 'bodyAccordionId',
                  style = {
                                          
                     'borderTop' : pStyle[self.file]['borderBlack'],
                     'borderBottom' : pStyle[self.file]['borderBlack']
                     
                  },
                  children = [
                     
                     dbc.AccordionItem(
                        
                        item_id = v.id,
                        title = v.title,
                        children = v.board(
                           
                           pData = pData,
                           pStyle = pStyle,
                           pContent = pContent
                           
                        )
                        
                     )
                     
                  for k, v in (self.body).items()]
                  
               )
               
            )
            
         ),
         dbc.Row(
            
            justify = 'center',
            children = self.footer.component(
               
               pStyle = pStyle,
               pContent = pContent
               
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
         
         Output('frameworkDivId', 'style'),
         Output('frameworkDivId', 'children'),
         Input('frameworkIntervalId', 'n_intervals')
         
      )
      def intervalCallback(i):
         '''  '''

         data, style, content = self.database.get().values()
         
         return [
            
            {
               
               **style[self.file]['frameworkDiv'],
               'background' : style[self.file]['colorBlack']
               
            },
            self.components(
               
               pData = data,
               pStyle = style,
               pContent = content,
               pIntervalRate = self.database.intervalRate
               
            )
            
         ]