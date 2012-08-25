baanlib
=======

A simple python wrapper around win32com OLE functionality to make OLE automation with Baan/Infor LN easier to use.

Instead of having to write

    from win32com.client.dynamic import Dispatch

    # Modify 'Baan.Application.erpln' to the Class Name in the BW configuration if necessary
    baan = Dispatch('Baan.Application.erpln')

    baan.ParseExecFunction(
        "odll_name",
        'some.function.name("with", "a", "few", "arguments")'
    )

It gets especially annoying if you want to use variables from your python scripts, as you'll always have to construct the string:

    'some.function.name("{0}")'.format(var)

baanlib makes all that a little bit easier:

    from baanlib import Baan

    b = Baan('Baan.Application.erpln')
    b.odll_name.some.function.name("with", "a", "few", "arguments")

    var = 1
    foo = 'test'
    b.odll_name.some.function.name(var, foo)
