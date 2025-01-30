from unittest import skip
from django.test import TransactionTestCase
from project_prj.models import Task


class WidgetTransactionTestCase(TransactionTestCase):
    def test_widget_creation(self):
        Task.objects.create(name='Парфюмерия')
        Task.objects.create(name='Гель для душа')
        self.assertEqual(Task.objects.count(), 2)
