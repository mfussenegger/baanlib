baanlib
=======

[![Build Status](https://secure.travis-ci.org/mfussenegger/baanlib.png?branch=master)](https://travis-ci.org/mfussenegger/baanlib)

A simple python wrapper around win32com OLE functionality to make OLE automation with Baan/Infor LN easier to use.

Instead of having to write

```python
from win32com.client.dynamic import Dispatch

# Modify 'Baan.Application.erpln' to the Class Name in the BW configuration if necessary
baan = Dispatch('Baan.Application.erpln')
baan.Timeout = 3600

baan.ParseExecFunction(
    "odll_name",
    'some.function.name("with", "a", "few", "arguments")'
)

baan.Quit()
```

It gets especially annoying if you want to use variables from your python scripts, as you'll always have to construct the string:

```python
'some.function.name("{0}")'.format(var)
```

baanlib makes all that a little bit easier:

```python
from baanlib import Baan

with Baan('Baan.Application.erpln') as b:
    b.odll_name.some.function.name("with", "a", "few", "arguments")

    var = 1
    foo = 'test'
    b.odll_name.some.function.name(var, foo)
```
To further reduce the amount of typing required, the api can also be used like this:

```python
with Baan('Baan.Application.erpln') as b:
    f = b.ottstpapihand
    put = f.stpapi.put.field

    put("sessioncode", "fieldname1", "value1")
    put("sessioncode", "fieldname2", "value2")

    f.end.session("sessioncode")
```

## Installation

Baanlib requires the pywin32 extensions which are available on [sourceforge](http://sourceforge.net/projects/pywin32/files/pywin32/Build%20217/).

Once the pywin32 requirement is met, baanlib can be installed using pip.

    pip install --upgrade baanlib
