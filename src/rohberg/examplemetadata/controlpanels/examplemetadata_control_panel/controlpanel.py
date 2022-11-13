# -*- coding: utf-8 -*-
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from rohberg.examplemetadata import _
from rohberg.examplemetadata.interfaces import IRohbergExamplemetadataLayer
from plone import schema
from zope.component import adapter
from zope.interface import Interface

import json


VOCABULARY_SCHEMA = json.dumps(
    {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "token": {"type": "string"},
                        "titles": {
                            "type": "object",
                            "properties": {
                                "lang": {"type": "string"},
                                "title": {"type": "string"},
                            },
                        },
                    },
                },
            }
        },
    }
)


class IExamplemetadataControlPanel(Interface):
    informationtype = schema.JSONField(
        title=_("Informationtype"),
        description=_("Type of information"),
        required=False,
        schema=VOCABULARY_SCHEMA,
        widget="vocabularyterms",
        default={
            "items": [
                {
                    "token": "manual",
                    "titles": {
                        "en": "Manual",
                        "de": "Anleitung",
                    },
                },
                {
                    "token": "qanda",
                    "titles": {
                        "en": "Questions and Answers",
                        "de": "FAQ",
                    },
                },
            ]
        },
        missing_value={"items": []},
    )


class ExamplemetadataControlPanel(RegistryEditForm):
    schema = IExamplemetadataControlPanel
    schema_prefix = "rohberg.examplemetadata.examplemetadata_control_panel"
    label = _("Examplemetadata Control Panel")


ExamplemetadataControlPanelView = layout.wrap_form(
    ExamplemetadataControlPanel, ControlPanelFormWrapper
)


@adapter(Interface, IRohbergExamplemetadataLayer)
class ExamplemetadataControlPanelConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IExamplemetadataControlPanel
    configlet_id = "examplemetadata_control_panel-controlpanel"
    configlet_category_id = "Products"
    title = _("Examplemetadata Control Panel")
    group = ""
    schema_prefix = "rohberg.examplemetadata.examplemetadata_control_panel"
