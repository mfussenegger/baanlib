baanlib
=======

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
