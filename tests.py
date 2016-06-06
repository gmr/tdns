import socket
import unittest

from tornado import testing
import pycares.errno

import tdns


class ChannelTests(testing.AsyncTestCase):

    def setUp(self):
        super(ChannelTests, self).setUp()
        self.channel = tdns.Channel(io_loop=self.io_loop)

    def tearDown(self):
        del self.channel

    def test_reverse_address(self):
        self.assertEqual('1.0.0.127.in-addr.arpa',
                         tdns.reverse_address('127.0.0.1'))

    @testing.gen_test
    def test_destroy(self):
        self.channel.destroy()
        with self.assertRaises(tdns.AresError):
            yield self.channel.gethostbyaddr('127.0.0.1')

    @testing.gen_test
    def test_gethostbyname(self):
        result = yield self.channel.gethostbyname('localhost', socket.AF_INET)
        self.assertIn('127.0.0.1', result.addresses)

    @testing.gen_test
    def test_gethostbyaddr(self):
        result = yield self.channel.gethostbyaddr('127.0.0.1')
        self.assertEqual('localhost', result.name)

    @testing.gen_test
    def test_getnameinfo(self):
        result = yield self.channel.getnameinfo('127.0.0.1', 80,
                                                tdns.ARES_NI_LOOKUPHOST |
                                                tdns.ARES_NI_LOOKUPSERVICE)
        self.assertEqual('localhost', result.node)
        self.assertEqual('http', result.service)

    @testing.gen_test
    def test_query(self):
        result = yield self.channel.query('gavinroy.com', tdns.QUERY_TYPE_MX)
        self.assertIn('alt1.aspmx.l.google.com', [r.host for r in result])

    @testing.gen_test
    def test_cancel(self):
        future = self.channel.query('gavinroy.com', tdns.QUERY_TYPE_MX)
        self.channel.cancel()
        with self.assertRaises(tdns.AresError):
            yield future

    def test_timeout(self):
        self.assertEqual(self.channel.timeout(3.0), 3.0)

    @testing.gen_test
    def test_local_ip(self):
        with self.assertRaises(tdns.AresError):
            self.channel.set_local_ip('4.4.4.4')
            yield self.channel.query('gavinroy.com', tdns.QUERY_TYPE_MX)

    def test_servers(self):
        self.channel.servers = ['4.4.4.4', '4.4.8.8']
        self.assertEqual(self.channel.servers, ['4.4.4.4', '4.4.8.8'])


class ConstantExportTests(unittest.TestCase):

    def test_that_top_level_constants_are_enumerated(self):
        for name in dir(pycares):
            if name.startswith(('QUERY_TYPE_', 'ARES_FLAG_', 'ARES_NI_')):
                self.assertEqual(getattr(tdns, name),
                                 getattr(pycares, name))

    def test_that_errno_constants_are_enumerated(self):
        for name in dir(pycares.errno):
            if name.startswith('ARES_'):
                self.assertEqual(getattr(tdns, name),
                                 getattr(pycares.errno, name))
