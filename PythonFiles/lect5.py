# -*- coding:utf-8 -*-
# Created by Kirill Osipov on 2014-01-11.
# Copyright (c) 2014 by Kirill Osipov.  All rights reserved.

from re import findall

data = ['23.4 Vasya Пупкин', '44 Ivam', '25 Andrey']

class Person(object):
	"""docstring for Person"""

	def __init__(self, **kwargs):
		super(Person, self).__init__()
		self.__dict__.update(kwargs)

	def __str__(self):
		str_form = '{} ' * self.__len__()
		items = (str_form.format(k, self.__dict__[k]).strip() for k in self.__dict__)
		return '|'.join(items)

	def __len__(self):
		return len(self.__dict__.keys())

def parsed(inStr=None):
	regex_dig = ur'[,.\d]+'
	regex_cha = ur'[^\d., ]+'
	return dict(digit=''.join(findall(regex_dig, inStr)),
				word=' '.join(findall(regex_cha, inStr))
			)

def main():
	humans = [Person(age=parsed(item)['digit'], name=parsed(item)['word']) for item in data]

	vasya = humans[0]
	print vasya
	print len(vasya)
	print vasya.__dict__
	print vasya.__doc__
	print vasya.__hash__()

if __name__ == '__main__':
	main()