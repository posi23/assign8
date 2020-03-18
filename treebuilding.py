# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.
#

import treenode as tn

def build_lecture_example():
    """
    Purpose:
        returns the example found in the lecture slides
    """
    atree = tn.create(2)
    a = tn.create(7)
    b = tn.create(5)
    tn.set_left(atree, a)
    tn.set_right(atree, b)
    c = tn.create(11)
    d = tn.create(6)
    tn.set_left(a, c)
    tn.set_right(a, d)
    return atree


def build_turtle():
    """
    Purpose:
        returns a simple tree with single letter data values
    """
    atree = tn.create('t', tn.create('u', tn.create('t'), tn.create('r')), 
                           tn.create('e', tn.create('l'), None))
    return atree

def build_tuttle():
    """
    Purpose:
        returns a simple tree with single letter data values
        this tree is slightly different from the previous tree
    """
    atree = tn.create('t', tn.create('u', tn.create('t'), tn.create('t')), 
                           tn.create('e', tn.create('l'), None))
    return atree
    
# a larger more e-xtree-me tree
def build_xtree_me():
    """
    Purpose:
        builds a slightly larger, more or less undistinguished tree
    """
    xtree = tn.create(5,
                  tn.create(1,None,
                            tn.create(4,
                                      tn.create(3,tn.create(2,None,None),None),
                                      None)),
                  tn.create(9,tn.create(8,tn.create(7,tn.create(6,None,None),None),None),
                              tn.create(1,tn.create(3,None,None),tn.create(3,None,None))))
    return xtree


def treeify(alist):
    """
    Purpose:
        Create a tree using the given list.
       The first node in the tree is the data value of the root.
       The first half of the remaining nodes form the left subtree.
       The second half of the remaining nodes form the right subtree.
       If the list has an even length, the left subtree will be slightly bigger then the right
    Pre:
        :param alist: a Python list
    Return:
        :return: a primitive tree structure (tnode)
    """

    if len(alist) == 0:
        # if there are no values, return empty tree
        return None
    elif len(alist) == 1:
        # if just one value, create a leaf
        return tn.create(alist[0])
    else:
        # split the list in half, and build two roughly equal subtrees
        mid = 1 + len(alist)//2
        return tn.create(alist[0], treeify(alist[1:mid]), treeify(alist[mid:]))


def build_complete(height, d=0):
    """
    Purpose:
        Create a complete binary tree of the given height.
        The data value for the root of the tree is d
    Pre-conditions:
        :param height: a non-negative integer
        :param d: (optional) an integer, used as the value for the root of the tree
    Return:
        :return: a complete primitive binary tree whose root has data value d
    """
    if height == 0:
        return None
    else:
        return tn.create(d,build_complete(height-1,2*d+1), build_complete(height-1,2*d+2))


def build_fibtree(n):
    """
    Purpose:
        Build a tree whose structure represents the Fibonacci numbers.
        The root of the tree has data value Fib(n).
        This function can return very large trees.  
    Pre-conditions:
        :param n: a non-negative integer
    Return:
        :return: a primitive binary tree whose structure reflects the calculation of fib(n)
    """
    if n <= 1:
        return tn.create(n)
    else:
        ltree = build_fibtree(n-1)
        rtree = build_fibtree(n-2)
        return tn.create(tn.get_data(ltree)+tn.get_data(rtree), ltree, rtree)

