# -*- coding: utf-8 -*-

from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from rohberg.examplemetadata import _
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider


class IMetadataFieldsMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IMetadataFields(model.Schema):
    """ """

    informationtype = schema.List(
        title=_("Type of Information"),
        value_type=schema.Choice(vocabulary="rohberg.examplemetadata.informationtype"),
        required=False,
    )


@implementer(IMetadataFields)
@adapter(IMetadataFieldsMarker)
class MetadataFields(object):
    def __init__(self, context):
        self.context = context

    @property
    def informationtype(self):
        if safe_hasattr(self.context, "informationtype"):
            return self.context.informationtype
        return None

    @informationtype.setter
    def informationtype(self, value):
        self.context.informationtype = value
