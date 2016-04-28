from tornado import gen, ioloop
import tdns

loop = ioloop.IOLoop()
channel = tdns.Channel(io_loop=loop)

@gen.coroutine
def on_start():
    response = yield channel.query('aweber.com', tdns.QUERY_TYPE_MX)
    print(response)
    loop.stop()


loop.add_callback(on_start)
loop.start()
