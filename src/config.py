from os import getenv
from dash import Dash
from pathlib import Path
from dash_bootstrap_components import themes


port = getenv("PORT", 8056)
host = getenv("HOST", "0.0.0.0")

root = Path(__file__).resolve().parent.parent
dirAssets = root / "src" / "assets"
fileLayout = dirAssets / "layout.json"


app = Dash(

    name = "lxRbckl",
    title = "lxRbckl",
    assets_folder = dirAssets,
    suppress_callback_exceptions = True,
    external_stylesheets = [themes.BOOTSTRAP]

)