Favorites Interpolation
=======================

plone.stringinterp.Interpolate will do ${id} style interpolation
using string substitutions provided by named adapters.

Let's test ${favorites_users_emails} interpolation using the homepage::

    >>> self.portal.portal_membership.getAuthenticatedMember().setProperties(email='currentuser@foobar.com')
    >>> apage = self.portal['front-page']
    >>> apage.restrictedTraverse('@@add-favorite')()
    >>> s = """Send notification to ${favorites_user_emails}"""
    >>> from plone.stringinterp import Interpolator
    >>> Interpolator(apage)(s)
    u'Send notification to currentuser@foobar.com'
    
