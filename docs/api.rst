tdns API
========
The :py:class:`Channel <tdns.Channel>` implements a Python class for interacting
with the `c-ares <http://c-ares.haxx.se>`_ API using native
`Tornado <https://www.tornadoweb.org>`_ asynchronous conventions. For example,
to query the MX records for google you could use the following snippet:

.. code:: python

    from tornado import gen, ioloop, web
    import tdns


    class RequestHandler(web.RequestHandler):

        @gen.coroutine
        def get(self, *args, **kwargs):
            channel = tdns.Channel(io_loop=ioloop.IOLoop.current())
            response = yield channel.query('google.com', 'MX')

tnds is build on top of the excellent `pycares <http://pycares.readthedocs.io>`_ library.

Ares Channel
------------
.. autoclass:: tdns.Channel
    :members:
    :inherited-members:

Utility Functions
-----------------
.. autofunction:: tdns.reverse_address
