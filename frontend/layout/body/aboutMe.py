# import <
from dash import html
from dash_player import DashPlayer
import dash_bootstrap_components as dbc

# >


class aboutMe:
   
   def __init__(self):
      '''  '''
      
      self.id = 'b1'   
      self.waitVideo = 2
      self.title = 'about me'
   
   
   def badge(
      
      self,
      pList,
      pColor,
      pTextColor
   
   ):
      '''  '''
   
      return [
         
         dbc.Badge(
            
            children = i,
            color = pColor,
            text_color = pTextColor,
            class_name = 'border me-1'
            
         )
         
      for i in pList]
   
   
   def board(
      
      self,
      pData,
      pStyle,
      pContent
   
   ):
      '''  '''

      return html.Div(
         
         style = {'position' : 'relative'},
         children = [
            
            DashPlayer(
               
               muted = True,
               width = '110%',
               height = 'auto',
               playing = False,
               id = 'backgroundVideoId',
               style = {'margin' : '0 0 -1% 0'},
               url = pContent['aboutMe']['background']
               
            ),
            html.Div(
               
               style = {
                  
                  'top' : 0,
                  'width' : '100%',
                  'padding' : '1%',
                  'position' : 'absolute'
                  
               },
               children = [
                  
                  # title <
                  # body <
                  # footer <
                  dbc.Row(
                     
                     children = [
                        
                        dbc.Col(width = 4),
                        dbc.Col(
                           
                           width = 8,
                           children = html.H1(
                              
                              children = pContent['aboutMe']['title'],
                              style = {
                                 
                                 'color' : '#181A1B',
                                 'fontFamily' : 'helvetica',
                                 'backdropFilter' : 'blur(15px)',
                                 'borderTop' : '1px solid #181A1B'
                                 
                              }
                           
                           )
                           
                        )
                        
                     ]
                     
                  ),
                  dbc.Row(
                     
                     children = [
                        
                        dbc.Col(width = 4),
                        *[
                           
                           dbc.Col(
                              
                              width = 4,
                              children = html.P(
                                 
                                 children = i,
                                 style = {
                                    
                                    'fontSize' : 15,
                                    'color' : '#181A1B',
                                    'textAlign' : 'justify',
                                    'backdropFilter' : 'blur(15px)',
                                    'borderBottom' : '1px solid #181A1B'
                                    
                                 }
                                 
                              )
                              
                           )
                           
                        for i in pContent['aboutMe']['body']]
                        
                     ]
                     
                  ),
                  dbc.Row(
                     
                     children = [
                        
                        dbc.Col(width = 4),
                        *[
                           
                           dbc.Col(
                              
                              width = v['width'],
                              children = html.Div(
                                 
                                 style = {
                                    
                                    'paddingTop' : '1%',
                                    'backdropFilter' : 'blur(15px)',
                                    'borderTop' : '1px solid #181A1B'
                                    
                                 },
                                 children = self.badge(
                                    
                                    pList = v['list'],
                                    pColor = '#181A1B',
                                    pTextColor = '#F7F5F1'
                                    
                                 )                                 
                                 
                              )
                              
                           )
                           
                        for k, v in pContent['aboutMe']['footer'].items()]
                        
                     ]
                     
                  )
                  
                  # >
                  
               ]
               
            )
            
         ]
         
      )