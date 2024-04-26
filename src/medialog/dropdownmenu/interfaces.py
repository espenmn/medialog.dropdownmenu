# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from zope import schema
from zope.interface import alsoProvides
from plone.supermodel import model
 



class IMedialogDropdownmenuLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
    


class ISettings(model.Schema):
    """Adds settings to medialog.controlpanel
    """

    model.fieldset(
        'dropdown_menu',
        label=(u'Dropdown Menu'),
        fields=[
            'scale', 
            ],
        )

     
    scale =  schema.Choice(
        title="scale", 
        vocabulary='plone.app.vocabularies.ImagesScales',
        default='icon',
    )



alsoProvides(ISettings, IMedialogControlpanelSettingsProvider)