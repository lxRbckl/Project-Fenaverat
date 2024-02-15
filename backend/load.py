# import <
from lxrbckl.local import fileGet
from lxrbckl.remote import requestsGet

# >


class load:
   
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
      

   def get(self):
      '''  '''
      
      rData = {}
      rStatus = True
      for k1 in self.links.keys():
         
         rData[k1] = {}
         for k2, v in self.links[k1].items():
            
            # # try (remote) <
            # # except (then local) <
            # try: file = requestsGet(v)
            # except: 
               
            #    rStatus = False
            #    file = fileGet(f'frontend/{k1}/{k2}.json')
            
            # # >
            
            file = fileGet(f'frontend/{k1}/{k2}.json')
            
            rData[k1][k2] = file
         
      return [rData, rStatus]