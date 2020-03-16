# OLAOLUWAPOSI ADEYEMI
# 11267056
# ooa642
# CMPT 145- 02

import treenode as tn
import treefunctions as tf
import node


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


root = tn.create(3)
a = tn.create(7)
b = tn.create(5)
c = tn.create(10)
tn.set_left(root, a)
tn.set_right(root, b)
tn.set_right(b, c)

print(root)
subst(root, 8, 9)
#print(tn.get_right(root))
print(root)