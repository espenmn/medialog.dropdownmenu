# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE
    PloneSandboxLayer,
)
from plone.testing import z2

import medialog.dropdownmenu


class MedialogDropdownmenuLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=medialog.dropdownmenu)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.dropdownmenu:default')


MEDIALOG_DROPDOWNMENU_FIXTURE = MedialogDropdownmenuLayer()


MEDIALOG_DROPDOWNMENU_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_DROPDOWNMENU_FIXTURE,),
    name='MedialogDropdownmenuLayer:IntegrationTesting',
)


MEDIALOG_DROPDOWNMENU_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_DROPDOWNMENU_FIXTURE,),
    name='MedialogDropdownmenuLayer:FunctionalTesting',
)


MEDIALOG_DROPDOWNMENU_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIALOG_DROPDOWNMENU_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MedialogDropdownmenuLayer:AcceptanceTesting',
)
