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
      self.title = 'my servers'
      self.cards = {
         
         'image' : self.cardImage,
         'guide' : self.cardGuide,
         'server' : self.cardServer
         
      }
   
   
   def cardServer(
      
      self,
      i,
      pStyle,
      pContent
   
   ):
      '''  '''
   
      colors = {
         
         True : '#13315C',
         False : '#134074'
         
      }
   
      return [
         
         dbc.CardHeader(
            
            style = {
               
               'border' : 'none',
               'borderRadius' : 0,
               'padding' : '10px 10px 0px 10px', 
               'border' : '3px solid {}'.format(colors[i[1]['isHost']])
               
            },
            children = dbc.Row(
               
               style = {},
               justify = 'between',
               children = [
                  
                  dbc.Col(
                     
                     width = 'auto',
                     style = {'margin' : '-5px 0px -4px -1px'},
                     children = html.H4(
                        
                        children = {
                           
                           True : lambda : i[0],
                           False : lambda : i[1]['hostname']
                           
                        }[i[1]['isHost']](),
                        style = {

                           'fontSize' : 25,
                           'color' : '#F7F5F1',
                           'fontWeight' : 'bold',
                           'fontFamily' : 'helvetica'
                           
                        }
                        
                     )
                     
                  ),
                  dbc.Col(
                     
                     width = 'auto',
                     style = {'margin' : '-5px 0px 0px 0px'},
                     children = html.Img(
                        
                        style = {
                           
                           'width' : 'auto',
                           'height' : '1.4rem'
                           
                        },
                        src = {
                           
                           True : pContent['myServers']['icon']['host'],
                           False : pContent['myServers']['icon']['swarm']
                           
                        }[i[1]['isHost']]
                        
                     )
                     
                  )
                  
               ]
               
            )
            
         ),
         dbc.CardBody(
            
            style = {
               
               'padding' : 10,
               'border' : 'none',
               'overflow' : 'hidden',
               'borderLeft' : '3px solid {}'.format(colors[i[1]['isHost']]),
               'borderRight' : '3px solid {}'.format(colors[i[1]['isHost']]),
               'borderBottom' : '3px solid {}'.format(colors[i[1]['isHost']])
               
            },
            children = html.Div(
               
               style = {'margin' : '-2px 2px 0px -2px'},
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
      
      pKey = 'myServers'
   
   ):
      '''  '''
            
      return dbc.Row(
         
         style = {

            'display' : 'grid',
            'overflow-x' : 'auto',
            'overflow-y': 'hidden',
            'scrollbar-width' : 'thin',
            
            'grid-auto-flow' : 'column',
            'padding' : '2.5px 15px 2.5px 14px',
            
            'backgroundSize' : 'cover',
            'backgroundPosition' : 'center',
            'backgroundImage' : 'url({})'.format(pContent[pKey]['background'])
         
         },
         children = self.cardsLoad(
            
            pStyle = pStyle,
            pCards = self.cards,
            pContent = pContent,
            pIterable = [
               
               *[('image', i) for i in pContent[pKey]['image']],
               *[('server', kv) for kv in pData[pKey]['host'].items()],
               *[('server', kv) for kv in pData[pKey]['swarm'].items()],
               *[('guide', kv) for kv in pContent[pKey]['guide'].items()],
               
            ]
            
         )
         
      )