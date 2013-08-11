from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer


class IThemeSpecific(IDefaultPloneLayer):
    """Marker Interface that Defines a Zope 3 Browser Layer.
       If a Viewlet Needs Registered Only for Your Theme,
       this Interface Must Be Its Layer
       (in theme/viewlets/configure.zcml).
    """

class IHomepage(Interface):
    """Browser View for Homepage Logic"""

