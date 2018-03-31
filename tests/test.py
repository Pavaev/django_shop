import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver import ActionChains

from .models import *


class TestBase(StaticLiveServerTestCase):
    serialized_rollback = True
    fixtures = ['user-data.json']

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def auth(self, user):
        driver = self.driver
        driver.get('%s%s' % (self.live_server_url, '/'))

        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("exampleInputEmail2").click()
        driver.find_element_by_id("exampleInputEmail2").clear()
        driver.find_element_by_id("exampleInputEmail2").send_keys(user.username)
        driver.find_element_by_id("exampleInputPassword2").click()
        driver.find_element_by_id("exampleInputPassword2").send_keys(user.password)
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def comments_test(self, comment):
        driver = self.driver
        driver.get('%s%s' % (self.live_server_url, '/'))

        driver.find_element_by_xpath("//h4").click()
        driver.find_element_by_link_text(u"Комментарии").click()
        driver.find_element_by_id("comment_text").click()
        driver.find_element_by_id("comment_text").clear()
        driver.find_element_by_id("comment_text").send_keys(comment.text)
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        driver.find_element_by_link_text("Logout").click()

    def orders_without_auth_test(self, order):
        driver = self.driver
        driver.get('%s%s' % (self.live_server_url, '/'))

        driver.find_element_by_xpath("//h4").click()
        driver.find_element_by_id("submit-btn").click()
        driver.find_element_by_id("submit-btn").click()

        action = ActionChains(driver)
        hidden_submenu = driver.find_element_by_id("basket_total_amount")
        action.move_to_element(hidden_submenu).perform()
        time.sleep(1)

        driver.find_element_by_link_text(u"Оформить заказ").click()
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(order.username)
        driver.find_element_by_name("phone").click()
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys(order.phone)
        driver.find_element_by_name("order").click()
        print('Meow')

class TestOrders(TestBase):

    def test(self):
        print('Run orders test...')

        self.orders_without_auth_test(order=OrderModel(username='user', phone='12'))


class TestComments(TestBase):

    def test(self):
        print('Run comments test...')

        self.auth(user=AuthModel("admin", "7zsulnlH"))
        self.comments_test(comment=CommentModel(text='Best!!!'))
