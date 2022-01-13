from django.test import TestCase
from .models import Stock

class StudentListViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        number_of_students = 30
        for student_id in range(number_of_students):
            Stock.objects.create(name=f"John{student_id}")
    def test_pagination_is_correct(self):
        response = self.client.get(reverse('students'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['student_list']), 10)