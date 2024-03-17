# import <
from .framework import framework

from dash import html
import dash_bootstrap_components as dbc

# >


class footer(framework):
   
   def __init__(self): super().__init__()
   
   
   def component(
      
      self,
      pStyle,
      pContent,
      
      pKey = 'footer'
      
   ):
      '''  '''

      return dbc.Col(
         
         style = {
            
            'paddingBottom' : '0.5%',
            'minWidth' : self.colWidth,
            'maxWidth' : self.colWidth,
            'backgroundColor' : '#F7F5F1'
         
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
                                 
                                 'link' : html.A(
                                 
                                    href = v,
                                    children = i,
                                    target = '_blank',
                                    style = {
                                       
                                       'fontSize' : 16,
                                       'color' : '#181A1B',
                                       'textDecoration' : 'none',
                                       'fontFamily' : 'helvetica',
                                       'vertical-align' : 'middle'
                                       
                                    }
                                       
                                    
                                 ),
                                 'icon' : html.Img(
                                    
                                    src = v,
                                    style = {
                                       
                                       'height' : '1.2em',
                                       'marginRight' : -25,
                                       'vertical-align' : 'middle'
                                       
                                    }
                                    
                                 )
                                 
                              }[k]
                              
                           )
                           
                        for k, v in j.items()]
                        
                     )
                     
                  )
                  
               for i, j in pContent['connections'].items()]
               
            ]
            
         )
         
      )