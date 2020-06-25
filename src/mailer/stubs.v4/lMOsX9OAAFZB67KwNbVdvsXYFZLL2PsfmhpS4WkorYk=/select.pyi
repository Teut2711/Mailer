import builtins as _mod_builtins

__doc__ = 'This module supports asynchronous I/O on multiple file descriptors.\n\n*** IMPORTANT NOTICE ***\nOn Windows, only sockets are supported; on Unix, all file descriptors.'
__file__ = 'c:\\python37\\dlls\\select.pyd'
__name__ = 'select'
__package__ = ''
error = _mod_builtins.OSError
def select(rlist, wlist, xlist, timeout=None):
    "select(rlist, wlist, xlist[, timeout]) -> (rlist, wlist, xlist)\n\nWait until one or more file descriptors are ready for some kind of I/O.\nThe first three arguments are sequences of file descriptors to be waited for:\nrlist -- wait until ready for reading\nwlist -- wait until ready for writing\nxlist -- wait for an ``exceptional condition''\nIf only one kind of condition is required, pass [] for the other lists.\nA file descriptor is either a socket or file object, or a small integer\ngotten from a fileno() method call on one of those.\n\nThe optional 4th argument specifies a timeout in seconds; it may be\na floating point number to specify fractions of seconds.  If it is absent\nor None, the call will never time out.\n\nThe return value is a tuple of three lists corresponding to the first three\narguments; each contains the subset of the corresponding file descriptors\nthat are ready.\n\n*** IMPORTANT NOTICE ***\nOn Windows, only sockets are supported; on Unix, all file\ndescriptors can be used."
    return tuple()

