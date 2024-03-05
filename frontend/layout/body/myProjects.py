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
         
         'project' : self.cardProject,
         'picture' : self.cardPicture,
         'guide' : self.cardGuide
         
      }
      
      
   def cardGuide(i):
      '''  '''
   
      pass
   
   
   def cardPicture(i):
      '''  '''
   
      pass
   
   
   def cardProject(i):
      '''  '''
   
      pass
   
   
   def cardsLoad(
      
      self,
      pCards, # <- possible removal LATER
      pIterable
      
   ):
      '''  '''
   
      rCards = []
      for t, i in pIterable:
         
         rCards.append(html.H1('ok'))
      
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
            'overflow-x': 'auto',
            'overflow-y': 'hidden',
            'scrollbar-width' : 'thin',
            'grid-auto-flow' : 'column',
            
            'backgroundSize' : 'cover',
            'backgroundRepeat' : 'noRepeat',
            'backgroundPosition' : 'center',
            'backgroundImage' : 'url({})'.format(pContent[pKey]['background'])
         
         },
         children = [
            
            dbc.Col(
               
               width = 'auto',
               children = c,
               style = {


                  'display' : 'grid'

               }
               
            )
            
         for c in self.cardsLoad(
            
            pCards = self.cards,
            pIterable = [
            
               *[('picture', i) for i in pContent[pKey]['picture']],
               *[('guide', kv) for kv in pContent[pKey]['guide'].items()],
               *[('project', kv) for v in pData[pKey].values() for kv in v.items()]
               
            ]
            
         )]
         
      )