from requests import get
from random import (choice, shuffle, sample)


class Services:


    def __init__(self):
        """Initialize service configuration for remote data fetches."""

        self.requestHeaders = {

            "Accept" : "application/json",
            "User-Agent" : "Project-Fenaverat"

        }
        self.dataUrls = [

            "https://raw.githubusercontent.com/lxrbckl-labs/Project-SelfStack/refs/heads/V3/data/manual.json",
            "https://raw.githubusercontent.com/lxrbckl-labs/Project-SelfStack/refs/heads/V3/data/automated.json"
            
        ]


    # Randomize autoplay flags for each item.
    def randomizeAutoplayStates(self, sAutoplay): return [choice([True, False]) for a in sAutoplay]


    def fetchRemoteData(self):
        """Fetch and merge JSON data from configured remote URLs."""

        data = {}
        for f in map(lambda url: get(url = url, headers = self.requestHeaders).json(), self.dataUrls):
            
            for k, v in f.items():

                if (k in data.keys()): data[k].extend(v)
                else: data[k] = v

        shuffledRepositories = sample(list(data["repositories"].keys()), k = len(data["repositories"]))
        data["repositories"] = {k: data["repositories"][k] for k in shuffledRepositories}

        return data