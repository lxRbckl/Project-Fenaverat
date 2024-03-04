# import <
from dash import html
import dash_bootstrap_components as dbc

# >


class myProjects:
   
   def __init__(self):
      '''  '''
      
      self.id = 'b2'
      self.title = 'my projects'
      self.y = 1
   
   
   def cardsLoad(self, pIterable):
      '''  '''

      print(pIterable)
   
   
   def board(
      
      self,
      pData,
      pStyle,
      pContent
   
   ):
      '''  '''

      projects = pData['projects']
      images = pContent['myProjects']['images']
      information = pContent['myProjects']['information']
            
      self.cardsLoad(pIterable = {
         
         'images' : images,
         'information' : information,
         'projects' : {k2 : v2 for v in projects.values() for k2, v2 in v.items()}
         
      })
      
      
      return dbc.Row(
         
         style = {
            
            'backgroundColor' : '#F7F5F1'
         
         },
         children = [
            
            html.H1('ok')
            
         ]
         
      )