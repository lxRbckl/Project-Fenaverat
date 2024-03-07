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
      pStyle,
      pIterable
      
   ):
      '''  '''
   
      return [
         
         dbc.Badge(
            
            color = None,
            children = i,
            text_color = None,
            style = {
               
               'color' : '#181A1B',
               'fontFamily' : 'helvetica',
               'margin' : '1px 2px 1px 2px',
               'border' : '1px solid #F7F5F1',
               'backgroundColor' : {
                  
                  '...' : '#C6AF97',
                  'package' : '#AA7F74',
                  'language' : '#96867F'
                  
               }[t]
               
            }
            
         )
         
      for t, i in pIterable]
   
   
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
               style = {'margin' : '0 0 -5px 0'}, # <- was -5%
               url = pContent['aboutMe']['background']
               
            ),
            dbc.Row(
               
               style = {
                  
                  'top' : 0,
                  'margin' : 0,
                  'width' : '100%',
                  'padding' : '5px',
                  'position' : 'absolute'
                  
               },
               children = [
                  
                  # title <
                  # content <
                  # ecosystem <
                  dbc.Row(
                     
                     style = {'padding' : 0, 'margin' : 0},
                     children = [
                        
                        dbc.Col(width = 4),
                        dbc.Col(
                           
                           width = 8,
                           style = {
                                                            
                              'margin' : 0,
                              'padding' : 5,
                              'border' : '1px solid #181A1B',
                              'backdropFilter' : 'blur(20px)'
                              
                           },
                           children = html.H1(
                              
                              children = pContent['aboutMe']['title'],
                              style = {

                                 'padding' : 0,
                                 'fontSize' : 38,
                                 'color' : '#181A1B',
                                 'marginLeft' : '-3px',
                                 'fontFamily' : 'helvetica',
                                 'margin' : '-7px 0px -10px -1px'
                                 
                              }
                              
                           )
                           
                        )
                        
                     ]
                     
                  ),
                  *[
                     
                     dbc.Row(
                        
                        style = {'margin' : 0, 'padding' : 0},
                        children = [
                           
                           dbc.Col(width = 4),
                           dbc.Col(
                              
                              style = {
                                 
                                 'padding' : 5,
                                 'margin' : '0px 0px 0px 0px',
                                 'backdropFilter' : 'blur(20px)',
                                 'borderLeft' : '1px solid #181A1B',
                                 'borderRight' : '1px solid #181A1B',
                                 'borderBottom' : '1px solid #181A1B'
                                 
                              },
                              children = html.P(
                                 
                                 children = i,
                                 style = {
                                    
                                    'fontSize' : 15,
                                    'color' : '#181A1B',
                                    'textAlign' : 'justify',
                                    'fontFamily' : 'helvetica',
                                    'margin' : '-6px 0px -6px -1px'
                                    
                                 }
                                 
                              )
                              
                           )
                           
                        ]
                        
                     )
                     
                  for i in pContent['aboutMe']['content']],
                  dbc.Row(
                     
                     style = {'margin' : 0, 'padding' : 0},
                     children = [
                        
                        dbc.Col(width = 4),
                        dbc.Col(
                           
                           width = 8,
                           style = {
                              
                              'margin' : '0px 0px 0px 0px',
                              'padding' : '3px 1px 4px 3px',
                              'backdropFilter' : 'blur(20px)',
                              'borderLeft' : '1px solid #181A1B',
                              'borderRight' : '1px solid #181A1B',
                              'borderBottom' : '1px solid #181A1B'
                              
                           },
                           children = self.badge(

                              pStyle = pStyle,
                              pIterable = pContent['aboutMe']['ecosystem']
                              
                           )
                           
                        )
                        
                     ]
                     
                  )
                  
                  # >
                  
               ]

            )
            
         ]
         
      )