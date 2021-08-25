import pytest
import time
from selenium import webdriver
link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
def test_lang(browser):
    browser.get(link)
    time.sleep(15)
    assert browser.find_element_by_css_selector('.add-to-basket'), 'No element'





