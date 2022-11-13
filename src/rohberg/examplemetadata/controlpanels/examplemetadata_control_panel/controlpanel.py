# -*- coding: utf-8 -*-
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from rohberg.examplemetadata import _
from rohberg.examplemetadata.interfaces import IRohbergExamplemetadataLayer
from zope import schema
from zope.component import adapter
from zope.interface import Interface


class IExamplemetadataControlPanel(Interface):
    myfield_name = schema.TextLine(
        title=_(
            "This is an example field for this control panel",
        ),
        description=_(
            "",
        ),
        default="",
        required=False,
        readonly=False,
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
