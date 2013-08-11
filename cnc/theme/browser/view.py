from zope.interface import implements
from zope.component import getMultiAdapter
from Acquisition import aq_inner

from plone.memoize.instance import memoize
from plone.app.layout.navigation.root import getNavigationRootObject

from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView

from cnc.theme.browser.interfaces import IHomepage


class Homepage(BrowserView):
    
    implements(IHomepage)
    
    @memoize
    def news_bulletin(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request),
            name=u'plone_portal_state')
        path = portal_state.navigation_root_path() + '/news/bulletin'
        brain = catalog(portal_type='Event',
                        review_state='published',
                        path=path,
                        sort_on='start',
                        sort_order='reverse',
                        sort_limit=3)[:3]
        res = []
        for b in brain:
            sdate = str(b.start)[:10].replace('/','-')
            res.append((b.Title, sdate, b.getURL()))
        return res

    @memoize
    def news_communion(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request),
            name=u'plone_portal_state')
        path = portal_state.navigation_root_path() + '/news/communion'
        return catalog(portal_type='Event',
                       review_state='published',
                       path=path,
                       sort_on='start',
                       sort_order='reverse',
                       sort_limit=3)[:3]
        res = []
        for b in brain:
            sdate = str(b.start)[:10].replace('/','-')
            res.append((b.Title, sdate, b.getURL()))
        return res

    @memoize
    def news_meeting(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request),
            name=u'plone_portal_state')
        path = portal_state.navigation_root_path() + '/news/meeting'
        return catalog(portal_type='Event',
                       review_state='published',
                       path=path,
                       sort_on='start',
                       sort_order='reverse',
                       sort_limit=3)[:3]
        res = []
        for b in brain:
            sdate = str(b.start)[:10].replace('/','-')
            res.append((b.Title, sdate, b.getURL()))
        return res

    @memoize
    def news_board(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request),
            name=u'plone_portal_state')
        path = portal_state.navigation_root_path() + '/news/board'
        return catalog(portal_type='Event',
                       review_state='published',
                       path=path,
                       sort_on='start',
                       sort_order='reverse',
                       sort_limit=3)[:3]
        res = []
        for b in brain:
            sdate = str(b.start)[:10].replace('/','-')
            res.append((b.Title, sdate, b.getURL()))
        return res

    @memoize
    def news_christian(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request),
            name=u'plone_portal_state')
        path = portal_state.navigation_root_path() + '/news/christian'
        return catalog(portal_type='Event',
                       review_state='published',
                       path=path,
                       sort_on='start',
                       sort_order='reverse',
                       sort_limit=3)[:3]
        res = []
        for b in brain:
            sdate = str(b.start)[:10].replace('/','-')
            res.append((b.Title, sdate, b.getURL()))
        return res

