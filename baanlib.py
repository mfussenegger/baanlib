#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging

logger = logging.getLogger('baanlib')

# this is a hack to be able to run the test cases on non-windows systems.
# otherwise, using this library on a non-windows system makes hardly any sense.
if sys.platform != 'win32':
    from mock import Mock
    Dispatch = Mock()
    assert Dispatch  # silence pyflakes
else:
    from win32com.client.dynamic import Dispatch


class Baan(object):
    def __init__(self, name, dispatcher=Dispatch):
        self._baan = dispatcher(name)
        self._baan.Timeout = 3600

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def __getattr__(self, name):
        return BaanWrapper(self._baan, name)

    def close(self):
        if self._baan:
            self._baan.Quit()
            self._baan = None

    @property
    def Timeout(self):
        return self._baan.Timeout

    @Timeout.setter
    def Timeout(self, value):
        self._baan.Timeout = value

    @property
    def ReturnValue(self):
        return self._baan.ReturnValue

    @property
    def FunctionCall(self):
        return self._baan.FunctionCall

    @property
    def ReturnCall(self):
        return self._baan.ReturnCall

    @property
    def Binary(self):
        return self._baan.Binary

    @Binary.setter
    def Binary(self, value):
        self._baan.Binary = value


class BaanWrapper(object):
    def __init__(self, baanobj, name):
        self._baanobj = baanobj
        self.name = name

    @property
    def _dll_name(self):
        return self.name.split('.')[0]

    @property
    def _method_name(self):
        return '.'.join(self.name.split('.')[1:])

    def _get_calling_method(self, *args):
        method = self._method_name + '('
        for i, arg in enumerate(args):
            if isinstance(arg, int):
                method += str(arg)
            else:
                method += '"{0}"'.format(arg)

            if not i + 1 == len(args):
                method += ", "
        method += ")"

        return method

    def __getattr__(self, name):
        return BaanWrapper(self._baanobj, self.name + "." + name)

    def __call__(self, *args):
        method = self._get_calling_method(*args)
        self._baanobj.ParseExecFunction(self._dll_name, method)
        return self._baanobj.ReturnValue
