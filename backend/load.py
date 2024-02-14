# import <
from os import listdir
from lxrbckl.remote import requestsGet

from resource import projectPath

# >


class load:
   
   def __init__(self, pType):
      '''  '''
      
      self.links = {
         
         'style' : {
            
            'footer' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/footer.json',
            'header' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/header.json',
            'content' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/content.json',
            'template' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/template.json'
            
         },
         'data' : {
            
            'header' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/data/header.json',
            'footer' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/data/footer.json',
            'aboutMe' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/data/aboutMe.json',
            'myServers' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/data/myServers.json',
            'myProjects' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/data/myProject.json'
         
         }
         
      }
      
      rData = {}
      for k in self.links.keys():
         
         print(k)
         for i, j in self.links[k].items():
            
            print(i)
            
            
         print()
      
      
      # return {
         
      #    'local' : self.getLocal,
      #    'remote' : self.getRemote
         
      # }[pType]()
   
   
   # def getLocal(self):
   #    '''  '''

   #    rData = {}
   #    for k in self.links.keys():
         
   #       print(k)
   #       for f in listdir(projectPath + f'frontend/{k}'):
            
   #          print(f)
         
   #       print()
   
   
   # def getRemote(self):
   #    '''  '''
      
   #    rData = {}
   #    for k, v in self.links.items():
         
   #       pass


x = load(pType = 'local')