# import <
from dash import (dcc, html)
import dash_bootstrap_components as dbc
from dash.dependencies import (Input, Output)

from backend.resource import application

# >


def fTemplate():
   '''  '''
   
   return html.Div(
      
      style = {
         
         
         
      },
      children = [
         
         # header <
         # body <
         # footer <
         dbc.Row(
            
            justify = 'center',
            children = None
            
         ),
         dbc.Row(
            
            justify = 'center',
            children = [
               
               # dbc.Col(children = 'demo', width = '4') #
               
            ]
         ),
         dbc.Row(
            
            justify = 'center',
            children = None
            
         )
         
         # >
         
      ]
      
   )