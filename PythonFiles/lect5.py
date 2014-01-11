# -*- coding:utf-8 -*-

class Person(object):
	"""docstring for Person"""

	obj_id = 0
	name = '***'

	def __init__(self, obj_id=None, name=None):
		super(Person, self).__init__()
		self.obj_id = obj_id
		self.name = name

	def __str__(self):
		return '{name} {obj_id}'.format(**self.attributes())

	def attributes(self):
		return {
			'name' : self.name,
			'obj_id' : self.obj_id
			}



def main():
	vasya = Person(45, 'Vasya')
	print vasya

if __name__ == '__main__':
	main()