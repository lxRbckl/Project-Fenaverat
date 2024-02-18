# import <
from dash import html
from dash_player import DashPlayer
import dash_bootstrap_components as dbc

# >


class aboutMe:
   
   def __init__(self):
      '''  '''
      
      self.id = 'b1'
      self.title = 'about me'
   
   
   def board(
      
      self,
      pStyle,
      pContent
   
   ):
      '''  '''

      return html.Div(
         
         style = {'position' : 'relative'},
         children = [
            
            # html.Video(
               
            #    muted = True,
            #    autoPlay = True,
            #    controls = True,
            #    id = 'backgroundVideoId',
            #    src = pContent['background'],
            #    style = {
                  
            #       'width' : '100vw',
            #       'height' : '40vh',
            #       'display' : 'block',
            #       'object-fit' : 'cover'
                  
            #    }
               
            # ),
            
            DashPlayer(
               
               muted = True,
               width = '110%',
               height = 'auto',
               playing = False,
               id = 'backgroundVideoId',
               url = pContent['background'],
               style = {
                  
                  'margin' : '0 0 -1% 0',
                  
               
               }
               
            ),
            html.Div(
               
               style = {
                  
                  'top' : 0,
                  'width' : '100%',
                  'padding' : '1%',
                  'height' : '40vh',
                  'position' : 'absolute'
                  
               },
               children = [
                  
                  # <
                  # <
                  dbc.Row(
                     
                     children = [
                        
                        dbc.Col(width = 4),
                        *[
                           
                           dbc.Col(
                              
                              width = 4,
                              children = html.P(
                                 
                                 children = i,
                                 style = {
                                    
                                    'color' : '#181A1B',
                                    'textAlign' : 'justify',
                                    'backdropFilter' : 'blur(15px)',
                                    'borderBottom' : '1px solid #181A1B'
                                    
                                 }
                                 
                              )
                              
                           )
                           
                        for i in pContent['information']]
                        
                     ]
                     
                  ),
                  dbc.Row(
                     
                     children = [
                        
                        dbc.Col(width = 4),
                        dbc.Col(
                           
                           width = 3,
                           children = html.Div(
                              
                              children = html.H1('ok'), # <
                              style = {
                                 
                                 'backdropFilter' : 'blur(15px)',
                                 'borderTop' : '1px solid #181A1B'
                              
                              }
                              
                           )
                           
                        ),
                        dbc.Col(
                           
                           width = 5,
                           children = html.Div(
                              
                              children = html.H1('ok'), # <
                              style = {
                                 
                                 'backdropFilter' : 'blur(15px)',
                                 'borderTop' : '1px solid #181A1B'
                              
                              }
                              
                           )
                           
                        )
                        
                     ]
                     
                  )
                  
                  # >
                  
               ]
               
            )
            
         ]
         
      )