# import <
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
            
            'header' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/data/header.json',
            'footer' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/data/footer.json',
            'aboutMe' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/data/body/aboutMe.json',
            'myServer' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/data/body/myServer.json',
            'myProject' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/data/body/myProject.json'
         
         }
         
      }
      
      # try (if load successful) <
      # except (then failed to load) <
      try:
         
         return {
            
            'local' : self.getLocal,
            'remote' : self.getRemote
            
         }[pType]()
      
      except: return False
      
      # >
   
   
   def getLocal(self):
      '''  '''
      
      rData = {}
      print(projectPath)
   
   
   def getRemote(self):
      '''  '''
      
      pass


x = load(pType = 'local')