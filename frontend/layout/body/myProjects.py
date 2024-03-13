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
      pContent
      
   ):
      '''  '''

      return [
         
         dbc.CardHeader(
            
            style = {
               
               'padding' : 10,
               'borderRadius' : 0,
               'border' : '1px solid #F7F5F1'
               
            },
            children = html.H4(
               
               children = i[0],
               style = {
                                    
                  'padding' : 0,                  
                  'fontSize' : 29,
                  'color' : '#F7F5F1',
                  'fontWeight' : 'bold',
                  'fontFamily' : 'helvetica',
                  'margin' : '-7px 0px -8px -1px'
                  
               }
               
            )
            
         ),
         dbc.CardBody(
            
            style = {
               
               'padding' : 10,
               'borderLeft' : '1px solid #F7F5F1',
               'borderRight' : '1px solid #F7F5F1',
               'borderBottom' : '1px solid #F7F5F1'
               
            },
            children = [
               
               html.P(
                  
                  children = j,
                  style = {
                                          
                     'fontSize' : 15,
                     'lineHeight' : 1.5,
                     'color' : '#F7F5F1',
                     'textAlign' : 'justify',
                     'fontFamily' : 'helvetica',
                     'margin' : '-6px 0px 0px 0px',
                     'padding' : '0px 0px 15px 0px'
                     
                  }
                  
               )
               
            for j in i[1]]
            
         )
         
      ]
   
   
   def cardImage(
      
      self,
      i,
      pStyle,
      pContent
      
   ):
      '''  '''

      return dbc.CardImg(
         
         src = i,
         style = {
                       
            'width' : '100%', 
            'height' : '100%',
            'borderRadius' : 0,
            'object-fit' : 'cover'
                  
         }
                  
      )
   
   
   def cardProject(
      
      self,
      i,
      pStyle,
      pContent
      
   ):
      '''  '''

      return [
         
         dbc.CardHeader(
            
            style = {
               
               'padding' : 10, 
               'border' : 'none',
               'borderRadius' : 0,
               'border' : '1px solid #F7F5F1'
            
            },
            children = [
               
               html.H4(
                  
                  children = i[0].replace('-', ' '),
                  style = {
                                          
                     'fontSize' : 29,
                     'color' : '#F7F5F1',
                     'fontWeight' : 'bold',
                     'fontFamily' : 'helvetica',
                     'margin' : '-7px 0px 0px 0px'
                     
                  }
                  
               ),
               html.P(
                  
                  children = i[1]['description'],
                  style = {
                                          
                     'fontSize' : 14,
                     'lineHeight' : 1.5,
                     'color' : '#F7F5F1',
                     'textAlign' : 'justify',
                     'fontFamily' : 'helvetica',
                     'margin' : '-4px -1px -7px 0px'
                     
                  }
                  
               )
                           
            ]
            
         ),
         dbc.CardBody(
            
            style = {
                     
               'padding' : 10,
               'border' : 'none',
               'overflow' : 'hidden',
               'borderLeft' : '1px solid #F7F5F1',
               'borderRight' : '1px solid #F7F5F1'
               
            },
            children = html.Div(
               
               style = {'margin' : '-3px 2px -2px -2px'},
               children = self.badge(
               
                  pStyle = pStyle,
                  pIterable = {
                     
                     'languages' : i[1]['languages'],
                     'packages' : i[1]['packages']
                     
                  }
               
               )
               
            )
            
         ),
         dbc.CardFooter(
            
            style = {
               
               'padding' : 10,
               'border' : 'none',
               'borderRadius' : 0,
               'border' : '1px solid #F7F5F1'
               
            },
            children = [
               
               dbc.Row(
                  
                  justify = 'between',
                  style = {'margin' : '-5px -12px -2px -12px'},
                  children = [
                     
                     # repo <
                     # wiki <
                     dbc.Col(
                        
                        width = 'auto',
                        children = html.A(

                           target = '_blank',
                           href = i[1]['url'],
                           children = html.Img(
                              
                              src = pContent['myProjects']['icon']['repo'],
                              style = {
                                 
                                 'width' : 'auto',
                                 'height' : '17px'
                                 
                              }
                              
                           )
                           
                        )
                        
                     ),
                     dbc.Col(
                        
                        width = 'auto',
                        children = html.A(
                           
                           target = '_blank',
                           href = i[1]['url'] + '/wiki',
                           children = html.Img(
                              
                              src = pContent['myProjects']['icon']['wiki'],
                              style = {
                                 
                                 'width' : 'auto',
                                 'height' : '17px'
                                 
                              }
                              
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
      
      isShuffled = True
      
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
               
               'padding' : 0,
               'width' : '18rem',
               'height' : '21rem',
               'margin' : '2.5px',
               'borderRadius' : 0,
               'background' : 'transparent',
               'border' : '1px solid #181A1B',
               'backdropFilter' : 'blur(20px)'
               
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
      
      pKey = 'myProjects'
   
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
               *[('guide', kv) for kv in pContent[pKey]['guide'].items()],
               *[('project', kv) for v in pData[pKey].values() for kv in v.items()]
               
            ]
            
         )
         
      )