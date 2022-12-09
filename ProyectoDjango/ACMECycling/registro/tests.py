from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from producto.models import Producto,Fabricante,Categoria,Departamento
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

class AdminTestCase(StaticLiveServerTestCase):

    def setUp(self):
        self.base = TestCase()

        options = webdriver.ChromeOptions()
        options.headless = False
        self.driver = webdriver.Chrome(options=options)

        super().setUp()            
            
    def tearDown(self):           
        super().tearDown()
        self.driver.quit()

        self.base.tearDown()

    def testRegistroLogin(self):   
        instancias = User.objects.all().count()                 
        self.driver.get(f'{self.live_server_url}')
        self.driver.set_window_size(1846, 1016)
        self.driver.find_element(By.LINK_TEXT, "Regístrate").click()
        self.driver.find_element(By.ID, "id_username").send_keys("newuser")
        self.driver.find_element(By.ID, "id_password1").click()
        self.driver.find_element(By.ID, "id_password1").send_keys("complexpassword")
        self.driver.find_element(By.ID, "id_password2").click()
        self.driver.find_element(By.ID, "id_password2").click()
        self.driver.find_element(By.ID, "id_password2").send_keys("complexpassword")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        alert = self.driver.switch_to.alert
        alert.accept()
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.find_element(By.ID, "id_username").send_keys("pablo")
        self.driver.find_element(By.ID, "id_password").send_keys("complexpassword")
        self.driver.find_element(By.CSS_SELECTOR, ".element:nth-child(2)").click()
        self.driver.find_element(By.ID, "id_username").send_keys("newuser")
        self.driver.find_element(By.ID, "id_password").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
  
        self.assertEquals(User.objects.all().count(), instancias+1)
