#!/usr/bin/env python
# -*- coding: utf-8 -*-

from baanlib import Baan, BaanWrapper
from unittest import TestCase
from mock import Mock


class TestBaanWrapper(TestCase):
    def test_dll_name(self):
        b = Baan('Baan.Application.erpln', dispatcher=Mock())
        self.assertEqual(b.ottstpapihand._dll_name, "ottstpapihand")
        self.assertEqual(b.ottstpapihand.stpapi.put.field._dll_name, "ottstpapihand")
        b.close()

    def test_method_name(self):
        b = Baan('Baan.Application.erpln', dispatcher=Mock())
        self.assertEqual(b.ottstpapihand.stpapi._method_name,
                         "stpapi")
        self.assertEqual(b.ottstpapihand.stpapi.put.field._method_name,
                         "stpapi.put.field")

        b.close()

    def test_get_calling_method(self):
        b = Baan('Baan.Application.erpln', dispatcher=Mock())
        wrapper = b.ottstpapihand.stpapi.put.field
        calling_method = wrapper._get_calling_method(
            *('tcibd0501m000', 'tcibd001.item', 'TEST'))

        self.assertEqual(
            'stpapi.put.field("tcibd0501m000", "tcibd001.item", "TEST")',
            calling_method
        )

        b.close()

    def test_call(self):
        mock = Mock()
        b = Baan('Baan.Application.erpln', dispatcher=mock)

        baanmock = mock.return_value

        b.ottstpapihand.stpapi.put.field("tcibd0501m000", "tcibd001.item", "TEST")

        baanmock.ParseExecFunction.assert_called_with(
            'ottstpapihand',
            'stpapi.put.field("tcibd0501m000", "tcibd001.item", "TEST")',
        )

        b.test.some.foo("test", 10)
        baanmock.ParseExecFunction.assert_called_with(
            'test',
            'some.foo("test", 10)',
        )

        b.close()

    def test_with_statement(self):
        with Baan('Baan.Application.erpln') as b:
            b.test.foo(1)

        self.assertIsNone(b._baan)

    def test_has_properties(self):
        with Baan('Baan.Application.erpln') as b:
            self.assertNotIsInstance(b.Timeout, BaanWrapper)
            self.assertEqual(b.Timeout, 3600)
            self.assertNotIsInstance(b.ReturnValue, BaanWrapper)
            self.assertNotIsInstance(b.FunctionCall, BaanWrapper)
            self.assertNotIsInstance(b.ReturnCall, BaanWrapper)
            self.assertNotIsInstance(b.Binary, BaanWrapper)


    def test_setter(self):
        with Baan('Baan.Application.erpln') as b:
            b.Timeout = 3800
            b.Binary = True

