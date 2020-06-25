class PyCapsule(object):
    'Capsule objects let you wrap a C "void *" pointer in a Python\nobject.  They\'re a way of passing data through the Python interpreter\nwithout creating your own custom type.\n\nCapsules are used for communication between extension modules.\nThey provide a way for an extension module to export a C interface\nto other extension modules, so that extension modules can use the\nPython import mechanism to link to one another.\n'
    __class__ = PyCapsule
    def __init__(self, *args, **kwargs):
        'Capsule objects let you wrap a C "void *" pointer in a Python\nobject.  They\'re a way of passing data through the Python interpreter\nwithout creating your own custom type.\n\nCapsules are used for communication between extension modules.\nThey provide a way for an extension module to export a C interface\nto other extension modules, so that extension modules can use the\nPython import mechanism to link to one another.\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

OSError = type
AF_APPLETALK = 16
AF_DECnet = 12
AF_INET = 2
AF_INET6 = 23
AF_IPX = 6
AF_IRDA = 26
AF_SNA = 11
AF_UNSPEC = 0
AI_ADDRCONFIG = 1024
AI_ALL = 256
AI_CANONNAME = 2
AI_NUMERICHOST = 4
AI_NUMERICSERV = 8
AI_PASSIVE = 1
AI_V4MAPPED = 2048
CAPI = PyCapsule()
EAI_AGAIN = 11002
EAI_BADFLAGS = 10022
EAI_FAIL = 11003
EAI_FAMILY = 10047
EAI_MEMORY = 8
EAI_NODATA = 11001
EAI_NONAME = 11001
EAI_SERVICE = 10109
EAI_SOCKTYPE = 10044
INADDR_ALLHOSTS_GROUP = -536870911
INADDR_ANY = 0
INADDR_BROADCAST = -1
INADDR_LOOPBACK = 2130706433
INADDR_MAX_LOCAL_GROUP = -536870657
INADDR_NONE = -1
INADDR_UNSPEC_GROUP = -536870912
IPPORT_RESERVED = 1024
IPPORT_USERRESERVED = 5000
IPPROTO_ICMP = 1
IPPROTO_IP = 0
IPPROTO_RAW = 255
IPPROTO_TCP = 6
IPPROTO_UDP = 17
IPV6_CHECKSUM = 26
IPV6_DONTFRAG = 14
IPV6_HOPLIMIT = 21
IPV6_HOPOPTS = 1
IPV6_JOIN_GROUP = 12
IPV6_LEAVE_GROUP = 13
IPV6_MULTICAST_HOPS = 10
IPV6_MULTICAST_IF = 9
IPV6_MULTICAST_LOOP = 11
IPV6_PKTINFO = 19
IPV6_RECVRTHDR = 38
IPV6_RECVTCLASS = 40
IPV6_RTHDR = 32
IPV6_TCLASS = 39
IPV6_UNICAST_HOPS = 4
IPV6_V6ONLY = 27
IP_ADD_MEMBERSHIP = 12
IP_DROP_MEMBERSHIP = 13
IP_HDRINCL = 2
IP_MULTICAST_IF = 9
IP_MULTICAST_LOOP = 11
IP_MULTICAST_TTL = 10
IP_OPTIONS = 1
IP_RECVDSTADDR = 25
IP_TOS = 3
IP_TTL = 4
MSG_BCAST = 1024
MSG_CTRUNC = 512
MSG_DONTROUTE = 4
MSG_ERRQUEUE = 4096
MSG_MCAST = 2048
MSG_OOB = 1
MSG_PEEK = 2
MSG_TRUNC = 256
MSG_WAITALL = 8
NI_DGRAM = 16
NI_MAXHOST = 1025
NI_MAXSERV = 32
NI_NAMEREQD = 4
NI_NOFQDN = 1
NI_NUMERICHOST = 2
NI_NUMERICSERV = 8
RCVALL_MAX = 3
RCVALL_OFF = 0
RCVALL_ON = 1
RCVALL_SOCKETLEVELONLY = 2
SHUT_RD = 0
SHUT_RDWR = 2
SHUT_WR = 1
SIO_KEEPALIVE_VALS = 2550136836
SIO_LOOPBACK_FAST_PATH = 2550136848
SIO_RCVALL = 2550136833
SOCK_DGRAM = 2
SOCK_RAW = 3
SOCK_RDM = 4
SOCK_SEQPACKET = 5
SOCK_STREAM = 1
SOL_IP = 0
SOL_SOCKET = 65535
SOL_TCP = 6
SOL_UDP = 17
SOMAXCONN = 2147483647
SO_ACCEPTCONN = 2
SO_BROADCAST = 32
SO_DEBUG = 1
SO_DONTROUTE = 16
SO_ERROR = 4103
SO_EXCLUSIVEADDRUSE = -5
SO_KEEPALIVE = 8
SO_LINGER = 128
SO_OOBINLINE = 256
SO_RCVBUF = 4098
SO_RCVLOWAT = 4100
SO_RCVTIMEO = 4102
SO_REUSEADDR = 4
SO_SNDBUF = 4097
SO_SNDLOWAT = 4099
SO_SNDTIMEO = 4101
SO_TYPE = 4104
SO_USELOOPBACK = 64
SocketType = socket
TCP_FASTOPEN = 15
TCP_KEEPCNT = 16
TCP_KEEPIDLE = 3
TCP_KEEPINTVL = 17
TCP_MAXSEG = 4
TCP_NODELAY = 1
__doc__ = 'Implementation module for socket operations.\n\nSee the socket module for documentation.'
__file__ = 'c:\\python37\\dlls\\_socket.pyd'
__name__ = '_socket'
__package__ = ''
def close(integer):
    "close(integer) -> None\n\nClose an integer socket file descriptor.  This is like os.close(), but for\nsockets; on some platforms os.close() won't work for socket file descriptors."
    pass

def dup(integer):
    "dup(integer) -> integer\n\nDuplicate an integer socket file descriptor.  This is like os.dup(), but for\nsockets; on some platforms os.dup() won't work for socket file descriptors."
    return 1

error = OSError
class gaierror(OSError):
    __class__ = gaierror
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'socket'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def getaddrinfo(host, port, family=None, type=None, proto=None, flags=None):
    'getaddrinfo(host, port [, family, type, proto, flags])\n    -> list of (family, type, proto, canonname, sockaddr)\n\nResolve host and port into addrinfo struct.'
    pass

def getdefaulttimeout():
    'getdefaulttimeout() -> timeout\n\nReturns the default timeout in seconds (float) for new socket objects.\nA value of None indicates that new socket objects have no timeout.\nWhen the socket module is first imported, the default is None.'
    pass

def gethostbyaddr(host):
    'gethostbyaddr(host) -> (name, aliaslist, addresslist)\n\nReturn the true host name, a list of aliases, and a list of IP addresses,\nfor a host.  The host argument is a string giving a host name or IP number.'
    return tuple()

def gethostbyname(host):
    "gethostbyname(host) -> address\n\nReturn the IP address (a string of the form '255.255.255.255') for a host."
    pass

def gethostbyname_ex(host):
    'gethostbyname_ex(host) -> (name, aliaslist, addresslist)\n\nReturn the true host name, a list of aliases, and a list of IP addresses,\nfor a host.  The host argument is a string giving a host name or IP number.'
    return tuple()

def gethostname():
    'gethostname() -> string\n\nReturn the current host name.'
    return ''

def getnameinfo(sockaddr, flags):
    'getnameinfo(sockaddr, flags) --> (host, port)\n\nGet host and port for a sockaddr.'
    return tuple()

def getprotobyname(name):
    'getprotobyname(name) -> integer\n\nReturn the protocol number for the named protocol.  (Rarely used.)'
    return 1

def getservbyname(servicename, protocolname=None):
    "getservbyname(servicename[, protocolname]) -> integer\n\nReturn a port number from a service name and protocol name.\nThe optional protocol name, if given, should be 'tcp' or 'udp',\notherwise any protocol will match."
    return 1

def getservbyport(port, protocolname=None):
    "getservbyport(port[, protocolname]) -> string\n\nReturn the service name from a port number and protocol name.\nThe optional protocol name, if given, should be 'tcp' or 'udp',\notherwise any protocol will match."
    return ''

has_ipv6 = True
class herror(OSError):
    __class__ = herror
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'socket'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def htonl(integer):
    'htonl(integer) -> integer\n\nConvert a 32-bit integer from host to network byte order.'
    return 1

def htons(integer):
    'htons(integer) -> integer\n\nConvert a 16-bit unsigned integer from host to network byte order.\nNote that in case the received integer does not fit in 16-bit unsigned\ninteger, but does fit in a positive C int, it is silently truncated to\n16-bit unsigned integer.\nHowever, this silent truncation feature is deprecated, and will raise an \nexception in future versions of Python.'
    return 1

def inet_aton(string):
    'inet_aton(string) -> bytes giving packed 32-bit IP representation\n\nConvert an IP address in string format (123.45.67.89) to the 32-bit packed\nbinary format used in low-level network functions.'
    pass

def inet_ntoa(packed_ip):
    'inet_ntoa(packed_ip) -> ip_address_string\n\nConvert an IP address from 32-bit packed binary format to string format'
    pass

def inet_ntop(af, packed_ip):
    'inet_ntop(af, packed_ip) -> string formatted IP address\n\nConvert a packed IP address of the given family to string format.'
    return ''

def inet_pton(af, ip):
    'inet_pton(af, ip) -> packed IP address string\n\nConvert an IP address from string format to a packed string suitable\nfor use with low-level network functions.'
    pass

def ntohl(integer):
    'ntohl(integer) -> integer\n\nConvert a 32-bit integer from network to host byte order.'
    return 1

def ntohs(integer):
    'ntohs(integer) -> integer\n\nConvert a 16-bit unsigned integer from network to host byte order.\nNote that in case the received integer does not fit in 16-bit unsigned\ninteger, but does fit in a positive C int, it is silently truncated to\n16-bit unsigned integer.\nHowever, this silent truncation feature is deprecated, and will raise an \nexception in future versions of Python.'
    return 1

def setdefaulttimeout(timeout):
    'setdefaulttimeout(timeout)\n\nSet the default timeout in seconds (float) for new socket objects.\nA value of None indicates that new socket objects have no timeout.\nWhen the socket module is first imported, the default is None.'
    pass

class socket(object):
    "socket(family=AF_INET, type=SOCK_STREAM, proto=0) -> socket object\nsocket(family=-1, type=-1, proto=-1, fileno=None) -> socket object\n\nOpen a socket of the given type.  The family argument specifies the\naddress family; it defaults to AF_INET.  The type argument specifies\nwhether this is a stream (SOCK_STREAM, this is the default)\nor datagram (SOCK_DGRAM) socket.  The protocol argument defaults to 0,\nspecifying the default protocol.  Keyword arguments are accepted.\nThe socket is created as non-inheritable.\n\nWhen a fileno is passed in, family, type and proto are auto-detected,\nunless they are explicitly set.\n\nA socket object represents one endpoint of a network connection.\n\nMethods of socket objects (keyword arguments not allowed):\n\n_accept() -- accept connection, returning new socket fd and client address\nbind(addr) -- bind the socket to a local address\nclose() -- close the socket\nconnect(addr) -- connect the socket to a remote address\nconnect_ex(addr) -- connect, return an error code instead of an exception\ndup() -- return a new socket fd duplicated from fileno()\nfileno() -- return underlying file descriptor\ngetpeername() -- return remote address [*]\ngetsockname() -- return local address\ngetsockopt(level, optname[, buflen]) -- get socket options\ngettimeout() -- return timeout or None\nlisten([n]) -- start listening for incoming connections\nrecv(buflen[, flags]) -- receive data\nrecv_into(buffer[, nbytes[, flags]]) -- receive data (into a buffer)\nrecvfrom(buflen[, flags]) -- receive data and sender's address\nrecvfrom_into(buffer[, nbytes, [, flags])\n  -- receive data and sender's address (into a buffer)\nsendall(data[, flags]) -- send all data\nsend(data[, flags]) -- send data, may not send all of it\nsendto(data[, flags], addr) -- send data to a given address\nsetblocking(0 | 1) -- set or clear the blocking I/O flag\ngetblocking() -- return True if socket is blocking, False if non-blocking\nsetsockopt(level, optname, value[, optlen]) -- set socket options\nsettimeout(None | float) -- set or clear the timeout\nshutdown(how) -- shut down traffic in one or both directions\nif_nameindex() -- return all network interface indices and names\nif_nametoindex(name) -- return the corresponding interface index\nif_indextoname(index) -- return the corresponding interface name\n\n [*] not available on all platforms!"
    __class__ = socket
    def __del__(self):
        return None
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, family=-1, type=-1, proto=-1, fileno=None):
        "socket(family=AF_INET, type=SOCK_STREAM, proto=0) -> socket object\nsocket(family=-1, type=-1, proto=-1, fileno=None) -> socket object\n\nOpen a socket of the given type.  The family argument specifies the\naddress family; it defaults to AF_INET.  The type argument specifies\nwhether this is a stream (SOCK_STREAM, this is the default)\nor datagram (SOCK_DGRAM) socket.  The protocol argument defaults to 0,\nspecifying the default protocol.  Keyword arguments are accepted.\nThe socket is created as non-inheritable.\n\nWhen a fileno is passed in, family, type and proto are auto-detected,\nunless they are explicitly set.\n\nA socket object represents one endpoint of a network connection.\n\nMethods of socket objects (keyword arguments not allowed):\n\n_accept() -- accept connection, returning new socket fd and client address\nbind(addr) -- bind the socket to a local address\nclose() -- close the socket\nconnect(addr) -- connect the socket to a remote address\nconnect_ex(addr) -- connect, return an error code instead of an exception\ndup() -- return a new socket fd duplicated from fileno()\nfileno() -- return underlying file descriptor\ngetpeername() -- return remote address [*]\ngetsockname() -- return local address\ngetsockopt(level, optname[, buflen]) -- get socket options\ngettimeout() -- return timeout or None\nlisten([n]) -- start listening for incoming connections\nrecv(buflen[, flags]) -- receive data\nrecv_into(buffer[, nbytes[, flags]]) -- receive data (into a buffer)\nrecvfrom(buflen[, flags]) -- receive data and sender's address\nrecvfrom_into(buffer[, nbytes, [, flags])\n  -- receive data and sender's address (into a buffer)\nsendall(data[, flags]) -- send all data\nsend(data[, flags]) -- send data, may not send all of it\nsendto(data[, flags], addr) -- send data to a given address\nsetblocking(0 | 1) -- set or clear the blocking I/O flag\ngetblocking() -- return True if socket is blocking, False if non-blocking\nsetsockopt(level, optname, value[, optlen]) -- set socket options\nsettimeout(None | float) -- set or clear the timeout\nshutdown(how) -- shut down traffic in one or both directions\nif_nameindex() -- return all network interface indices and names\nif_nametoindex(name) -- return the corresponding interface index\nif_indextoname(index) -- return the corresponding interface name\n\n [*] not available on all platforms!"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _accept(self):
        '_accept() -> (integer, address info)\n\nWait for an incoming connection.  Return a new socket file descriptor\nrepresenting the connection, and the address of the client.\nFor IP sockets, the address info is a pair (hostaddr, port).'
        return tuple()
    
    def bind(self, address):
        'bind(address)\n\nBind the socket to a local address.  For IP sockets, the address is a\npair (host, port); the host must refer to the local host. For raw packet\nsockets the address is a tuple (ifname, proto [,pkttype [,hatype [,addr]]])'
        pass
    
    def close(self):
        'close()\n\nClose the socket.  It cannot be used after this call.'
        pass
    
    def connect(self, address):
        'connect(address)\n\nConnect the socket to a remote address.  For IP sockets, the address\nis a pair (host, port).'
        pass
    
    def connect_ex(self, address):
        'connect_ex(address) -> errno\n\nThis is like connect(address), but returns an error code (the errno value)\ninstead of raising an exception when an error occurs.'
        pass
    
    def detach(self):
        'detach()\n\nClose the socket object without closing the underlying file descriptor.\nThe object cannot be used after this call, but the file descriptor\ncan be reused for other purposes.  The file descriptor is returned.'
        pass
    
    @property
    def family(self):
        'the socket family'
        pass
    
    def fileno(self):
        'fileno() -> integer\n\nReturn the integer file descriptor of the socket.'
        return 1
    
    def getblocking(self):
        'getblocking()\n\nReturns True if socket is in blocking mode, or False if it\nis in non-blocking mode.'
        pass
    
    def getpeername(self):
        'getpeername() -> address info\n\nReturn the address of the remote endpoint.  For IP sockets, the address\ninfo is a pair (hostaddr, port).'
        pass
    
    def getsockname(self):
        'getsockname() -> address info\n\nReturn the address of the local endpoint.  For IP sockets, the address\ninfo is a pair (hostaddr, port).'
        pass
    
    def getsockopt(self, level, option, buffersize=None):
        'getsockopt(level, option[, buffersize]) -> value\n\nGet a socket option.  See the Unix manual for level and option.\nIf a nonzero buffersize argument is given, the return value is a\nstring of that length; otherwise it is an integer.'
        pass
    
    def gettimeout(self):
        'gettimeout() -> timeout\n\nReturns the timeout in seconds (float) associated with socket \noperations. A timeout of None indicates that timeouts on socket \noperations are disabled.'
        pass
    
    def ioctl(self, cmd, option):
        "ioctl(cmd, option) -> long\n\nControl the socket with WSAIoctl syscall. Currently supported 'cmd' values are\nSIO_RCVALL:  'option' must be one of the socket.RCVALL_* constants.\nSIO_KEEPALIVE_VALS:  'option' is a tuple of (onoff, timeout, interval).\nSIO_LOOPBACK_FAST_PATH: 'option' is a boolean value, and is disabled by default"
        return 1
    
    def listen(self, backlog=None):
        'listen([backlog])\n\nEnable a server to accept connections.  If backlog is specified, it must be\nat least 0 (if it is lower, it is set to 0); it specifies the number of\nunaccepted connections that the system will allow before refusing new\nconnections. If not specified, a default reasonable value is chosen.'
        pass
    
    @property
    def proto(self):
        'the socket protocol'
        pass
    
    def recv(self, buffersize, flags=None):
        'recv(buffersize[, flags]) -> data\n\nReceive up to buffersize bytes from the socket.  For the optional flags\nargument, see the Unix manual.  When no data is available, block until\nat least one byte is available or until the remote end is closed.  When\nthe remote end is closed and all data is read, return the empty string.'
        pass
    
    def recv_into(self, buffer, nbytes=None, flags=None):
        'recv_into(buffer, [nbytes[, flags]]) -> nbytes_read\n\nA version of recv() that stores its data into a buffer rather than creating \na new string.  Receive up to buffersize bytes from the socket.  If buffersize \nis not specified (or 0), receive up to the size available in the given buffer.\n\nSee recv() for documentation about the flags.'
        pass
    
    def recvfrom(self, buffersize, flags=None):
        "recvfrom(buffersize[, flags]) -> (data, address info)\n\nLike recv(buffersize, flags) but also return the sender's address info."
        return tuple()
    
    def recvfrom_into(self, buffer, nbytes=None, flags=None):
        "recvfrom_into(buffer[, nbytes[, flags]]) -> (nbytes, address info)\n\nLike recv_into(buffer[, nbytes[, flags]]) but also return the sender's address info."
        return tuple()
    
    def send(self, data, flags=None):
        'send(data[, flags]) -> count\n\nSend a data string to the socket.  For the optional flags\nargument, see the Unix manual.  Return the number of bytes\nsent; this may be less than len(data) if the network is busy.'
        pass
    
    def sendall(self, data, flags=None):
        "sendall(data[, flags])\n\nSend a data string to the socket.  For the optional flags\nargument, see the Unix manual.  This calls send() repeatedly\nuntil all data is sent.  If an error occurs, it's impossible\nto tell how much data has been sent."
        pass
    
    def sendto(self, data, flags=None, address=None):
        'sendto(data[, flags], address) -> count\n\nLike send(data, flags) but allows specifying the destination address.\nFor IP sockets, the address is a pair (hostaddr, port).'
        pass
    
    def setblocking(self, flag):
        'setblocking(flag)\n\nSet the socket to blocking (flag is true) or non-blocking (false).\nsetblocking(True) is equivalent to settimeout(None);\nsetblocking(False) is equivalent to settimeout(0.0).'
        pass
    
    def setsockopt(self, level, option, None_, optlen: int):
        'setsockopt(level, option, value: int)\nsetsockopt(level, option, value: buffer)\nsetsockopt(level, option, None, optlen: int)\n\nSet a socket option.  See the Unix manual for level and option.\nThe value argument can either be an integer, a string buffer, or \nNone, optlen.'
        pass
    
    def settimeout(self, timeout):
        "settimeout(timeout)\n\nSet a timeout on socket operations.  'timeout' can be a float,\ngiving in seconds, or None.  Setting a timeout of None disables\nthe timeout feature and is equivalent to setblocking(1).\nSetting a timeout of zero is the same as setblocking(0)."
        pass
    
    def share(self, process_id):
        'share(process_id) -> bytes\n\nShare the socket with another process.  The target process id\nmust be provided and the resulting bytes object passed to the target\nprocess.  There the shared socket can be instantiated by calling\nsocket.fromshare().'
        pass
    
    def shutdown(self, flag):
        'shutdown(flag)\n\nShut down the reading side of the socket (flag == SHUT_RD), the writing side\nof the socket (flag == SHUT_WR), or both ends (flag == SHUT_RDWR).'
        pass
    
    @property
    def timeout(self):
        'the socket timeout'
        pass
    
    @property
    def type(self):
        'the socket type'
        pass
    

class timeout(OSError):
    __class__ = timeout
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'socket'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

