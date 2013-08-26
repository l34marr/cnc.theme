from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import PersonalBarViewlet, FooterViewlet

class PersonalBarViewlet(PersonalBarViewlet):
    index = ViewPageTemplateFile('personal_bar.pt')

class FooterViewlet(FooterViewlet):
    index = ViewPageTemplateFile('footer.pt')

