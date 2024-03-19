# import <
from .aboutMe import aboutMe

from dash import html
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
      pContent,
      
      pKey = 'cardGuide',
      pFile = 'myProjects'
      
   ):
      '''  '''

      return [
         
         dbc.CardHeader(
            
            style = {
               
               **pStyle[pFile][pKey]['cardHeader'],
               'border' : pStyle['framework']['borderWhite']
               
            },
            children = html.H4(
               
               children = i[0],
               style = {

                  **pStyle[pFile][pKey]['cardGuideH4'],
                  'color' : pStyle['framework']['colorWhite']
                  
               }
               
            )
            
         ),
         dbc.CardBody(
            
            style = {
               
               **pStyle[pFile][pKey]['cardBody'],
               'borderLeft' : pStyle['framework']['borderWhite'],
               'borderRight' : pStyle['framework']['borderWhite'],
               'borderBottom' : pStyle['framework']['borderWhite']
               
            },
            children = [
               
               html.P(
                  
                  children = j,
                  style = {
                     
                     **pStyle[pFile][pKey]['cardGuideP'],
                     'color' : pStyle['framework']['colorWhite']
                     
                  }
                  
               )
               
            for j in i[1]]
            
         )
         
      ]
   
   
   def cardImage(
      
      self,
      i,
      pStyle,
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
      pContent,
      
      pKey = 'cardProject'
      
   ):
      '''  '''
      
      return [
         
         dbc.CardHeader(
            
            style = {

               **pStyle[self.file][pKey]['cardHeader'],
               'border' : pStyle['framework']['borderWhite']
            
            },
            children = [
               
               html.H4(
                  
                  children = i[0].replace('-', ' '),
                  style = {
                                          
                     **pStyle[self.file][pKey]['cardProjectH4'],
                     'color' : pStyle['framework']['colorWhite']
                     
                  }
                  
               ),
               html.P(
                  
                  children = i[1]['description'],
                  style = {
                                          
                     **pStyle[self.file][pKey]['cardProjectP'],
                     'color' : pStyle['framework']['colorWhite']
                     
                  }
                  
               )
                           
            ]
            
         ),
         html.Div(
            
            style = {
               
               'height' : '100%',
               'borderLeft' : pStyle['framework']['borderWhite'],
               'borderRight' : pStyle['framework']['borderWhite'],
               'backgroundImage' : {
                  
                  False : lambda : None,
                  True : lambda : pContent[self.file]['backgroundCard'][i[0]]
                  
               }[i[0] in pContent[self.file]['backgroundCard'].keys()]()
               
            },
            children = dbc.CardBody(
               
               style = {
                  
                  'height' : '100%',
                  'backdropFilter' : 'blur(2.5px)',
                  **pStyle[self.file][pKey]['cardBody']
                  
               },   
               children = html.Div(
                  
                  style = pStyle[self.file][pKey]['cardBodyDiv'],
                  children = self.badge(
                  
                     pStyle = pStyle,
                     pIterable = {
                        
                        'languages' : i[1]['languages'],
                        'packages' : i[1]['packages']
                        
                     }
                  
                  )
                  
               )
               
            )
            
         ),
         dbc.CardFooter(
            
            style = {
               
               **pStyle[self.file][pKey]['cardFooter'],
               'border' : pStyle['framework']['borderWhite']
               
            },
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
      
      isShuffled = True,
      pKey = 'cardsLoad',
      pFile = 'myProjects'
      
   ):
      '''  '''
   
      c = 0
      rCards = []
      for t, i in pIterable:
                  
         # index <
         # add card <
         if (t in self.cardsPriority): c += 1
                  
         {
            
            # if (not priority) <
            # else (then priority) <
            False : lambda i : rCards.append(i),
            True : lambda i : rCards.insert(0, i)
            
            # >
            
         }[t in self.cardsPriority](dbc.Card(
            
            children = pCards[t](
               
               i = i,
               pStyle = pStyle,
               pContent = pContent
            
            ),
            style = {
               
               **pStyle[pFile][pKey]['card'],
               'border' : pStyle['framework']['borderBlack'],
               'backdropFilter' : pStyle['framework']['backdropFilter']
               
            }
            
         ))
         
         # >
            
      if (isShuffled):
         
         first = rCards[:c]
         last = rCards[c:]
         shuffle(last)
         
         return [*first, *last]
      
      else: return rCards
         
   
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