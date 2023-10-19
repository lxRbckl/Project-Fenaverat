# import <
from dash import html
import dash_bootstrap_components as dbc

# >


def badgeFunction(

        pData: dict,
        pSubject: list,
        pIterable: list,
        pWidth: str = 12,
        pType: str = 'text',
        pBorder: str = None

):
    '''  '''

    return dbc.Row(

        style = {

            'text' : pData['badgeStyle']['badgeRowTextStyle'],
            'link' : pData['badgeStyle']['badgeRowLinkStyle']

        }[pType],
        children = [

            dbc.Col(

                width = pWidth,
                children = {

                    'text' : html.Small(v.replace('-', ' ')),
                    'link' : html.A(

                        href = '#' + v.replace('-', ' '),
                        children = html.Small(['➥  ', v.replace('-', ' ').title()]),
                        style = dict(

                            textDecoration = 'none',
                            fontFamily = 'sans-serif',
                            color = pData['templateStyle']['gColorBlack']

                        )

                    )

                }[pType],
                style = dict(

                    margin = '2px 2px 2px 2px',
                    **pData['badgeStyle']['badgeColStyle'],
                    border = pBorder if (pBorder) else None,
                    fontFamily = pData['templateStyle']['gFontFamily'],
                    borderRadius = (pData['templateStyle']['gBorderRadius'] / 2),
                    backgroundColor = pData['badgeStyle']['badgeColorPalette'][k]

                )

            )

        for k, v in [(k, v) for k in pSubject for v in pIterable[k]]]

    )


def badgeIcon(

        pSrc: list,
        pData: dict,
        pWidth: dict,
        pHref: str = None,
        pHeight: int = 19,
        pStyle: dict = None,
        isBack: bool = False,
        isExternal: bool = False

):
    '''  '''

    return [

        dbc.Col(

            width = pWidth,
            style = pStyle,
            children = html.A(

                href = pHref,
                style = pData['badgeStyle']['footerAStyle'],
                target = '_blank' if (isExternal) else '_self',
                children = html.Img(

                    src = str(s),
                    style = dict(

                        height = pHeight,
                        transform = "rotate(180deg)" if (isBack) else None

                    )

                )

            )

        )

    for s in pSrc if (s is not None)]
