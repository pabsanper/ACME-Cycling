from django.test import TestCase
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from producto.models import Producto,Fabricante,Categoria,Departamento
from finalizarCompra.models import Venta
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestCarrito(StaticLiveServerTestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    c=Categoria(nombre="Montaña")
    c.save()
    d=Departamento(nombre="Ruedas")
    d.save()
    f=Fabricante(nombre="Decathlon")
    f.save()
       

    self.producto = Producto(categoria=c, departamento=d, fabricante=f, nombre="Rueda de montaña", descripcion="Rueda de montaña para bici grande",precio=20, stock=10)
    self.producto.save()
  
  def tearDown(self):
    self.driver.quit()
  
  def test_carrito(self):
    ventas=Venta.objects.all().count()
    self.driver.get(f'{self.live_server_url}')
    self.driver.set_window_size(1846, 1016)
    self.driver.find_element(By.LINK_TEXT, "Productos").click()
    self.driver.find_element(By.LINK_TEXT, "Agregar al carrito").click()
    self.driver.find_element(By.LINK_TEXT, "+").click()
    self.driver.find_element(By.LINK_TEXT, "Finalizar compra").click()
    alert = self.driver.switch_to.alert
    alert.accept()
    self.driver.find_element(By.NAME, "nombre").click()
    self.driver.find_element(By.NAME, "nombre").send_keys("Pablo")
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("pablitosantospsp@gmail.com")
    self.driver.find_element(By.NAME, "direccion").click()
    self.driver.find_element(By.NAME, "direccion").send_keys("C/ Reina Mercedes s/n")
    self.driver.find_element(By.NAME, "metodoPago").click()
    self.driver.find_element(By.NAME, "metodoEnvio").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.assertEquals(Venta.objects.all().count(), ventas)