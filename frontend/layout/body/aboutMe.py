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
      self.maxHeight = 515
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
               'background' : pStyle['framework']['badgeColors'][k],
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
            
            html.Img(
               
               style = {
                  
                  'width' : '100%',
                  'maxHeight' : self.maxHeight
                  
               },
               src = pContent[self.file]['coverPhoto']
               
            ),
            dbc.Row(
               
               style = pStyle[self.file][pKey]['row'],
               children = [
                  
                  dbc.Col(
                     
                     width = 4,
                     children = DashPlayer(
                        
                        muted = True,
                        width = '300px',
                        height = '300px',
                        playing = False,
                        id = 'profileVideoId',
                        url = pContent[self.file]['profileVideo'],
                        style = {
                           
                           **pStyle[self.file][pKey]['dashPlayer'],
                           'border' : pStyle['framework']['borderBlack'],
                           'background' : pStyle['framework']['colorBlack']
                           
                        }
                        
                     )
                  
                  ),
                  dbc.Col(
                     
                     width = 8,
                     style = {
                        
                        'maxHeight' : self.maxHeight,                        
                        **pStyle[self.file][pKey]['col'],
                        'border' : pStyle['framework']['borderBlack'],
                        'backdropFilter' : pStyle['framework']['backdropFilter']
                        
                     },
                     children = [
                        
                        # stack <
                        # content <
                        # ecosystem <
                        dbc.Stack(
                           
                           gap = 2,
                           direction = 'horizontal',
                           style = {
                              
                              **pStyle[self.file][pKey]['stack'],
                              'borderBottom' : pStyle['framework']['borderBlack']
                              
                           },
                           children = [
                              
                              # title <
                              # symbols <
                              html.H1(
                                 
                                 children = pContent[self.file]['title'],
                                 style = {
                                    
                                    'fontWeight' : '900',
                                    **pStyle[self.file][pKey]['titleH1'],
                                    'color' : pStyle['framework']['colorBlack']
                                 
                                 }
                                 
                              ),
                              *[
                                 
                                 html.Img(
                                    
                                    src = i,
                                    style = {
                                       
                                       **pStyle[self.file][pKey]['symbolsImg'],
                                       'border' : pStyle['framework']['borderBlack']
                                       
                                    }
                                    
                                 )
                                 
                              for i in pContent[self.file]['symbols']]
                              
                              # >
                              
                           ]
                           
                        ),
                        *[
                           
                           dcc.Markdown(
                              
                              children = i,
                              style = {
                                 
                                 
                                 'color' : pStyle['framework']['colorBlack'],
                                 **pStyle[self.file][pKey]['contentMarkdown']
                                 
                              }
                              
                           )
                           
                        for i in pContent[self.file]['content']],
                        html.Div(
                           
                           style = {
                              
                              **pStyle[self.file][pKey]['ecosystemDiv'],
                              'borderTop' : pStyle['framework']['borderBlack']
                           
                           },
                           children = self.badge(
                              
                              pStyle = pStyle,
                              pIterable = pContent[self.file]['ecosystem']
                              
                           )
                           
                        )
                        
                        # >
                        
                     ]
                     
                  )
                  
               ]

            )
            
         ]
         
      )