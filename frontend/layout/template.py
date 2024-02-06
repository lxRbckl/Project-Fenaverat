# import <
from dash import (dcc, html)
from dash.dependencies import (Input, Output)

# >


def fTemplate():
   '''  '''
   
   return html.Div(
      
      children = [
         
         html.Img(
            
            className="play-once",  # Apply the CSS class for the animation
            src="https://tenor.com/view/got-drogon-game-of-thrones-gif-10718218",  # Replace 'your-gif-url.gif' with the URL of your GIF
            style={
               
                  'visibility': 'hidden',  # Initial visibility set to hidden
                  'opacity': '0',  # Initial opacity set to 0
                  'animation': 'playOnce 1s forwards'  # Apply the animation with a duration of 1s
            }
            
         )
         
      ]
      
   )