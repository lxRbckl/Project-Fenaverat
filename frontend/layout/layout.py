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
      
      # attributes <
      # objects <
      self.colWidth = 8
      self.defaultBoard = 'b1'
      
      self.database = None
      self.header = None
      self.footer = None
      self.body = []
      
      # >
      
   # def loadHeader(self, pData):
   #    '''  '''
      
   #    return dbc.Row(
         
   #       justify = 'center',
   #       children = self.header.component(
            
   #          *self.database.getStatus(),
   #          pStyle = pData['style']['header'],
   #          pContent = pData['content']['header']
            
   #       )
         
   #    )
   
   
   # def loadBody(self, pData):
   #    '''  '''
      
   #    return dbc.Row(
         
   #       justify = 'center',
   #       children = dbc.Col(
            
   #          width = self.colWidth,
   #          style = {
               
   #             'background' : '#F7F5F1',
   #             'paddingBottom' : '0.5%'
            
   #          },
   #          children = dbc.Accordion(
               
   #             flush = True,
   #             active_item = None,
   #             id = 'bodyAccordionId',
   #             style = {
                  
   #                'borderTop' : '1px solid #181A1B',
   #                'borderBottom' : '1px solid #181A1B'
                  
   #             },
   #             children = [
                  
   #                dbc.AccordionItem(
                     
   #                   item_id = i.id,
   #                   title = i.title,
   #                   style = i.style,
   #                   children = i.board()
                     
   #                )
                  
   #             for i in self.body]
               
   #          )
            
   #       )
         
   #    )

   
   # def loadFooter(self, pData):
   #    '''  '''

   #    return dbc.Row(
         
   #       justify = 'center',
   #       children = self.footer.component(
            
   #          pStyle = pData['style']['footer'],
   #          pContent = pData['content']['footer']
            
   #       )
         
   #    )
   
   
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
               interval = (60000 * self.database.refreshRate)
               
            ),
            html.Div(
               
               children = None,
               id = 'templateDivId'
            
            )
                        
         ]
         
      )
   
   
   # def components(self, pData):
   #    '''  '''
   
   #    re
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
   
   
   # def registerCallbacks(self):
   #    '''  '''
      
      # @application.callback(
         
      #    Output('templateDivId', 'children'),
      #    Input('templateIntervalId', 'n_intervals')
         
      # )
      # def intervalCallback(i):
      #    '''  '''
         
      #    data = self.database.getLocal()
         
      #    return [
            
      #       self.loadHeader(data),
      #       self.loadBody(data),
      #       self.loadFooter(data)
            
      #    ]
      
      
      # @application.callback(
         
      #    Output('', ''),
      #    Input('', '')
         
      # )
      # def bodyCallback(i):
      #    '''  '''
         
      #    print(i)