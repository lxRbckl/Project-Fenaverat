# import <
from .myProjects import myProjects

from dash import html
import dash_bootstrap_components as dbc

# >


class myServers(myProjects):
   
   def __init__(self):
      '''  '''
      
      super().__init__()
      
      self.id = 'b3'
      self.title = 'my servers'
      
   
   
   
   
   def board(
      
      self,
      pData,
      pStyle,
      pContent
   
   ):
      '''  '''
      
      return dbc.Row(
         
         style = {},
         children = [
            
            
            
         ]
         
      )