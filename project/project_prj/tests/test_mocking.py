from unittest import skip
from django.test import TestCase, RequestFactory
from unittest.mock import Mock, patch
from project_prj.models import Task
from project_prj.views import index


class GoogListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_name_list_view(self):
        Task.objects.create(title='Белый', price=100)
        Task.objects.create(title='Черный', price=1000)

        request = self.factory.get('/index/')

        mock_queryset = Mock(spec=Task.objects.all())
        mock_queryset.return_value = [
            Mock(title='Сыр', price=100),
            Mock(title='Торт', price=1000)
        ]

        with patch('blog.views.Goog.objects.all', mock_queryset):
            response = index(request)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Белый', 100)
        self.assertContains(response, 'Черный', 1000)