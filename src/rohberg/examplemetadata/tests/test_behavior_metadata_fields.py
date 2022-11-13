# -*- coding: utf-8 -*-
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from rohberg.examplemetadata.behaviors.metadata_fields import IMetadataFieldsMarker
from rohberg.examplemetadata.testing import (
    ROHBERG_EXAMPLEMETADATA_INTEGRATION_TESTING,
)  # noqa
from zope.component import getUtility

import unittest


class MetadataFieldsIntegrationTest(unittest.TestCase):

    layer = ROHBERG_EXAMPLEMETADATA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_behavior_metadata_fields(self):
        behavior = getUtility(IBehavior, "rohberg.examplemetadata.metadata_fields")
        self.assertEqual(
            behavior.marker,
            IMetadataFieldsMarker,
        )
