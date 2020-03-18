# OLAOLUWAPOSI ADEYEMI
# 11267056
# ooa642
# CMPT 145- 02

import treenode as tn
import treefunctions as tf


def subst(tnode, t, r):
	"""
	Purpose: To substitute a target value t with a replacement value r wherever it appears as a data value
		in the given tree
	Pre-conditions:
		tnode: the given tree node
		t: target value
		r: replacement value
	Post conditions: the target value is replaced with the replacement value
	Return: None
	"""
	if tnode is not None and tn.get_data(tnode) == t:
		tn.set_data(tnode, r)
	elif tnode is None:
		pass
	else:
		subst(tn.get_right(tnode), t, r)
		subst(tn.get_left(tnode), t, r)


root = tn.create(7)
a = tn.create(5)
b = tn.create(5)
c = tn.create(5)
tn.set_left(root, a)
tn.set_right(root, b)
tn.set_right(b, c)

print(root)


def count_target(tnode, target):
	"""
	Purpose: Counts the number of times the given target appears in the given tree
	Pre-condition:
		tnode: the given tree node
		target: the target value
	Post condition: None
	Return: the number of times the given target value appears in the given tree
	"""
	count = 0
	if tnode is None:
		pass
	else:
		if tn.get_data(tnode) == target:
			count += 1
		count += count_target(tn.get_right(tnode), target)
		count += count_target(tn.get_left(tnode), target)
	return count


def sum_leaf_values(tnode):
	"""
	Purpose: returns the sum of all the leaf values in the given tree
	Pre-conditions:
		tnode: the given tree node
	Post condition: None
	Return: the sum of all the leaf values in the tree
	"""
	count = 0
	if tnode is None:
		pass
	elif tf.is_leaf(tnode):
		count += 1
	else:
		count += sum_leaf_values(tn.get_left(tnode))
		count += sum_leaf_values(tn.get_right(tnode))
	return count


def min_level(tnode):
	"""
	Purpose: Returns the height of the leaf node with the smallest level
	Pre-condition:
		tnode: the given tree node
	Post condition: None
	Return: the height of the leaf node at with the smallest level
	"""
	height = 0
	if tnode is None:
		pass
	else:
		if tn.get_right(tnode) is not None or tn.get_left(tnode) is not None:
			height += 1
		height += min_level(tn.get_left(tnode))
		height += min_level(tn.get_right(tnode))
	return height
