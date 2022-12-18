import unittest
from main import one_to_many, many_to_many
from main import task_1
from main import task_2
from main import task_3


class TestProgramm(unittest.TestCase):

	def test_task1(self):
		result = [
			(4, 1, 'Заметки'),
			(1, 1, 'Книга'),
			(5, 2, 'Книга1'),
			(2, 2, 'Курсовая'),
			(3, 3, 'Приказ'),
			(3, 4, 'Приказ'),
			(3, 5, 'Приказ'),
			(6, 3, 'Сборник указов '),
			(6, 4, 'Сборник указов '),
			(6, 5, 'Сборник указов ')
		]

		self.assertEqual(task_1(one_to_many), result)

	def test_task2(self):
		result = [
			('Приказ', 12),
			('Сборник указов ', 12),
			('Курсовая', 2),
			('Книга1', 2),
			('Книга', 1),
			('Заметки', 1)
		]

		self.assertEqual(task_2(one_to_many), result)


	def test_task3(self):
		result = {
			'Книга': ['От автора'], 
			'Книга1': ['Введение']
		}

		self.assertEqual(task_3(many_to_many), result)



if __name__ == '__main__':
	unittest.main()