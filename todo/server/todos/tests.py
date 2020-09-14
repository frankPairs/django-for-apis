from django.test import TestCase

from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first todo', body='todo test content')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected = f'{todo.title}'

        self.assertEqual(expected, 'first todo')

    def test_body_content(self):
        todo = Todo.obts.get(id=1)
        expected = f'{todo.body}'

        self.assertEqual(expected, 'todo test content')
