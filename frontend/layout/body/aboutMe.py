# import <
from dash import dcc, html
from dash_player import DashPlayer
import dash_bootstrap_components as dbc

# >


class aboutMe:
   
   def __init__(self):
      '''  '''
      
      self.id = 'b1'   
      self.waitVideo = 2
      self.file = 'aboutMe'
      self.title = 'about me'
   
   
   def badge(
      
      self,
      pStyle,
      pIterable,
      
      pKey = 'badge',
      pFile = 'aboutMe',
      isService = False
      
   ):
      '''  '''

      return [
                     
            dbc.Badge(
               
               color = None,
               text_color = None,
               children = i.replace('-', ' ') if (i) else None,
               style = {
                  
                  **pStyle[pFile][pKey]['badge'],
                  'color' : pStyle['framework']['colorBlack'],
                  'background' : pStyle[pFile][pKey]['colorGroup'][k],
                  **pStyle[pFile][pKey]['type'][{
                     
                     False : 'other',
                     True : 'service'
                     
                  }[isService]]
                  
               }
               
            )
         
      for k, v in pIterable.items() for i in v]
         
   
   def board(
      
      self,
      pData,
      pStyle,
      pContent,
      
      pKey = 'board'
   
   ):
      '''  '''

      return html.Div(
         
         style = pStyle[self.file][pKey]['div'],
         children = [
            
            DashPlayer(
               
               muted = True,
               width = '110%',
               height = 'auto',
               playing = False,
               id = 'backgroundVideoId',
               url = pContent[self.file]['background'],
               style = pStyle[self.file][pKey]['DashPlayer']
               
            ),
            dbc.Row(
               
               style = pStyle[self.file][pKey]['row'],
               children = [
                  
                  # title <
                  # content <
                  # ecosystem <
                  dbc.Row(
                     
                     style = pStyle[self.file][pKey]['titleRow'],
                     children = [
                        
                        dbc.Col(width = 4),
                        dbc.Col(
                           
                           width = 8,
                           style = {
                              
                              **pStyle[self.file][pKey]['titleCol'],
                              'border' : pStyle['framework']['borderBlack'],
                              'backdropFilter' : pStyle['framework']['backdropFilter']
                              
                           },
                           children = html.H1(
                              
                              children = pContent[self.file]['title'],
                              style = {

                                 **pStyle[self.file][pKey]['titleH1'],
                                 'color' : pStyle['framework']['colorBlack']
                                 
                              }
                              
                           )
                           
                        )
                        
                     ]
                     
                  ),
                  *[
                     
                     dbc.Row(
                        
                        style = pStyle[self.file][pKey]['contentRow'],
                        children = [
                           
                           dbc.Col(width = 4),
                           dbc.Col(
                              
                              style = {
                                 
                                 **pStyle[self.file][pKey]['contentCol'],
                                 'borderLeft' : pStyle['framework']['borderBlack'],
                                 'borderRight' : pStyle['framework']['borderBlack'],
                                 'borderBottom' : pStyle['framework']['borderBlack'],
                                 'backdropFilter' : pStyle['framework']['backdropFilter']
                                 
                              },
                              children = dcc.Markdown(
                                 
                                 children = i,
                                 style = {
                                    
                                    'color' : pStyle['framework']['colorBlack'],
                                    **pStyle[self.file][pKey]['contentMarkdown']
                                    
                                 }
                                 
                              )
                              
                           )
                           
                        ]
                        
                     )
                     
                  for i in pContent[self.file]['content']],
                  dbc.Row(
                     
                     style = pStyle[self.file][pKey]['ecosystemRow'],
                     children = [
                        
                        dbc.Col(width = 4),
                        dbc.Col(
                           
                           width = 8,
                           style = {
                              
                              **pStyle[self.file][pKey]['ecosystemCol'],
                              'borderLeft' : pStyle['framework']['borderBlack'],
                              'borderRight' : pStyle['framework']['borderBlack'],
                              'borderBottom' : pStyle['framework']['borderBlack'],
                              'backdropFilter' : pStyle['framework']['backdropFilter']
                              
                           },
                           children = html.Div(
                              
                              style = pStyle[self.file][pKey]['ecosystemDiv'],
                              children = self.badge(
                                 
                                 pStyle = pStyle,
                                 pIterable = pContent[self.file]['ecosystem']
                                 
                              )
                              
                           )
                           
                        )
                        
                     ]
                     
                  )
                  
                  # >
                  
               ]

            )
            
         ]
         
      )