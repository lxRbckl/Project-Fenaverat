# import <
from backend.load import load
from frontend.layout.header import header
from frontend.layout.footer import footer
from frontend.layout.body.aboutMe import aboutMe
from frontend.layout.body.myServers import myServers
from frontend.layout.body.myProjects import myProjects
from backend.resource import (
   
   colWidth,
   refreshRate,
   application
   
)

from time import sleep
from dash import (dcc, html)
import dash_bootstrap_components as dbc
from dash.dependencies import (Input, Output)

# >


class template:
   
   
   def __init__(self):
      '''  '''
      
      self.load = load()
      self.header = header()
      self.footer = footer()
      self.body = [
         
         aboutMe(),
         myProjects(),
         myServers()
         
      ]
      
      
   def loadHeader(
      
      self, 
      pData,
      pStatus
   
   ):
      '''  '''
      
      return dbc.Row(
         
         justify = 'center',
         children = self.header.component(
            
            pStatus = pStatus,
            pStyle = pData['style']['header']
            pContent = pData['data']['header'],
            
         )
         
      )
   
   
   def loadBody(
      
      self, 
      pData,
      pStyle
   
   ):
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
                  
               for i in self.body]
               
            )
            
         )
         
      )

   
   def loadFooter(
      
      self, 
      pData,
      pStyle
   
   ):
      '''  '''

      return dbc.Row(
         
         justify = 'center',
         children = self.footer.component(
            
            pStyle = pData['style']['footer'],
            pContent = pData['data']['footer']
            
         )
         
      )
   
   
   def component(self):
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
               interval = (60000 * refreshRate)
               
            ),
            html.Div(
               
               children = None,
               id = 'templateDivId'
            
            )
                        
         ]
         
      )
   
   
   def registerCallbacks(self):
      '''  '''
      
      @application.callback(
         
         Output('templateDivId', 'children'),
         Input('templateIntervalId', 'n_intervals')
         
      )
      def intervalCallback(i):
         '''  '''
         
         data, status = self.load.get()
         
         return [
            
            self.loadHeader(
               
               pData = data,
               pStatus = status
               
            ),
            self.loadBody(data),
            self.loadFooter(data)
            
         ]
      
      
      # @application.callback(
         
      #    Output('', ''),
      #    Input('', '')
         
      # )
      # def bodyCallback(i):
      #    '''  '''
         
      #    print(i)
      
      
      
      
      
      # TODO
      # we need to deal with the load methods.
      # in the parameters, we need to break our parameters apart
      # we need to break them apart into (style and data) and pass them into loads