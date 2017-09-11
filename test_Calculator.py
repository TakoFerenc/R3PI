import unittest
import time
from appium import webdriver
from subprocess import Popen
from device_config import Config
from app_locators import AppLocators
from verify_calculations import VerifyCalculations


class TestCalculatorApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.process = Popen('appium -a 0.0.0.0 -p 4723', shell=True)
        time.sleep(10)
        cls.desired_caps = Config.desired_capabilities()
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cls.desired_caps[0])
        cls.driver.implicitly_wait(30)
        cls.applocators = AppLocators()
        cls.element = cls.applocators.locator
        cls.calc = VerifyCalculations()

    def test_a_all_UI_elements(self):
        self.assertTrue(self.element('TITLE_TEXT'))
        self.assertEqual('Calculator', self.element('TITLE_TEXT').get_attribute('text'))
        self.assertTrue(self.element('STITLE_TEXT'))
        self.assertEqual('Wonky calculator app', self.element('STITLE_TEXT').get_attribute('text'))
        self.assertTrue(self.element('RESULT'))
        self.assertEqual('Result:', self.element('RESULT').get_attribute('text'))
        self.assertTrue(self.element('ADD_BTN'))
        self.assertEqual('ADD', self.element('ADD_BTN').get_attribute('text'))
        self.assertTrue(self.element('SUB_BTN'))
        self.assertEqual('SUBTRACT', self.element('SUB_BTN').get_attribute('text'))
        self.assertTrue(self.element('SQRT_BTN'))
        self.assertEqual('SQUARE ROOT', self.element('SQRT_BTN').get_attribute('text'))
        self.assertTrue(self.element('DIVIDE_BTN'))
        self.assertEqual('DIVIDE by 2', self.element('DIVIDE_BTN').get_attribute('text'))
        self.assertTrue(self.element('MULTI_BTN'))
        self.assertEqual('MULTIPLY by 2', self.element('MULTI_BTN').get_attribute('text'))
        self.assertTrue(self.element('POWER_BTN'))
        self.assertEqual('POWER by 2', self.element('POWER_BTN').get_attribute('text'))

    def test_add_functionality(self):
        self.calc.get_current_result()
        self.calc.tap_the_button(self.element('ADD_BTN'), 9)
        self.assertEqual(self.calc.add_one(), self.calc.get_current_result())

    def test_subtract_functionality(self):
        self.calc.get_current_result()
        self.calc.tap_the_button(self.element('SUB_BTN'), 3)
        self.assertEqual(self.calc.subtract_one(), self.calc.get_current_result())

    def test_square_root_functionality(self):
        self.calc.get_current_result()
        self.calc.tap_the_button(self.element('SQRT_BTN'), 2)
        self.assertEqual(self.calc.square_root(), self.calc.get_current_result())

    def test_divide_functionality(self):
        self.calc.get_current_result()
        self.calc.tap_the_button(self.element('DIVIDE_BTN'), 4)
        self.assertEqual(self.calc.devide_by_two(), self.calc.get_current_result())

    def test_multiply_functionality(self):
        self.calc.get_current_result()
        self.calc.tap_the_button(self.element('MULTI_BTN'), 3)
        self.assertEqual(self.calc.multiply_by_two(), self.calc.get_current_result())

    def test_power_functionality(self):
        self.calc.get_current_result()
        self.calc.tap_the_button(self.element('POWER_BTN'), 2)
        self.assertEqual(self.calc.power_by_two(), self.calc.get_current_result())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        Popen(f"TASKKILL /F /PID {cls.process.pid} /T")

    @classmethod
    def pass_driver(cls):
        return cls.driver
