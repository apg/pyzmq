import sys, os
import time

import zmq

def main():

    c = zmq.Context(1,1,zmq.POLL)
    s1 = zmq.Socket(c, zmq.REQ)
    s1.bind('tcp://127.0.0.1:5555')

    poller = zmq.Poller()
    poller.register(s1)
    socks = poller.poll()
    # I needed this to get rid of an error:
    # Assertion failed: err == ECONNREFUSED || err == ETIMEDOUT (tcp_connecter.cpp:283)
    # Abort trap.
    # time.sleep(0.0001)
    print socks
    # for s, mask in socks:
    #     if s is s1:
    #         self.assertEquals(mask, zmq.POLLOUT)
    #     if s is s2:
    #         self.assertEquals(mask, 0)
    # If I do s1.send('asdf') and then poll I don't get the right
    # flags back. I am getting POLLIN for both.
    s1.send('asdf')
    socks = poller.poll()
    print socks
    time.sleep(1.0)
    poller.unregister(s1)

if __name__ == '__main__':
    main()