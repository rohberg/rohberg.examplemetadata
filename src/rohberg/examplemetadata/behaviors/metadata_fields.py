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

    project = schema.TextLine(
        title=_("Project"),
        description=_("Give in a project name"),
        required=False,
    )


@implementer(IMetadataFields)
@adapter(IMetadataFieldsMarker)
class MetadataFields(object):
    def __init__(self, context):
        self.context = context

    @property
    def project(self):
        if safe_hasattr(self.context, "project"):
            return self.context.project
        return None

    @project.setter
    def project(self, value):
        self.context.project = value
