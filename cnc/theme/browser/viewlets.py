from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import PersonalBarViewlet

class PersonalBarViewlet(PersonalBarViewlet):
    index = ViewPageTemplateFile('personal_bar.pt')

