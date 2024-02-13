# import <
from dash import html
import dash_bootstrap_components as dbc

from backend.resource import (
   
   colWidth
   
)

# >


class header:
   
   def __init__(self):
      '''  '''
      
      pass
   
   
   def component(self):
      '''  '''

      return dbc.Col(
         
         width = colWidth,
         id = 'headerColId',
         style = {'background' : '#F7F5F1'},
         children = [
         
            dbc.Row(
               
               justify = 'between',
               children = [
                  
                  dbc.Col(
                     
                     width = 'auto',
                     children = html.H1(
                        
                        children = 'Alex Arbuckle',
                        style = {
                           
                           'fontSize' : 85,
                           'color' : '#181A1B',
                           'margin' : '0 0 -30px 0',
                           'fontFamily' : 'Helveticamazing'
                           
                        }
                        
                     )
                     
                  ),
                  dbc.Col(
                     
                     width = 'auto',
                     children = dbc.Spinner(size = 'sm')
                     
                  )
                  
               ]
               
            ),
            html.Hr()
            
            
            
            
            
            
            
            
         ]
         
      )

      # = = = = = = = =

      # return dbc.Col(
         
      #    width = colWidth,
      #    style = {
            
      #       'background' : 'red'
      #       # 'backgroundColor' : '#F7F5F1'
            
      #    },
      #    children = [
            
      #       html.Div(
            
      #          # title <
      #          # background <
      #          html.H1(
                  
      #             children = 'Alex Arbuckle',
      #             style = {
                     
      #                'fontSize' : 85,
      #                'textAlign' : 'center',
      #                'margin' : '0 0 -25px 0',
      #                'fontFamily' : 'Helveticamazing'
                     
      #             }
                  
      #          )
               
      #          # >
            
      #       ),
      #       html.Hr()
            
      #    ]
         
      # )