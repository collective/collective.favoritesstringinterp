#!/usr/bin/env python
# encoding: utf-8
"""
adapters.py

Created by Bogdan Girman on Fri Oct 11 18:42:20 EEST 2013
Copyright (c) 2013 Plone Foundation.
"""

from zope.component import adapts
from zope.site.hooks import getSite
from Products.CMFCore.interfaces import IContentish
from Products.CMFCore.utils import getToolByName

from plone.stringinterp import _
from plone.stringinterp.adapters import BaseSubstitution
from collective.favorites.interfaces import IFavoriteStorage


class FavoritesUserEmailsSubstitution(BaseSubstitution):
    adapts(IContentish)

    category = _(u'Favorites')
    description = _(u'List emails separated by coma for users who favorites current content')

    def safe_call(self):
        users = []
        uid = self.context.UID()
        pm = getToolByName(self.context, 'portal_membership')
        favorites = IFavoriteStorage(getSite()).get_favorites()
        for userId, values in favorites.items():
            for value in values:
                if uid == value['id']:
                    users.append(pm.getMemberById(userId))
        return ', '.join([u.getProperty('email', None) for u in users])
