# Manases Garcia
# CSCI 248 Homework #11 Challenge #11
# datastructures.py
# 11-13-2020
#
# This program has the Stack, Queue and EmptyCollectionError classes. 

"""Provide Stack, Queue, and EmptyCollectionError classes.

Stack -- a stack data structure
    __init__(self) -- create an empty stack
    push(self, item) -- add item to the top of the stack
    pop(self) -- remove and return item from the top of the stack
        (raise EmptyCollectionError if the stack is empty)
    peek(self) -- return item from the top of the stack
        (raise EmptyCollectionError if the stack is empty)
    is_empty(self) -- return whether or not the stack is empty
    size(self) -- return the number of items in the stack
    __str__(self) -- return a string representation from top to bottom

Queue -- a queue data structure
    __init__(self) -- create an empty queue
    enqueue(self, item) -- add item to the back of the queue
    dequeue(self) -- remove and return item from the front of the queue
        (raise EmptyCollectionError if the queue is empty)
    first(self) -- return item from the front of the queue
        (raise EmptyCollectionError if the queue is empty)
    is_empty(self) -- return whether or not the queue is empty
    size(self) -- return the number of items in the queue
    __str__(self) -- return a string representation from front to back

EmptyCollectionError  -- an empty collection exception
"""

class Stack:

    """Represent a stack data structure."""

    def __init__(self):
        """Create an empty stack."""
        self.__stack = []

    def push(self, item):
        """Add item to the top of the stack."""
        self.__stack.insert(0, item)

    def pop(self):
        """Remove and return item from the top of the stack.
        
        Raise: EmptyCollectionError if the stack is empty."""

        if len(self.__stack) == 0:
            raise EmptyCollectionError('Cannot pop from empty stack.')

        item = self.__stack[0]
        del self.__stack[0]
        return item

    def peek(self):
        """Return item from the top of the stack.
        
        Raise: EmptyCollectionError if the stack is empty."""

        if len(self.__stack) == 0:
            raise EmptyCollectionError('Cannot peek on empty stack.')
        return self.__stack[0]

    def is_empty(self):
        """Return whether or not the stack is empty."""
        return len(self.__stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.__stack)

    def __str__(self):
        """Return a string representation from top to bottom."""
        result = ''
        for item in self.__stack:
            result += str(item) + '\n'
        return result

class Queue:

    """Represent a queue data structure."""

    def __init__(self):
        """Create a empty structure."""
        self.__queue = []

    def enqueue(self, item):
        """Add an item to the end of the queue"""
        self.__queue.append(item)

    def dequeue(self):
        """Remove and item from the front of the queue
        
        Raise:EmptyCollectionError if the stack is empty"""

        if len(self.__queue) == 0:
            raise EmptyCollectionError('Cannot dequeue from empty queue')

        item = self.__queue[0]
        del self.__queue[0]
        return item

    def first(self):
        """Return item from the front of the queue.

        Raise:EmptyCollectionError if the queue is empty."""

        if len(self.__queue) == 0:
            raise EmptyCollectionError('Cannot return first from empty stack')
        return self.__queue[0]

    def is_empty(self):
        """Return whether of not the queue is empty."""
        return len(self.__queue) == 0

    def size(self):
        """Return the size of the queue."""
        return len(self.__queue)

    def __str__(self):
        """Return the sting representation from top to bottom"""

        result = ''
        for item in self.__queue:
            result += str(item) + '\n'
        return result
        

class EmptyCollectionError(Exception):

    """Represent an empty collection exception."""

    def __init__(self, message=''):
        Exception.__init__(self, message)

