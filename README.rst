tdns
====
An asynchronous Tornado `pycares <http://pycares.readthedocs.io>`_ DNS
client wrapper, exporting the full API.

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
