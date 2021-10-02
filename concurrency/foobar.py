from contextlib import contextmanager
from datetime import datetime
import threading
import asyncio
import time
import random

global locked
locked = True

class FooBar:
    def __init__(self, n):
        self.n = n
        self.i = 0
        self.lock = threading.Lock()
        #print('init')


    def getLock(self,condition) :
        global locked
        if(locked != condition):
            #print('not yet')
            time.sleep(random.random())
            self.getLock(condition)
        else :
            self.lock.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
            global locked
            #print('calling foo')
            condition = True
            for i in range(self.n):
                #print('in foo loop ', i)
                self.getLock(condition)
                #print('foo got lock')
                ## printFoo() outputs "foo". Do not change or remove this line.
                #print('printing foo')
                locked = not condition
                self.lock.release()
                printFoo()
                #print('release foo')
                

    def bar(self, printBar: 'Callable[[], None]') -> None:
            global locked
            #print('calling bar')
            condition = False
            for i in range(self.n):
                #print('in bar loop ', i)
                self.getLock(condition)
                #print('bar got lock')
                ## printBar() outputs "bar". Do not change or remove this line.
                #print('printing bar')
                locked = not condition
                self.lock.release()
                printBar()
                #print('release bar')
                
                
            
