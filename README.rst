tdns
====
An asynchronous Tornado `pycares <http://pycares.readthedocs.io>`_ DNS
client wrapper, exporting the full API.

|Version| |Downloads| |PythonVersions| |Status| |Coverage| |CodeClimate|

Documentation is available at `tdns.readthedocs.io <http://tdns.readthedocs.io>`_.

Example
-------

.. code:: python

    from tornado import gen, ioloop
    import tdns

    loop = ioloop.IOLoop()
    channel = tdns.Channel(io_loop=loop)

    @gen.coroutine
    def on_start():
        response = yield channel.query('google.com', tdns.QUERY_TYPE_MX)
        print(response)
        loop.stop()


    loop.add_callback(on_start)
    loop.start()

.. |Version| image:: https://img.shields.io/pypi/v/tdns.svg?
   :target: https://pypi.python.org/pypi/tdns

.. |PythonVersions| image:: https://img.shields.io/pypi/pyversions/tdns.svg?
   :target: https://github.com/gmr/tdns

.. |Status| image:: https://img.shields.io/travis/gmr/tdns.svg?
   :target: https://travis-ci.org/gmr/tdns

.. |Coverage| image:: https://img.shields.io/codecov/c/github/gmr/tdns.svg?
   :target: https://codecov.io/github/gmr/tdns?branch=master

.. |Downloads| image:: https://img.shields.io/pypi/dm/tdns.svg?
   :target: https://pypi.python.org/pypi/tdns

.. |CodeClimate| image:: https://codeclimate.com/github/gmr/tdns/badges/gpa.svg
   :target: https://codeclimate.com/github/gmr/tdns
   :alt: Code Climate
