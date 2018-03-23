import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver import ActionChains


class SeleniumTests(StaticLiveServerTestCase):
    fixtures = ['user-data.json']

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_auth(self):

        driver = self.driver
        driver.get('%s%s' % (self.live_server_url, '/'))

        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_xpath("//ul[@id='login-dp']/li/div/div[2]/a/b").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("new")
        driver.find_element_by_id("id_email").click()
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("new@new.com")
        driver.find_element_by_id("id_password1").click()
        driver.find_element_by_id("id_password1").clear()
        driver.find_element_by_id("id_password1").send_keys("Master1996")
        driver.find_element_by_id("id_password2").click()
        driver.find_element_by_id("id_password2").clear()
        driver.find_element_by_id("id_password2").send_keys("Master1996")
        driver.find_element_by_class_name("btn-reg").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("exampleInputEmail2").click()
        driver.find_element_by_id("exampleInputEmail2").clear()
        driver.find_element_by_id("exampleInputEmail2").send_keys("new")
        driver.find_element_by_id("exampleInputPassword2").click()
        driver.find_element_by_id("exampleInputPassword2").send_keys("Master1996")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//h4").click()
        driver.find_element_by_link_text(u"Комментарии").click()
        driver.find_element_by_id("comment_text").click()
        driver.find_element_by_id("comment_text").clear()
        driver.find_element_by_id("comment_text").send_keys("Best!!!")
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        driver.find_element_by_id("submit-btn").click()
        driver.find_element_by_id("submit-btn").click()

        action = ActionChains(driver)
        hidden_submenu = driver.find_element_by_id("basket_total_amount")
        action.move_to_element(hidden_submenu).perform()
        time.sleep(1)

        driver.find_element_by_link_text(u"Оформить заказ").click()
        driver.find_element_by_name("phone").click()
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Logout").click()

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
