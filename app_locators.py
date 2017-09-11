import test_Calculator


class AppLocators:

    def __init__(self):
        self.driver = test_Calculator.TestCalculatorApp.pass_driver()

    def locator(self, name):
        return {'TITLE_TEXT': self.driver.find_element_by_id(r"android:id/title"),
                'STITLE_TEXT': self.driver.find_element_by_id(r"com.test.calc:id/title"),
                'ADD_BTN': self.driver.find_element_by_id(r"com.test.calc:id/add"),
                'SUB_BTN': self.driver.find_element_by_id(r"com.test.calc:id/subtract"),
                'SQRT_BTN': self.driver.find_element_by_id(r"com.test.calc:id/sqrt"),
                'DIVIDE_BTN': self.driver.find_element_by_id(r"com.test.calc:id/divide"),
                'MULTI_BTN': self.driver.find_element_by_id(r"com.test.calc:id/multiply"),
                'POWER_BTN': self.driver.find_element_by_id(r"com.test.calc:id/power"),
                'RESULT': self.driver.find_element_by_id(r"com.test.calc:id/result")
                }.get(name, None)
