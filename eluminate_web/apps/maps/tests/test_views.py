from django.core.urlresolvers import reverse

from django.test import LiveServerTestCase
from django.test.client import Client
from maps.models import Location
from selenium import webdriver

class LocationViewsTest(LiveServerTestCase):
    fixtures = ['maps_test_fixture.json']
    
    def setUp(self):
        self.client = Client()
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(6)
    
    def tearDown(self):
        self.browser.quit()
        
    def test_list_locations(self):
        
        # login
        login = self.client.login(username="test", password="test")
        self.assertEqual(login, True)
        
        response = self.client.get(reverse('locations_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_add_location(self):
        
        #login
        self.browser.get(self.live_server_url)
        login = self.browser.find_element_by_link_text("Log in")
        login.click()
                
        username = self.browser.find_element_by_id("id_username")
        username.send_keys("test")
        
        password = self.browser.find_element_by_id("id_password")
        password.send_keys("test")
        
        submit = self.browser.find_element_by_class_name("btn-primary")
        submit.click()
        
        self.browser.get(self.live_server_url + reverse('add_location'))
        
        location_name = "test_location"
        loc_name = self.browser.find_element_by_id("id_name")
        loc_name.send_keys(location_name)
        
        submit = self.browser.find_element_by_id("submit-id-submit")
        
        submit.click()
        
        loc = Location.objects.get(name=location_name)
        self.assertEqual(loc.name, location_name)
    
    def test_add_location_error_handling_when_no_name_supplied(self):
        """test if the error is displayed properly if no name is added"""
               #login
        self.browser.get(self.live_server_url)
        login = self.browser.find_element_by_link_text("Log in")
        login.click()
                
        username = self.browser.find_element_by_id("id_username")
        username.send_keys("test")
        
        password = self.browser.find_element_by_id("id_password")
        password.send_keys("test")
        
        submit = self.browser.find_element_by_class_name("btn-primary")
        submit.click()
        
        
        # We try to submit a location without a name
        self.browser.get(self.live_server_url + reverse('add_location'))
        submit = self.browser.find_element_by_id("submit-id-submit")
        submit.click()
        
        #An error should be displayed now
        name_error = self.browser.find_element_by_class_name("error")
        self.assertIn("This field is required", name_error.text)
        
        
        