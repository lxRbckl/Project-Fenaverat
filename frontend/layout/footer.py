# import <
from dash import html
import dash_bootstrap_components as dbc

from backend.resource import (
   
   socials,
   colWidth
   
)

# >


class footer:
   
   def __init__(self):
      '''  '''
      
      pass
   
   
   def component(self):
      '''  '''

      return dbc.Col(
         
         width = colWidth,
         style = {
            
            'padding' : 0,
            'backgroundColor' : '#F7F5F1'
         
         },
         children = dbc.Row(
            
            justify = 'between',
            children = [
               
               html.Div(style = {'borderBottom' : '1.5px solid #181A1B'}),
               *[
                  
                  dbc.Col(
                     
                     width = 'auto',
                     children = html.H1(
                        
                        children = i,
                        style = {
                           
                           'fontSize' : 18,
                           'fontFamily' : 'helvetica',
                           'textDecoration' : 'underline'
                           
                        }
                     
                     )
                     
                  )
                  
               for i in socials]
            ]
            
         )
         
      )
      
      # return dbc.Col(
         
      #    width = colWidth,
      #    style = {'backgroundColor' : '#F7F5F1'},
      #    children = [
            
      #       html.Div(style = {'borderBottom' : '1.5px solid #181A1B'}),
      #       *[
               
      #          html.H2(
                  
      #             children = i
                  
      #          )
               
      #       for i in socials]

      #       # html.H1(
               
      #       #    children = 'footer', 
      #       #    style = {'fontWeight' : 'bold', 'fontFamily' : 'Helvetica'})
            
      #    ]
         
      # )