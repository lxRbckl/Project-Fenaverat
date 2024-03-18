# import <
from .myProjects import myProjects

from dash import html
import dash_bootstrap_components as dbc

# >


class myServers(myProjects):
   
   def __init__(self):
      '''  '''
      
      super().__init__()
            
      self.id = 'b2'
      self.file = 'myServers'
      self.title = 'my servers'
      self.isHost = lambda i, j : i['borderGroup'][{
         
         True : 'host', 
         False : 'swarm'
      
      }[j]]
      self.cards = {
         
         'image' : self.cardImage,
         'guide' : self.cardGuide,
         'server' : self.cardServer
         
      }
   
   
   def cardServer(
      
      self,
      i,
      pStyle,
      pContent,
      
      pKey = 'cardServer'
   
   ):
      '''  '''
   
      return [
         
         dbc.CardHeader(
            
            style = {
               
               **pStyle[self.file][pKey]['cardHeader'],
               'border' : self.isHost(pStyle[self.file][pKey], i[1]['isHost'])
                                 
            },
            children = dbc.Row(
               
               justify = 'between',
               children = [
                  
                  # text <
                  # image <
                  dbc.Col(
                     
                     width = 'auto',
                     style = pStyle[self.file][pKey]['textCol'],
                     children = html.H4(
                        
                        children = {
                           
                           True : lambda : i[0],
                           False : lambda : i[1]['hostname']
                           
                        }[i[1]['isHost']](),
                        style = {
                           
                           **pStyle[self.file][pKey]['textH4'],
                           'color' : pStyle['framework']['colorWhite']
                           
                        }
                        
                     )
                     
                  ),
                  dbc.Col(
                     
                     width = 'auto',
                     style = pStyle[self.file][pKey]['imageCol'],
                     children = html.Img(
                        
                        style = pStyle[self.file][pKey]['imageImg'],
                        src = {
                           
                           True : pContent[self.file]['icon']['host'],
                           False : pContent[self.file]['icon']['swarm']
                           
                        }[i[1]['isHost']]
                        
                     )
                     
                  )
                  
                  # >
                  
               ]
               
            )
            
         ),
         dbc.CardBody(
            
            style = {

               **pStyle[self.file][pKey]['cardBody'],
               'borderLeft' : self.isHost(pStyle[self.file][pKey], i[1]['isHost']),
               'borderRight' : self.isHost(pStyle[self.file][pKey], i[1]['isHost']),
               'borderBottom' : self.isHost(pStyle[self.file][pKey], i[1]['isHost'])
               
            },
            children = html.Div(
               
               style = pStyle[self.file][pKey]['cardBodyDiv'],
               children = self.badge(
                  
                  pStyle = pStyle,
                  isService = True,
                  pIterable = {'service' : i[1]['service']}
                  
               )
               
            )
            
         )
         
      ]
   
   
   def board(
      
      self,
      pData,
      pStyle,
      pContent,
      
      pKey = 'board'
   
   ):
      '''  '''
            
      return dbc.Row(
         
         style = {

            **pStyle[self.file][pKey]['row'],
            'backgroundImage' : 'url({})'.format(pContent[self.file]['background'])
         
         },
         children = self.cardsLoad(
            
            pStyle = pStyle,
            pCards = self.cards,
            pContent = pContent,
            pIterable = [
               
               *[('image', i) for i in pContent[self.file]['image']],
               *[('server', kv) for kv in pData[self.file]['host'].items()],
               *[('server', kv) for kv in pData[self.file]['swarm'].items()],
               *[('guide', kv) for kv in pContent[self.file]['guide'].items()]
               
            ]
            
         )
         
      )