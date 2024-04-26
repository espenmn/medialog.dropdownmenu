# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone.app.layout.viewlets.common import GlobalSectionsViewlet

# class DropDownMenuViewlet(ViewletBase):

#     def update(self):
#         self.message = self.get_message()

#     def get_message(self):
#         return u'My message'

#     def index(self):
#         return super(DropDownMenuViewlet, self).render()



class DropDownMenuViewlet(GlobalSectionsViewlet):
    
    def customize_tab(self, entry, tab):
        """Helper to add custom entry keys/values."""
        #Maybe add option for 'top folder too?
        entry['image_thumb'] = ''
        
    def customize_entry(self, entry, brain):
        """Helper to add custom entry keys/values."""
        entry['image_thumb'] = ''
        if brain.getIcon:
            entry['image_thumb'] = '<img  alt="" class="subnmenu_image" src="{url}/@@images/image/{thumb}" /> '.format( url = entry['url'], thumb = 'listing' )
            
    
    _item_markup_template = (
            '<li class="{id}{has_sub_class} nav-item">'
            '<a href="{url}" class="state-{review_state} nav-link"{aria_haspopup}>{image_thumb}{title}</a>{opener}'   
            "{sub}"  
            "</li>"
        )