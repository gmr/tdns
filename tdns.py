"""
tdns
====
An asynchronous Tornado pycares DNS client wrapper, exporting the full API.

"""
from tornado import concurrent
from tornado import ioloop

import pycares.errno

__version__ = '0.2.0'

__all__ = ['Channel',
           'AresError'
           'reverse_address',
           'QUERY_TYPE_A',
           'QUERY_TYPE_AAAA',
           'QUERY_TYPE_CNAME',
           'QUERY_TYPE_MX',
           'QUERY_TYPE_NAPTR',
           'QUERY_TYPE_NS',
           'QUERY_TYPE_PTR',
           'QUERY_TYPE_SOA',
           'QUERY_TYPE_SRV',
           'QUERY_TYPE_TXT',
           'ARES_FLAG_USEVC',
           'ARES_FLAG_PRIMARY',
           'ARES_FLAG_IGNTC',
           'ARES_FLAG_NORECURSE',
           'ARES_FLAG_STAYOPEN',
           'ARES_FLAG_NOSEARCH',
           'ARES_FLAG_NOALIASES',
           'ARES_FLAG_NOCHECKRESP',
           'ARES_NI_NOFQDN',
           'ARES_NI_NUMERICHOST',
           'ARES_NI_NAMEREQD',
           'ARES_NI_NUMERICSERV',
           'ARES_NI_DGRAM',
           'ARES_NI_TCP',
           'ARES_NI_UDP',
           'ARES_NI_SCTP',
           'ARES_NI_DCCP',
           'ARES_NI_NUMERICSCOPE',
           'ARES_NI_LOOKUPHOST',
           'ARES_NI_LOOKUPSERVICE',
           'ARES_NI_IDN',
           'ARES_NI_IDN_ALLOW_UNASSIGNED',
           'ARES_NI_IDN_USE_STD3_ASCII_RULES'
           'ARES_SUCCESS',
           'ARES_ENODATA',
           'ARES_EFORMERR',
           'ARES_ESERVFAIL',
           'ARES_ENOTFOUND',
           'ARES_ENOTIMP',
           'ARES_EREFUSED',
           'ARES_EBADQUERY',
           'ARES_EBADNAME',
           'ARES_EBADFAMILY',
           'ARES_EBADRESP',
           'ARES_ECONNREFUSED',
           'ARES_ETIMEOUT',
           'ARES_EOF',
           'ARES_EFILE',
           'ARES_ENOMEM',
           'ARES_EDESTRUCTION',
           'ARES_EBADSTR',
           'ARES_EBADFLAGS',
           'ARES_ENONAME',
           'ARES_EBADHINTS',
           'ARES_ENOTINITIALIZED',
           'ARES_ELOADIPHLPAPI',
           'ARES_EADDRGETNETWORKPARAMS',
           'ARES_ECANCELLED']

AresError = pycares.AresError

# Export pycares constants

QUERY_TYPE_A = pycares.QUERY_TYPE_A
QUERY_TYPE_AAAA = pycares.QUERY_TYPE_AAAA
QUERY_TYPE_CNAME = pycares.QUERY_TYPE_CNAME
QUERY_TYPE_MX = pycares.QUERY_TYPE_MX
QUERY_TYPE_NAPTR = pycares.QUERY_TYPE_NAPTR
QUERY_TYPE_NS = pycares.QUERY_TYPE_NS
QUERY_TYPE_PTR = pycares.QUERY_TYPE_PTR
QUERY_TYPE_SOA = pycares.QUERY_TYPE_SOA
QUERY_TYPE_SRV = pycares.QUERY_TYPE_SRV
QUERY_TYPE_TXT = pycares.QUERY_TYPE_TXT

ARES_FLAG_USEVC = pycares.ARES_FLAG_USEVC
ARES_FLAG_PRIMARY = pycares.ARES_FLAG_PRIMARY
ARES_FLAG_IGNTC = pycares.ARES_FLAG_IGNTC
ARES_FLAG_NORECURSE = pycares.ARES_FLAG_NORECURSE
ARES_FLAG_STAYOPEN = pycares.ARES_FLAG_STAYOPEN
ARES_FLAG_NOSEARCH = pycares.ARES_FLAG_NOSEARCH
ARES_FLAG_NOALIASES = pycares.ARES_FLAG_NOALIASES
ARES_FLAG_NOCHECKRESP = pycares.ARES_FLAG_NOCHECKRESP

ARES_NI_NOFQDN = pycares.ARES_NI_NOFQDN
ARES_NI_NUMERICHOST = pycares.ARES_NI_NUMERICHOST
ARES_NI_NAMEREQD = pycares.ARES_NI_NAMEREQD
ARES_NI_NUMERICSERV = pycares.ARES_NI_NUMERICSERV
ARES_NI_DGRAM = pycares.ARES_NI_DGRAM
ARES_NI_TCP = pycares.ARES_NI_TCP
ARES_NI_UDP = pycares.ARES_NI_UDP
ARES_NI_SCTP = pycares.ARES_NI_SCTP
ARES_NI_DCCP = pycares.ARES_NI_DCCP
ARES_NI_NUMERICSCOPE = pycares.ARES_NI_NUMERICSCOPE
ARES_NI_LOOKUPHOST = pycares.ARES_NI_LOOKUPHOST
ARES_NI_LOOKUPSERVICE = pycares.ARES_NI_LOOKUPSERVICE
ARES_NI_IDN = pycares.ARES_NI_IDN
ARES_NI_IDN_ALLOW_UNASSIGNED = pycares.ARES_NI_IDN_ALLOW_UNASSIGNED
ARES_NI_IDN_USE_STD3_ASCII_RULES = pycares.ARES_NI_IDN_USE_STD3_ASCII_RULES

# export pycares.errno constants too

ARES_SUCCESS = pycares.errno.ARES_SUCCESS
ARES_ENODATA = pycares.errno.ARES_ENODATA
ARES_EFORMERR = pycares.errno.ARES_EFORMERR
ARES_ESERVFAIL = pycares.errno.ARES_ESERVFAIL
ARES_ENOTFOUND = pycares.errno.ARES_ENOTFOUND
ARES_ENOTIMP = pycares.errno.ARES_ENOTIMP
ARES_EREFUSED = pycares.errno.ARES_EREFUSED
ARES_EBADQUERY = pycares.errno.ARES_EBADQUERY
ARES_EBADNAME = pycares.errno.ARES_EBADNAME
ARES_EBADFAMILY = pycares.errno.ARES_EBADFAMILY
ARES_EBADRESP = pycares.errno.ARES_EBADRESP
ARES_ECONNREFUSED = pycares.errno.ARES_ECONNREFUSED
ARES_ETIMEOUT = pycares.errno.ARES_ETIMEOUT
ARES_EOF = pycares.errno.ARES_EOF
ARES_EFILE = pycares.errno.ARES_EFILE
ARES_ENOMEM = pycares.errno.ARES_ENOMEM
ARES_EDESTRUCTION = pycares.errno.ARES_EDESTRUCTION
ARES_EBADSTR = pycares.errno.ARES_EBADSTR
ARES_EBADFLAGS = pycares.errno.ARES_EBADFLAGS
ARES_ENONAME = pycares.errno.ARES_ENONAME
ARES_EBADHINTS = pycares.errno.ARES_EBADHINTS
ARES_ENOTINITIALIZED = pycares.errno.ARES_ENOTINITIALIZED
ARES_ELOADIPHLPAPI = pycares.errno.ARES_ELOADIPHLPAPI
ARES_EADDRGETNETWORKPARAMS = pycares.errno.ARES_EADDRGETNETWORKPARAMS
ARES_ECANCELLED = pycares.errno.ARES_ECANCELLED


def reverse_address(ip_address):
    """Returns the reversed representation of an IP address, usually used when
    doing PTR queries.

    :param str ip_address: IP address to be reversed
    :rtype: str

    """
    return pycares.reverse_address(ip_address)


class Channel(object):
    """An asynchronous wrapper class for c-ares channels."""

    def __init__(self, io_loop=None, **kwargs):
        """Create a new :class:`~tdns.Channel` instance.

        :param int flags: Flags controlling the behavior of the resolver. See
            constants for available values
        :param float timeout: The number of seconds each name server is given
            to respond to a query on the first try. The default is five seconds
        :param int tries: The number of tries the resolver will try contacting
            each name server before giving up. The default is four tries
        :param int ndots: The number of dots which must be present in a domain
            name for it to be queried for "as is" prior to querying for it with
            the default domain extensions appended. The default value is 1
            unless set otherwise by ``resolv.conf`` or the ``RES_OPTIONS``
            environment variable
        :param int tcp_port: The (TCP) port to use for queries.
            The default is ``53``
        :param int udp_port: The (UDP) port to use for queries.
            The default is ``53``
        :param list servers: List of nameservers to be used to do the
            lookups
        :param list domains: The domains to search, instead of the
            domains specified in ``resolv.conf`` or the domain derived from the
            kernel hostname variable
        :param str lookup: The lookups to perform for host queries.
            lookups should be set to a string of the characters ``b`` or ``f``,
            where ``b`` indicates a DNS lookup and ``f`` indicates a lookup in
            the hosts file
        :param bool rotate:  If set to ``True``, the nameservers are rotated
            when doing queries
        :param tornado.ioloop.IOLoop io_loop: The IOLoop to use.
            The default is `tornado.ioloop.IOLoop.current`

        """
        self.io_loop = io_loop or ioloop.IOLoop.current()
        self._fds = {}
        kwargs['sock_state_cb'] = self._sock_state_cb
        self._channel = pycares.Channel(**kwargs)

    def __del__(self):  # pragma: no cover
        """Destroy the channel when deleting the object instance."""
        try:
            self._channel.destroy()
        except pycares.AresError as e:
            # raised when the channel has never been used
            pass

    def gethostbyname(self, name, family):
        """Retrieves host information corresponding to a host name from a host
        database.

        :param str name: Name to query
        :param int family: Socket family
        :raises: :exc:`~tdns.AresError`

        """
        future = concurrent.Future()
        self._channel.gethostbyname(
            name, family,
            lambda result, errno: self._process_result(result, errno, future))
        return future

    def gethostbyaddr(self, addr):
        """Retrieves the host information corresponding to a network address.

        :param str addr: Network address to query
        :rtype: str
        :raises: :exc:`~tdns.AresError`

        """
        future = concurrent.Future()
        self._channel.gethostbyaddr(
            addr,
            lambda result, errno: self._process_result(result, errno, future))
        return future

    def getnameinfo(self, name, port, flags):
        """Provides protocol-independent name resolution from an address to a
        host name and from a port number to the service name.

        :param str name: Name to query
        :param int port: Port of the service to query
        :param int flags: Query flags, see the NI flags section
        :raises: :exc:`~tdns.AresError`

        """
        future = concurrent.Future()
        self._channel.getnameinfo(
            (name, port), flags,
            lambda result, errno: self._process_result(result, errno, future))
        return future

    def query(self, name, query_type):
        """Do a DNS query of the specified type. Available types:

         - :data:`tdns.QUERY_TYPE_A`
         - :data:`tdns.QUERY_TYPE_AAAA`
         - :data:`tdns.QUERY_TYPE_CNAME`
         - :data:`tdns.QUERY_TYPE_MX`
         - :data:`tdns.QUERY_TYPE_NAPTR`
         - :data:`tdns.QUERY_TYPE_NS`
         - :data:`tdns.QUERY_TYPE_PTR`
         - :data:`tdns.QUERY_TYPE_SOA`
         - :data:`tdns.QUERY_TYPE_SRV`
         - :data:`tdns.QUERY_TYPE_TXT`

        :param str name: Name to query
        :param int query_type: Type of query to perform.

        Return Types:

            - A and AAAA: ``ares_query_simple_result``, fields:

              - host
              - ttl

            - CNAME: ``ares_query_cname_result``, fields:

              - cname
              - ttl

            - MX: ``ares_query_mx_result``, fields:

              - host
              - priority
              - ttl

            - NAPTR: ``ares_query_naptr_result``, fields:

              - order
              - preference
              - flags
              - service
              - regex
              - replacement
              - ttl

            -  NS: ``ares_query_ns_result``, fields:

              - host
              - ttl

            - PTR: ``ares_query_ptr_result``, fields:

              - name
              - ttl

            - SOA: ``ares_query_soa_result``, fields:

              - nsmane
              - hostmaster
              - serial
              - refresh
              - retry
              - expires
              - minttl
              - ttl

            - SRV: ``ares_query_srv_result``, fields:

              - host
              - port
              - priority
              - weight
              - ttl

            - TXT: ``ares_query_txt_result``, fields:

              - text
              - ttl

        :raises: :exc:`~tdns.AresError`

        """
        future = concurrent.Future()
        self._channel.query(
            name, query_type,
            lambda result, errno: self._process_result(result, errno, future))
        return future

    def cancel(self):
        """Cancel any pending query on this channel. All pending requests will
        raise a :exc:`~tdns.AresError` with the ``ARES_ECANCELLED`` errorno.

        :raises: :exc:`~tdns.AresError`

        """
        self._channel.cancel()

    def destroy(self):
        """Destroy the channel. All pending requests will raise a
        :exc:`~tdns.AresError` with the ``ARES_EDESTRUCTION`` errorno.

        :raises: :exc:`~tdns.AresError`

        """
        self._channel.destroy()

    def timeout(self, max_timeout):
        """Set the maximum time for which the caller should wait before
        invoking process_fd to process timeouts. If the ``max_timeout``
        parameter is specified, it is stored on the channel and the appropriate
        value is then returned.

        :param float max_timeout: Maximum timeout
        :rtype: float
        :raises: :exc:`~tdns.AresError`
        :raises: ValueError

        """
        return self._channel.timeout(max_timeout)

    def set_local_dev(self, local_dev):
        """Set the local ethernet device from which the queries will be sent.

        :param str local_dev: Network device name
        :raises: :exc:`~tdns.AresError`
        :raises: ValueError

        """
        return self._channel.set_local_dev(local_dev)

    def set_local_ip(self, local_ip):
        """Set the local IPv4 or IPv6 address from which the queries will be
        sent.

        :param str local_ip: IP address
        :raises: :exc:`~tdns.AresError`
        :raises: ValueError

        """
        return self._channel.set_local_ip(local_ip)

    @property
    def servers(self):
        """List of nameservers to use for DNS queries

        :rtype: list

        """
        return self._channel.servers

    @servers.setter
    def servers(self, servers):
        """Set the list of nameservers to use for DNS queries

        :param list servers: The servers to use

        """
        self._channel.servers = servers

    def _sock_state_cb(self, fd, readable, writable):
        state = ((ioloop.IOLoop.READ if readable else 0) |
                 (ioloop.IOLoop.WRITE if writable else 0))
        if not state:
            self.io_loop.remove_handler(fd)
            del self._fds[fd]
        elif fd in self._fds:
            self.io_loop.update_handler(fd, state)
            self._fds[fd] = state
        else:
            self.io_loop.add_handler(fd, self._handle_events, state)
            self._fds[fd] = state

    def _handle_events(self, fd, events):
        read_fd = pycares.ARES_SOCKET_BAD
        write_fd = pycares.ARES_SOCKET_BAD
        if events & ioloop.IOLoop.READ:
            read_fd = fd
        if events & ioloop.IOLoop.WRITE:
            write_fd = fd
        self._channel.process_fd(read_fd, write_fd)

    @staticmethod
    def _process_result(result, errno, future):
        """Common method for processing pycares responses.

        :param mixed result: The result from the pycares call
        :param int errno: The error number if any
        :param tornado.concurrent.Future future: The future to assign the
            result to

        """
        if errno is not None:
            future.set_exception(AresError(errno,
                                           pycares.errno.strerror(errno)))
        else:
            future.set_result(result)
