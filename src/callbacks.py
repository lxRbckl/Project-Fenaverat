from src.view import View
from src.config import app
from dash.dependencies import (Input, Output, State, ALL)


class Callbacks:


    def __init__(self, services):
        """Initialize callbacks with a services dependency."""

        self._services = services
    

    def registerCallbacks(self):
        """Register all Dash callbacks for the app."""

        self._videoNintervalsCallback()
        self._dataNintervalsCallback()


    def _videoNintervalsCallback(self):
        """Register the interval callback that randomizes video autoplay."""

        @app.callback(

            inputs = Input("videoIntervalId", "n_intervals"),
            state = State({"type": "video", "index": ALL}, "autoPlay"),
            output = Output({"type": "video", "index": ALL}, "autoPlay")

        )
        def func(*args): return self._services.randomizeAutoplayStates(*args[1:])


    def _dataNintervalsCallback(self):
        """Register the interval callback that refreshes remote data sections."""
        
        @app.callback(
            
            inputs = Input("dataIntervalId", "n_intervals"),
            output = [

                Output("my-projects", "children"),
                Output("my-stack", "children")

            ]
            
        )
        def func(*args): 
            
            data = self._services.fetchRemoteData()

            return [

                View.buildItemProjects(data = {
                    
                    "repositories": data["repositories"],
                    "repositoryBackgrounds": data["repositoryBackgrounds"]
                    
                }),
                View.buildItemStack(data = {
                    
                    "backgrounds" : data["repositoryBackgrounds"],
                    "languages": data["languages"], 
                    "packages": data["packages"], 
                    "tools": data["tools"]
                    
                })

            ]