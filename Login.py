import time
import unittest
from selenium.webdriver.common.by import By
from appium import webdriver


class RegistroModulo(unittest.TestCase):
    # Primer Test Case
    @staticmethod
    def test_RE01():
        # Inicializacion de Manejador Appium
        desired_caps = {
            "platformName": "Android",
            "appium:platformVersion": "10",
            "appium:deviceName": "dandelion_global ",
            "appium:automationName": "UiAutomator1",
            "appium:appPackage": "com.habitsv2",
            "appium:appActivity": ".MainActivity"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        driver.implicitly_wait(6)

        # Activar modo Desarrollo
        for i in range(1, 11):
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget."
                                          "LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout"
                                          "/android.widget.FrameLayout/android.widget.FrameLayout/android.view."
                                          "ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                          "android.view.ViewGroup/android.widget.FrameLayout/"
                                          "android.view.ViewGroup/android.view.ViewGroup/android.v"
                                          "iew.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                          "android.view.ViewGroup/android.view.ViewGroup/android.view."
                                          "ViewGroup[1]/android.widget.ImageView").click()

        modal = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget"
                                              ".LinearLayout/android.widget.FrameLayout/android.widget."
                                              "LinearLayout/android.widget.FrameLayout/android.widget."
                                              "FrameLayout/android.view.ViewGroup/android.view.ViewGroup/"
                                              "android.view.ViewGroup/android.view.ViewGroup/android.widget."
                                              "FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android"
                                              ".view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup"
                                              "/android.view.ViewGroup")

        # Confirmar si la modal para modo desarrollo esta visible
        modalisvisible = modal.is_displayed()

        if modalisvisible is True:
            contra = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget."
                                                   "LinearLayout/android.widget.FrameLayout/android.widget."
                                                   "LinearLayout/android.widget.FrameLayout/android.widget."
                                                   "FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
                                                   "/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                                                   ".FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android"
                                                   ".view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup"
                                                   "/android.view.ViewGroup/android.view.ViewGroup[2]/android."
                                                   "widget.EditText")
            contra.send_keys("12345678")
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout"
                                          "/android.widget.LinearLayout/android.widget"
                                          ".FrameLayout/android.widget.LinearLayout/android"
                                          ".widget.FrameLayout/android.widget.FrameLayout/android"
                                          ".view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                          "/android.view.ViewGroup/android.widget.FrameLayout/android.view"
                                          ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android."
                                          "view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                          "android.view.ViewGroup[3]/android.widget.TextView").click()
        else:
            print("No se desplego la modal")

        modal2 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/"
                                               "android.widget.LinearLayout/android.widget"
                                               ".FrameLayout/android.widget.LinearLayout/android."
                                               "widget.FrameLayout/android.widget.FrameLayout/android"
                                               ".view.ViewGroup[1]/android.view.ViewGroup/android.view.V"
                                               "iewGroup/android.view.ViewGroup/android.widget.FrameLayout"
                                               "/android.view.ViewGroup/android.view.ViewGroup/android.vi"
                                               "ew.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGr"
                                               "oup/android.view.ViewGroup/android.widget.TextView")

        modal2isvisible = modal2.is_displayed()
        # Seleccionar opcion Desarrollo
        if modal2isvisible is True:
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout"
                                          "/android.widget.LinearLayout/android.widget"
                                          ".FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget."
                                          "FrameLayout/android.view.ViewGroup[1]/android"
                                          ".view.ViewGroup/android.view.ViewGroup/android"
                                          ".view.ViewGroup/android.widget.FrameLayout"
                                          "/android.view.ViewGroup/android.view.ViewGroup"
                                          "/android.view.ViewGroup[2]/android.view.ViewGroup"
                                          "/android.view.ViewGroup/android.view.ViewGroup/"
                                          "android.view.ViewGroup[3]/android.view.ViewGroup").click()

            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android."
                                          "widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                          ".LinearLayout/android.widget.FrameLayout/android.widget."
                                          "FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup"
                                          "/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                                          ".FrameLayout/android.view.ViewGroup/android.view.ViewGroup/"
                                          "android.view.ViewGroup[2]/android.view.ViewGroup/android.view"
                                          ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]").click()
        else:
            print("Modal par seleccionar opcion desarrollo no esta visible")

        time.sleep(2)

        #Registrar usuario

        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget"
                                      ".LinearLayout/android.widget.FrameLayout/android.widget"
                                      ".LinearLayout/android.widget.FrameLayout/android.widget."
                                      "FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
                                      "/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                                      ".FrameLayout/android.view.ViewGroup/android.view.ViewGroup/"
                                      "android.view.ViewGroup/android.view.ViewGroup/android.view"
                                      ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                      "android.view.ViewGroup[3]").click()

        codigo = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android."
                                               "widget.LinearLayout/android.widget.FrameLayout/android"
                                               ".widget.LinearLayout/android.widget.FrameLayout/android"
                                               ".widget.FrameLayout/android.view.ViewGroup/android.view"
                                               ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                               "/android.widget.FrameLayout/android.view.ViewGroup/android"
                                               ".view.ViewGroup/android.view.ViewGroup/android.view."
                                               "ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                               "android.widget.FrameLayout/android.view.ViewGroup/android"
                                               ".view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                               "/android.view.ViewGroup/android.view.ViewGroup/android."
                                               "view.ViewGroup/android.widget.ScrollView/android.view."
                                               "ViewGroup/android.view.ViewGroup[1]/android.widget.EditText")
        codigo.send_keys("comlic")

        time.sleep(5)










        driver.find_element(By.XPATH, "/hierarchy"
                                      "/android.widget.FrameLayout/android.widget.LinearLayout/"
                                      "android.widget.FrameLayout/android.widget.LinearLayout/"
                                      "android.widget.FrameLayout/android.widget.FrameLayout/"
                                      "android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                      "/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup"
                                      "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                      "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                      "/android.view.ViewGroup[3]/android.widget.TextView").click()


if __name__ == '__main__':
    unittest.main()
