# -*- coding:utf-8 -*-
# Copyright (c) 2014 by Kirill Osipov.  All rights reserved.

class Person(object):
	"""docstring for Person"""

	def __init__(self, **kwargs):
		super(Person, self).__init__()
		self.__dict__.update(kwargs)

	def __str__(self):
		items = ("{}: {}".format(k, self.__dict__[k]) for k in self.__dict__)
		return '\n'.join(items)

	def __len__(self):
		return len(self.__dict__.keys())



def main():
	vasya = Person(age=41, name='Vasya')

	print vasya
	print len(vasya)
	print dir(vasya)
	print vasya.__dict__
	print vasya.__doc__
	print vasya.__hash__()

if __name__ == '__main__':
	main()