# import <
from dash import html
from random import shuffle
import dash_bootstrap_components as dbc

# >


class myProjects:
   
   def __init__(self):
      '''  '''
      
      self.id = 'b2'
      self.maxHeight = 350
      self.title = 'my projects'
      self.cardsPriority = ['guide']
      self.cards = {
         
         'guide' : self.cardGuide,
         'image' : self.cardImage,
         'project' : self.cardProject
         
      }
      
      
   def cardGuide(self, i):
      '''  '''
   
      return None
   
   
   def cardImage(self, i):
      '''  '''

      return dbc.CardImg(
         
         src = i,
         style = {
            
            'background' : 'blue',
            
            'padding' : 2.5,
            'width' : '100%', 
            'height' : '100%',
            'borderRadius' : 0,
            'object-fit' : 'cover'
                  
         }
                  
      )
   
   
   def cardProject(self, i):
      '''  '''
   
      return None
   
   
   def cardsLoad(
      
      self,
      pCards,
      pIterable
      
   ):
      '''  '''
   
      rCards = []
      for t, i in pIterable:
         
         {
            
            # if (not priority) <
            # else (then priority) <
            False : lambda i : rCards.append(i),
            True : lambda i : rCards.insert(0, i)
            
            # >
            
         }[t in self.cardsPriority](dbc.Card(
            
            children = pCards[t](i),
            style = {
               
               'padding' : 0,
               'width' : '18rem',
               'height' : '21rem',
               'margin' : '2.5px',
               'background' : 'red',
               'borderRadius' : 0
               
            }
            
         ))
      
      return rCards
   
   
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
            
            'object-fit' : 'cover',
            'backgroundImage' : 'url({})'.format(pContent[pKey]['background'])
         
         },
         children = self.cardsLoad(
            
            pCards = self.cards,
            pIterable = [
               
               *[('image', i) for i in pContent[pKey]['image']],
               *[('guide', kv) for kv in pContent[pKey]['guide'].items()],
               *[('project', kv) for v in pData[pKey].values() for kv in v.items()]
               
            ]
            
         )
         
      )