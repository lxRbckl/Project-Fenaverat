# import <
from .aboutMe import aboutMe

from dash import html, dcc
from random import shuffle
import dash_bootstrap_components as dbc

# >


class myProjects(aboutMe):
   
   def __init__(self):
      '''  '''
      
      self.id = 'b3'
      self.maxHeight = 350
      self.file = 'myProjects'
      self.title = 'my projects'
      self.cardsPriority = ['guide']
      self.cards = {
         
         'guide' : self.cardGuide,
         'image' : self.cardImage,
         'project' : self.cardProject
         
      }
      
      
   def cardGuide(
      
      self,
      i,
      pStyle,
      pBorder,
      pContent,
      
      pKey = 'cardGuide',
      pFile = 'myProjects'
      
   ):
      '''  '''

      return html.Div(
         
         style = pStyle[pFile][pKey]['div'],
         children = [
            
            dbc.CardHeader(
               
               style = pStyle[pFile][pKey]['cardHeader'],
               children = html.H4(
                  
                  children = i[0],
                  style = {

                     **pStyle[pFile][pKey]['cardHeaderH4'],
                     'color' : pStyle['framework']['colorWhite']
                     
                  }
                  
               )
               
            ),
            dbc.CardBody(
               
               style = {
                  
                  'borderTop' : pBorder,
                  **pStyle[pFile][pKey]['cardBody']
               
               },
               children = [
                  
                  dcc.Markdown(
                     
                     children = j,
                     style = {
                        
                        **pStyle[pFile][pKey]['cardBodyMarkdown'],
                        'color' : pStyle['framework']['colorWhite']
                        
                     }
                     
                  )
                  
               for j in i[1]]
               
            )
            
         ]
         
      )
   
   
   def cardImage(
      
      self,
      i,
      pStyle,
      pBorder,
      pContent,
      
      pKey = 'cardImage',
      pFile = 'myProjects'
      
   ):
      '''  '''
      
      return dbc.CardImg(
         
         src = i,
         style = pStyle[pFile][pKey]['cardImg']
                  
      )
   
   
   def cardProject(
      
      self,
      i,
      pStyle,
      pBorder,
      pContent,
      
      pKey = 'cardProject'
      
   ):
      '''  '''
      
      return [
         
         dbc.CardHeader(
            
            style = pStyle[self.file][pKey]['cardHeader'],
            children = [
               
               html.H4(
                  
                  children = i[0].replace('-', ' '),
                  style = {
                                          
                     **pStyle[self.file][pKey]['cardHeaderH4'],
                     'color' : pStyle['framework']['colorWhite']
                     
                  }
                  
               ),
               dcc.Markdown(
                  
                  children = i[1]['description'],
                  style = {
                                          
                     'color' : pStyle['framework']['colorWhite'],
                     **pStyle[self.file][pKey]['cardHeaderMarkdown']
                     
                  }
                  
               )
                           
            ]
            
         ),
         dbc.CardBody(
            
            children = self.badge(
               
               pStyle = pStyle,
               pIterable = {
                  
                  'languages' : i[1]['languages'],
                  'packages' : i[1]['packages']
                  
               }
               
            ),
            style = {
               
               'borderTop' : pBorder,
               'borderBottom' : pBorder,
               **pStyle[self.file][pKey]['cardBody'],
               
            }
            
         ),
         dbc.CardFooter(
            
            style = pStyle[self.file][pKey]['cardFooter'],
            children = [
               
               dbc.Row(
                  
                  justify = 'between',
                  style = pStyle[self.file][pKey]['cardFooterRow'],
                  children = [
                     
                     # repo <
                     # wiki <
                     dbc.Col(
                        
                        width = 'auto',
                        children = html.A(

                           target = '_blank',
                           href = i[1]['url'],
                           children = html.Img(
                              
                              src = pContent[self.file]['icon']['repo'],
                              style = pStyle[self.file][pKey]['cardFooterImg']
                              
                           )
                           
                        )
                        
                     ),
                     dbc.Col(
                        
                        width = 'auto',
                        children = html.A(
                           
                           target = '_blank',
                           href = i[1]['url'] + '/wiki',
                           children = html.Img(
                              
                              src = pContent[self.file]['icon']['wiki'],
                              style = pStyle[self.file][pKey]['cardFooterImg']
                              
                           )
                           
                        )
                        
                     )
                     
                     # >
                     
                  ]
                  
               )
               
            ]
            
         )
         
      ]
   
   
   def cardsLoad(
      
      self,
      pCards,
      pStyle,
      pContent,
      pIterable,
      
      pKey = 'cardsLoad',
      pFile = 'myProjects'
      
   ):
      '''  '''
   
      rCards = {'priority' : [], 'other' : []}
      for t, i in pIterable:

         border = pStyle['framework']['borders'][{
            
            False : lambda : t,
            True : lambda : {
               
               True : 'host',
               False : 'swarm'
               
            }[i[1]['isHost']]
            
         }[t == 'server']()]
              
         {
            
            False : lambda j : rCards['other'].append(j),
            True : lambda j : rCards['priority'].append(j)
            
         }[t in self.cardsPriority](dbc.Card(
            
            children = pCards[t](
               
               i = i,
               pStyle = pStyle,
               pBorder = border,
               pContent = pContent
            
            ),
            style = {
               
               'border' : border,
               **pStyle[pFile][pKey]['card'],
               **{
                  
                  False : lambda : {},
                  True : lambda : {
                     
                     'backgroundSize' : 'cover',
                     'backgroundPosition' : 'center',
                     'background' : pContent[pFile]['backgroundCard'][i[0]]
                     
                  }
                  
               }[i[0] in pContent[pFile]['backgroundCard'].keys()]()
               
            }
            
         ))
         
         # >
            
      shuffle(rCards['other'])
      return (rCards['priority'] + rCards['other'])
         
   
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
            'background' : 'url({})'.format(pContent[self.file]['background'])
         
         },
         children = self.cardsLoad(
            
            pStyle = pStyle,
            pCards = self.cards,
            pContent = pContent,
            pIterable = [
               
               *[('image', i) for i in pContent[self.file]['image']],
               *[('guide', kv) for kv in pContent[self.file]['guide'].items()],
               *[('project', kv) for v in pData[self.file].values() for kv in v.items()]
               
            ]
            
         )
         
      )