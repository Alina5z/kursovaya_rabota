# from unittest import skip
# from django.test import TestCase
# from project_prj.models import Task
#
# class TaskModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         Task.objects.create(
#             name='Test Product',
#             place='Test Place',
#             price=10,
#             square=5
#         )
#
#     def test_name_content(self):
#         task = Task.objects.get(id=1)
#         expected_name = f'{task.name}'
#         self.assertEqual(expected_name, 'Test Product')
#
#     def test_str_method(self):
#         task = Task.objects.get(id=1)
#         self.assertEqual(str(task), task.name)