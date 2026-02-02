from dash.html import (Div, Video)
from dash_iconify import DashIconify
import dash_mantine_components as dmc
from dash.dcc import (Markdown, Interval)


class View:


    def __init__(self, items):
        """Initialize the view with a list of grid item configs."""

        self.items = items
        self._dataIntervalMinutes = 60
        self._videoIntervalSeconds = 120


    def _buildItem(
            
        self,
        width = 1, 
        style = {},
        height = 1,
        corpus = None,
        visible = True,
        background = None,
        contentType = "markdown",

    ):
        """Build a single grid item container with optional content."""

        return Div(

            className = f"gridItem {'blur' if (corpus and background) else ''}",
            children = {

                "video" : View.buildItemVideo,
                "markdown" : View.buildItemMarkdown,
                "my-projects" : lambda i : Div(id = "my-projects", className = "myProjectsDiv"),
                "my-stack" : lambda i : Div(id = "my-stack", className = "myStackDiv")

            }[contentType](corpus) if corpus else None,
            style = {

                **style,
                "gridRow" : f"span {height}",
                "gridColumn" : f"span {width}",
                "backgroundImage" : f"url({background})",
                "visibility" : "visible" if visible else "hidden"

            }
            
        )


    @staticmethod
    def buildItemVideo(video):
        """Build a video component for a given video URL."""

        return Video(

            src = video,
            loop = False,
            muted = True,
            className = "videoExtended",
            id = {"type" : "video", "index" : video}

        )


    @staticmethod
    def buildItemMarkdown(markdown):
        """Build a Markdown component from a list of markdown blocks."""

        return Markdown(

            className = "markdownExtended",
            children = "\n".join([
                
                {

                    str: m,
                    list: " ".join(m) + "\n"

                }[type(m)]
                
            for m in markdown])

        )


    @staticmethod
    def buildItemProjects(data):
        """Build a list of project cards from repository data."""

        return [

            View.buildItemProjectCard(
                
                url = v["url"],
                title = v["title"],
                description = v["description"],
                stack = [f"`{s}`" for s in v["stack"]],
                background = data.get("repositoryBackgrounds").get(k),

            ) if v["show"] else None

        for k, v in data["repositories"].items()] if (data and type(data) == dict) else None


    @staticmethod
    def buildItemProjectCard(

        url,
        stack,
        title,
        description,
        iconWidth = 25,
        background = None,
        iconGithub = "ion:logo-github",
        iconChevron = "tabler-chevron-right"

    ):
        """Build a single project card with a link and metadata."""

        return Div(

            style = {"backgroundImage" : f"url({background})"},
            className = f"myProjectsSubDiv {'blur' if background else ''}",
            children = [

                Div(

                    className = "projectCardHeader",
                    children = View.buildItemMarkdown(markdown = [
                        
                        f"## **{title}**", 
                        description
                    
                    ])

                ),
                Div(

                    className = "projectCardBody",
                    children = View.buildItemMarkdown(markdown = [stack])

                ),
                Div(

                    className = "projectCardFooter",
                    children = dmc.NavLink(

                        href = url,
                        active = True,
                        target = "_blank",
                        label = "See More",
                        variant = "filled",
                        className = "navlinkExtended",
                        leftSection = DashIconify(icon = iconGithub, width = iconWidth),
                        rightSection = DashIconify(icon = iconChevron, width = iconWidth)

                    )
                    
                )
            ]

        )


    @staticmethod
    def buildItemStack(data, fields = ["languages", "packages", "tools"]):
        """Build the stack section from categorized data fields."""

        return [

            Div(children = View.buildItemMarkdown(markdown = ["## My *Stack*"])),
            *[Div(

                className = "myStackSubDiv",
                children = View.buildItemMarkdown(markdown = [
                    
                    f"### {f.capitalize()}",
                    " ".join(f"`{i}`" for i in data[f])

                ]),

            ) for f in fields]
            
        ] if (data and type(data) == dict) else None


    @property
    def build(self):
        """Return the complete Dash layout for this view."""

        return dmc.MantineProvider(children = dmc.Center(children = [

            Interval(

                n_intervals = 0,
                id = "videoIntervalId",
                interval = (1000 * self._videoIntervalSeconds)

            ),
            Interval(

                n_intervals = 0,
                id = "dataIntervalId",
                interval = (1000 * (self._dataIntervalMinutes * 60))

            ),
            Div(

                className = "gridContainer",
                children = [self._buildItem(**i) for i in self.items]

            )

        ]))