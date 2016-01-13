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
    def events(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request),
            name=u'plone_portal_state')
        path = portal_state.navigation_root_path() + '/bulletin/events'
        brain = catalog(portal_type=['Event','News Item'],
                        review_state='published',
                        path=path,
                        sort_on='created',
                        sort_order='reverse',
                        sort_limit=3)[:3]
        res = []
        for b in brain:
            sdate = str(b.created)[:10].replace('/','-')
            res.append((b.Title, sdate, b.getURL()))
        return res

    @memoize
    def communion(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request),
            name=u'plone_portal_state')
        path = portal_state.navigation_root_path() + '/bulletin/communion'
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
    def meeting(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request),
            name=u'plone_portal_state')
        path = portal_state.navigation_root_path() + '/bulletin/meeting'
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
    def board(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request),
            name=u'plone_portal_state')
        path = portal_state.navigation_root_path() + '/bulletin/board'
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
    def christian(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request),
            name=u'plone_portal_state')
        path = portal_state.navigation_root_path() + '/bulletin/christian'
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

