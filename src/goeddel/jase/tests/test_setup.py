# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from goeddel.jase.testing import GOEDDEL_JASE_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that goeddel.jase is properly installed."""

    layer = GOEDDEL_JASE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if goeddel.jase is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'goeddel.jase'))

    def test_browserlayer(self):
        """Test that IGoeddelJaseLayer is registered."""
        from goeddel.jase.interfaces import (
            IGoeddelJaseLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IGoeddelJaseLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = GOEDDEL_JASE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['goeddel.jase'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if goeddel.jase is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'goeddel.jase'))

    def test_browserlayer_removed(self):
        """Test that IGoeddelJaseLayer is removed."""
        from goeddel.jase.interfaces import \
            IGoeddelJaseLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IGoeddelJaseLayer,
            utils.registered_layers())
