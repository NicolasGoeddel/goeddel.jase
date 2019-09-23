# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import goeddel.jase


class GoeddelJaseLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=goeddel.jase)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'goeddel.jase:default')


GOEDDEL_JASE_FIXTURE = GoeddelJaseLayer()


GOEDDEL_JASE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GOEDDEL_JASE_FIXTURE,),
    name='GoeddelJaseLayer:IntegrationTesting',
)


GOEDDEL_JASE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GOEDDEL_JASE_FIXTURE,),
    name='GoeddelJaseLayer:FunctionalTesting',
)


GOEDDEL_JASE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        GOEDDEL_JASE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='GoeddelJaseLayer:AcceptanceTesting',
)
