# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import rohberg.examplemetadata


class RohbergExamplemetadataLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=rohberg.examplemetadata)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "rohberg.examplemetadata:default")


ROHBERG_EXAMPLEMETADATA_FIXTURE = RohbergExamplemetadataLayer()


ROHBERG_EXAMPLEMETADATA_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ROHBERG_EXAMPLEMETADATA_FIXTURE,),
    name="RohbergExamplemetadataLayer:IntegrationTesting",
)


ROHBERG_EXAMPLEMETADATA_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ROHBERG_EXAMPLEMETADATA_FIXTURE,),
    name="RohbergExamplemetadataLayer:FunctionalTesting",
)


ROHBERG_EXAMPLEMETADATA_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ROHBERG_EXAMPLEMETADATA_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="RohbergExamplemetadataLayer:AcceptanceTesting",
)
