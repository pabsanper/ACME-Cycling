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
from django.test.client import Client

class ProductoTestCase(TestCase):
      

    def setUp(self):
        super().setUp()
        c=Categoria(nombre="Montaña")
        c.save()
        d=Departamento(nombre="Ruedas")
        d.save()
        f=Fabricante(nombre="Decathlon")
        f.save()
       

        self.producto = Producto(categoria=c, departamento=d, fabricante=f, nombre="Rueda de montaña", descripcion="Rueda de montaña para bici grande",precio=20, stock=10)
        self.producto.save()

    def tearDown(self):
        super().tearDown()
        self.producto = None

    def testExist(self):
       producto = Producto.objects.first()
       self.assertEquals(producto.nombre, 'Rueda de montaña')

    def testDelete(self):
       instancias = Producto.objects.all().count()
       Producto.objects.first().delete()

       self.assertEquals(Producto.objects.all().count(), instancias-1)

class AdminTestCase(StaticLiveServerTestCase):

    def create_user(self):
        self.username = "admin"
        self.password = "qwerty"
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        self.user = user

    def setUp(self):
        self.base = TestCase()
        self.create_user()

        options = webdriver.ChromeOptions()
        options.headless = False
        self.driver = webdriver.Chrome(options=options)

        super().setUp()            
            
    def tearDown(self):           
        super().tearDown()
        self.driver.quit()

        self.base.tearDown()
    
    def testCreateFullAndDelete(self):      
        instancias = Producto.objects.all().count()              
        self.driver.get(f'{self.live_server_url}/admin/')
        self.driver.find_element(By.ID,'id_username').send_keys("admin")
        self.driver.find_element(By.ID,'id_password').send_keys("qwerty",Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, ".model-categoria .addlink").click()
        self.driver.find_element(By.ID, "id_nombre").send_keys("Montaña")
        self.driver.find_element(By.NAME, "_save").click()
        self.driver.find_element(By.LINK_TEXT, "Producto").click()
        self.driver.find_element(By.CSS_SELECTOR, ".model-departamento .addlink").click()
        self.driver.find_element(By.ID, "id_nombre").send_keys("Ruedas")
        self.driver.find_element(By.NAME, "_save").click()
        self.driver.find_element(By.LINK_TEXT, "Producto").click()
        self.driver.find_element(By.CSS_SELECTOR, ".model-fabricante .addlink").click()
        self.driver.find_element(By.ID, "id_nombre").send_keys("Arkea")
        self.driver.find_element(By.NAME, "_save").click()
        self.driver.find_element(By.LINK_TEXT, "Producto").click()
        self.driver.find_element(By.CSS_SELECTOR, ".model-producto .addlink").click()
        dropdown = self.driver.find_element(By.ID, "id_categoria")
        dropdown.find_element(By.XPATH, "//option[. = 'Montaña']").click()
        element = self.driver.find_element(By.ID, "id_categoria")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "id_categoria")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "id_categoria")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        dropdown = self.driver.find_element(By.ID, "id_departamento")
        dropdown.find_element(By.XPATH, "//option[. = 'Ruedas']").click()
        element = self.driver.find_element(By.ID, "id_departamento")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "id_departamento")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "id_departamento")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        dropdown = self.driver.find_element(By.ID, "id_fabricante")
        dropdown.find_element(By.XPATH, "//option[. = 'Arkea']").click()
        element = self.driver.find_element(By.ID, "id_fabricante")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "id_fabricante")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "id_fabricante")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "id_nombre").click()
        self.driver.find_element(By.ID, "id_nombre").send_keys("Rueda de montaña")
        self.driver.find_element(By.ID, "id_descripcion").click()
        self.driver.find_element(By.ID, "id_descripcion").send_keys("Rueda para ir por el campo")
        self.driver.find_element(By.ID, "id_precio").click()
        self.driver.find_element(By.ID, "id_precio").send_keys("20")
        self.driver.find_element(By.ID, "id_stock").click()
        self.driver.find_element(By.ID, "id_stock").send_keys("20")
        self.driver.find_element(By.NAME, "_save").click()
        self.assertEquals(Producto.objects.all().count(), instancias+1)

        instancias = Producto.objects.all().count()              
        self.driver.get(f'{self.live_server_url}/admin/')
        self.driver.find_element(By.LINK_TEXT, "Productos").click()
        self.driver.find_element(By.ID, "action-toggle").click()
        element = self.driver.find_element(By.NAME, "action")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.NAME, "action")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.NAME, "action")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "changelist-form").click()
        element = self.driver.find_element(By.ID, "changelist-form")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        dropdown = self.driver.find_element(By.NAME, "action")
        dropdown.find_element(By.XPATH, "//option[. = 'Eliminar productos seleccionado/s']").click()
        element = self.driver.find_element(By.NAME, "action")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.NAME, "action")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.NAME, "action")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.NAME, "index").click()
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(4)").click()
        self.assertEquals(Producto.objects.all().count(), instancias-1)