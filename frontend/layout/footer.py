# import <
from .framework import framework

from dash import html
import dash_bootstrap_components as dbc

# >


class footer(framework):
   
   def __init__(self): 
      
      super().__init__()
      self.file = 'footer'
   
   
   def component(
      
      self,
      pStyle,
      pContent,
      
      pKey = 'component'
      
   ):
      '''  '''

      return dbc.Col(
         
         style = {
            
            'minWidth' : self.colWidth,
            'maxWidth' : self.colWidth,
            **pStyle[self.file][pKey]['col'],
            'background' : pStyle['framework']['colorWhite']
         
         },
         children = dbc.Row(
            
            justify = 'between',
            children = [
               
               *[
                  
                  dbc.Col(
                     
                     width = 'auto',
                     children = dbc.Row(
                        
                        justify = 'between',
                        children = [
                           
                           dbc.Col(
                              
                              width = 'auto',
                              children = {
                                 
                                 'icon' : html.Img(
                                    
                                    src = v,
                                    style = {
                                       
                                       'color' : 'blue',
                                       'background' : 'red',
                                       **pStyle[self.file][pKey]['colIcon'],
                                       'backgroundColor' : pStyle['framework']['colorWhite']
                                    
                                    }
                                    
                                 ),
                                 'link' : html.A(
                                 
                                    href = v,
                                    children = i,
                                    target = '_blank',
                                    style = {
                                       
                                       **pStyle[self.file][pKey]['colLink'],
                                       'color' : pStyle['framework']['colorBlack']
                                       
                                    }
                                    
                                 )
                                 
                              }[k]
                              
                           )
                           
                        for k, v in j.items()]
                        
                     )
                     
                  )
                  
               for i, j in pContent[self.file]['connections'].items()]
               
            ]
            
         )
         
      )