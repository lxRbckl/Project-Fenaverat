# import <
from dash import html, dcc
import dash_bootstrap_components as dbc

from backend.resource import gFilter

# >


def searchFunction(pData: dict):
    '''  '''

    return dbc.Row(

        style = dict(

            margin = pData['templateStyle']['gMargin'],
            padding = pData['templateStyle']['gPadding'],
            border = pData['templateStyle']['gBorderBlack'],
            borderRadius = pData['templateStyle']['gBorderRadius'],
            backgroundColor = pData['templateStyle']['gColorBlackTransparent']

        ),
        children = [

            dbc.Col(

                width = v['width'],
                style = dict(pData['searchStyle']['colStyle']),
                children = dcc.Dropdown(

                    id = f'{k}Id',
                    maxHeight = 150,
                    optionHeight = 40,
                    style = v['style'],
                    placeholder = v['placeholder'],
                    options = [dict(

                        value = i,
                        label = html.Small(

                            children = i.replace('-', ' '),
                            style = dict(

                                fontSize = 14,
                                color = pData['templateStyle']['gColorBlack']

                            )

                        )

                    ) for i in v['options']]

                )

            )

        for k, v in {

            'nameDropdown' : {

                'width' : None,
                'placeholder' : 'by project name',
                'options' : [k for k in pData['myProjectData'].keys() if (k not in gFilter)],
                'style' : dict(

                    borderTopRightRadius = 0,
                    borderBottomRightRadius = 0,
                    **pData['searchStyle']['dropdownStyle'],
                    fontFamily = pData['templateStyle']['gFontFamily'],
                    backgroundColor = pData['templateStyle']['gColorWhite'],
                    pBackdropFilter = pData['templateStyle']['gBackdropFilter'],
                    borderTopLeftRadius = pData['templateStyle']['gBorderRadius'],
                    borderBottomLeftRadius = pData['templateStyle']['gBorderRadius']

                )

            },
            'languageDropdown' : {

                'width' : {'size' : 3},
                'placeholder' : 'by language, shell',
                'options' : pData['myProjectData']['language'],
                'style' : dict(

                    borderRadius = 0,
                    **pData['searchStyle']['dropdownStyle'],
                    fontFamily = pData['templateStyle']['gFontFamily'],
                    backgroundColor = pData['templateStyle']['gColorWhite'],
                    pBackdropFilter = pData['templateStyle']['gBackdropFilter']

                )

            },
            'libraryDropdown' : {

                'width' : {'size' : 3},
                'options' : pData['myProjectData']['library'],
                'placeholder' : 'by module, package, library',
                'style' : dict(

                    borderTopLeftRadius = 0,
                    borderBottomLeftRadius = 0,
                    **pData['searchStyle']['dropdownStyle'],
                    fontFamily = pData['templateStyle']['gFontFamily'],
                    backgroundColor = pData['templateStyle']['gColorWhite'],
                    pBackdropFilter = pData['templateStyle']['gBackdropFilter'],
                    borderTopRightRadius = pData['templateStyle']['gBorderRadius'],
                    borderBottomRightRadius = pData['templateStyle']['gBorderRadius']

                )

            }

        }.items()]

    )
