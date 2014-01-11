# -*- coding:utf-8 -*-

class Person(object):
	"""docstring for Person"""

	obj_id = 0
	name = '***'

	def __init__(self, obj_id=1, name='AAaa'):
		super(Person, self).__init__()
		self.obj_id = obj_id
		self.name = name

	def __str__(self):
		return '{}{}'.format(self.obj_id, self.name)


def main():
	person = []
	vasya = Person(1, 'Vasya')
	print vasya

if __name__ == '__main__':
	main()