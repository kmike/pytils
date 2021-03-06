# -*- coding: utf-8 -*-
# pytils - russian-specific string utils
# Copyright (C) 2006-2009  Yury Yurevich
#
# http://pyobject.ru/projects/pytils/
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, version 2
# of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
"""
Unit tests for pytils
"""
from __future__ import print_function, absolute_import, division, unicode_literals

__all__ = ["test_numeral", "test_dt", "test_translit", "test_utils", "test_typo"]

import unittest
import sys

def get_django_suite():
    try:
        import django
    except ImportError:
        return unittest.TestSuite()

    import pytils.test.templatetags
    return pytils.test.templatetags.get_suite()

def get_suite():
    """Return TestSuite for all unit-test of pytils"""
    suite = unittest.TestSuite()
    for module_name in __all__:
        imported_module = __import__("pytils.test."+module_name,
                                       globals(),
                                       locals(),
                                       ["pytils.test"])

        loader = unittest.defaultTestLoader
        suite.addTest(loader.loadTestsFromModule(imported_module))
        suite.addTest(get_django_suite())

    return suite

def run_tests_from_module(module, verbosity=1):
    """Run unit-tests for single module"""
    suite = unittest.TestSuite()
    loader = unittest.defaultTestLoader
    suite.addTest(loader.loadTestsFromModule(module))
    unittest.TextTestRunner(verbosity=verbosity).run(suite)

def run(verbosity=1):
    """Run all unit-test of pytils"""
    suite = get_suite()
    return unittest.TextTestRunner(verbosity=verbosity).run(suite)

if __name__ == '__main__':
    result = run()
    status = not int(result.wasSuccessful())
    sys.exit(status)

