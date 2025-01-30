from unittest import skip
from django.test import LiveServerTestCase
from selenium import webdriver
from project_prj.models import Task
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class NameFunctionalTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    def test_product_list_functional(self):
        Task.objects.create(name='Черный')
        Task.objects.create(name='Белый')

        self.selenium.get(self.live_server_url + '/task/')
        self.assertIn('Список Товаров', self.selenium.title)
        names = self.selenium.find_elements(By.TAG_NAME, 'td')
        self.assertEqual(len(names), 2)
        self.assertEqual(names[0].text, 'Черный')
        self.assertEqual(names[1].text, 'Белый')