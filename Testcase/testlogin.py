import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import Service
service=Service(executable_path="H:\\chromedriver_win32 (1)\\chromedriver.exe")
class Test_001:
 def test_log(self):
           self.driver=webdriver.Chrome(service=service)
           self.driver.get("www.facebook.com")
           act=self.driver.title
           assert "Log in to Facebook"==act

# executable_path="H:\\chromedriver_win32 (1)\\chromedriver.exe"






        # Log in to Facebook
