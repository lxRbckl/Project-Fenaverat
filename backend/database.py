# import <
from lxrbckl.local import fileGet
from lxrbckl.remote import requestsGet

# >


class database:
   
   def __init__(self):
      '''  '''
      
      self.updateRate = 30
      self.developerMode = True
      self.intervalRate = (60000 * self.updateRate)
      self.links = {
         
         'data' : {
            
            'myProjects' : 'https://raw.githubusercontent.com/lxRbckl/Project-Heimir/Project-Heimir-2/data.json',
            'myServers' : 'https://raw.githubusercontent.com/lxRbckl/Project-Acta-Mea/Project-Acta-Mea-5/data.json'
            
         },
         'style' : {
            
            'footer' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/footer.json',
            'header' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/header.json',
            'aboutMe' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/aboutMe.json',
            'framework' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/framework.json',
            'myServers' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/myServers.json',
            'myProjects' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/myProjects.json'
            
         },
         'content' : {
            
            'header' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/content/header.json',
            'footer' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/content/footer.json',
            'aboutMe' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/content/aboutMe.json',
            'myServers' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/content/myServers.json',
            'myProjects' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/content/myProjects.json'
         
         }
         
      }
      
      
   def get(self):
      '''  '''
      
      rData = {}
      for k1 in (self.links).keys():
         
         rData[k1] = {}
         for k2, v in (self.links[k1]).items():

            rData[k1][k2] = {
                                 
               # if (data) <
               # else (then style/content) <
               False : requestsGet(v),
               True : {
                  
                  False : lambda : requestsGet(v),
                  True : lambda : fileGet(f'frontend/{k1}/{k2}.json')
               
               }[self.developerMode]()
               
               # >
               
            }[k1 in ['style', 'content']]
                     
      return rData