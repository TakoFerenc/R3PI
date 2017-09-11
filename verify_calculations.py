import math
import test_Calculator
from app_locators import AppLocators


class VerifyCalculations:

    def __init__(self):
        self.driver = test_Calculator.TestCalculatorApp.pass_driver()
        self.applocators = AppLocators()
        self.element = self.applocators.locator

    def get_current_result(self):
        # This function returns the current result displayed in the app
        self.raw_text = self.element('RESULT').get_attribute('text')
        self.string_result = self.raw_text[8:]
        if self.string_result == '':
            self.current_result = 0
        else:
            self.current_result = float(self.string_result)
        return self.current_result

    def tap_the_button(self, locator, times):
        # This function taps 'times' a button 'locator'
        self.times = times
        for tap in range(times):
            locator.click()

    def add_one(self):
        # This function calculates and returns the expected result for add
        return self.current_result + 1 * self.times

    def subtract_one(self):
        # This function calculates and returns the expected result for subtract
        return self.current_result - 1 * self.times

    def square_root(self):
        # This function calculates and returns the expected result for square root
        result = math.sqrt(self.current_result)
        if self.times == 1:
            return result
        else:
            for item in range(self.times - 1):
                result = math.sqrt(result)
            return result

    def devide_by_two(self):
        # This function calculates and returns the expected result for divide
        result = self.current_result / 2
        if self.times == 1:
            return result
        else:
            for item in range(self.times - 1):
                result = result / 2
            return result

    def multiply_by_two(self):
        # This function calculates and returns the expected result for multiply
        result = self.current_result * 2
        if self.times == 1:
            return result
        else:
            for item in range(self.times - 1):
                result = result * 2
            return result

    def power_by_two(self):
        # This function calculates and returns the expected result for power
        result = self.current_result * self.current_result
        if self.times == 1:
            return result
        else:
            for item in range(self.times - 1):
                result = result * result
            return result
