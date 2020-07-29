import unittest

def filter_list(l):
 return [x for x in l if type(x) == type(1)]

test.assert_equals(filter_list([1,2,'a','b']),[1,2])
test.assert_equals(filter_list([1,'a','b',0,15]),[1,0,15])
test.assert_equals(filter_list([1,2,'aasf','1','123',123]),[1,2,123])