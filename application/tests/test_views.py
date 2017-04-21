from django.test import TestCase
from django.urls import reverse_lazy
from django.http import JsonResponse


class ViewTest(TestCase):
    fixtures = ['initial.json']

    def test_application_view(self):
        url = reverse_lazy("application")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)
        self.assertTrue('form_extra' in response.context)

    def test_update_specialists(self):
        # Extra parameters to make this a Ajax style request.
        kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        data = {'specialist_id': '1', }
        url = reverse_lazy("update_specialists")
        response = self.client.post(url, data, **kwargs)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), JsonResponse)
