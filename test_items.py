import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

class TestBasket():
    def test_guest_should_see_basket_button_for_different_languages(self, browser):
      link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
      browser.get(link)
      time.sleep(30)
      element = browser.findElement(By.TAG_NAME, "button.btn[@type='submit']")
      assertElementPresent(element) == true, "Button is not present" 
