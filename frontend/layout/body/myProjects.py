# import <
from .aboutMe import aboutMe

from dash import html
from random import shuffle
import dash_bootstrap_components as dbc

# >


class myProjects(aboutMe):
   
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

      return dbc.CardBody(
         
         style = {'padding' : 10},
         children = [
            
            html.H4(
               
               children = i[0],
               style = {
                  
                  'fontSize' : 29,
                  'color' : '#F7F5F1',
                  'fontWeight' : 'bold',
                  'fontFamily' : 'helvetica',
                  'margin' : '-7px 0px 0px -1px'
                  
               }
               
            ),
            html.Hr(style = {
               
               'padding' : 0,
               'color' : '#F7F5F1',
               'margin' : '2px 0px 4px 0px'
               
            }),
            *[
               
               html.P(
                  
                  children = j,
                  style = {
                     
                     'fontSize' : 15,
                     'color' : '#F7F5F1',
                     'textAlign' : 'justify',
                     'fontFamily' : 'helvetica',
                     'margin' : '0px 0px 7px 0px'
                     
                  }
                  
               )
               
            for j in i[1]]
            
         ]
         
      )
   
   
   def cardImage(self, i):
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
   
   
   def cardProject(self, i):
      '''  '''
   
      print(i[0]) # remove
      print(i[1]) # remove
      print('--------------') # remove
      return [
         
         dbc.CardHeader(
            
            style = {'padding' : 10, 'border' : 'none'},
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
                     
                     'fontSize' : 15,
                     'color' : '#F7F5F1',
                     'textAlign' : 'justify',
                     'fontFamily' : 'helvetica',
                     'margin' : '-3px 0px 7px 0px'
                     
                  }
                  
               ),
               html.Hr(style = {
                  
                  'padding' : 0,
                  'color' : '#F7F5F1',
                  'margin' : '0px 0px 4px 0px'
                  
               })
                           
            ]
            
         ),
         dbc.CardBody(
            
            style = {'padding' : 10, 'border' : 'none'},
            children = None
            
         ),
         dbc.CardFooter(
            
            style = {'padding' : 10, 'border' : 'none'},
            children = None
            
         )
         
      ]
   
   
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
               'borderRadius' : 0,
               'background' : 'transparent',
               'border' : '1px solid #181A1B',
               'backdropFilter' : 'blur(20px)'
               
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
            
            'backgroundSize' : 'cover',
            'backgroundPosition' : 'center',
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