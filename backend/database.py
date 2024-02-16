# import <
from lxrbckl.local import fileGet
from lxrbckl.remote import requestsGet

# >


class database:
   
   def __init__(self):
      '''  '''
      
      self.links = {
         
         'style' : {
            
            'footer' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/footer.json',
            'header' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/header.json',
            'content' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/content.json',
            'template' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/style/template.json'
            
         },
         'content' : {
            
            'header' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/data/header.json',
            'footer' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/data/footer.json',
            'aboutMe' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/data/aboutMe.json',
            'myServers' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/data/myServers.json',
            'myProjects' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat/Project-Fenaverat-3/frontend/data/myProject.json'
         
         }
         
      }
      
      self.rate = 30
      self.status = self.links
      self.developerMode = True
      self.intervalRate = (60000 * self.rate)
      
      
   def get(self):
      '''  '''
      
      rData = {}
      for k1 in (self.links).keys():
         
         rData[k1] = {}
         for k2, v in (self.links[k1]).items():
        
            # if (default) <
            # else (then developer) <
            if (not self.developerMode):
            
               # try (load remotely) <
               # except (then local) <
               try:
                  
                  f = requestsGet(v)
                  self.status[k1][k2] = 'remote'
                              
               except:
                  
                  self.status[k1][k2] = 'local'
                  f = fileGet(f'frontend/{k1}/{k2}.json')
               
               # >
                           
            else:
               
               self.status[k1][k2] = 'local'
               f = fileGet(f'frontend/{k1}/{k2}.json')
            
            # >
         
            rData[k1][k2] = f
         
      return rData