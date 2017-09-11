from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
import click
import os
import test_restAPI
import test_Calculator

restAPI_tests = TestLoader().loadTestsFromTestCase(test_restAPI.TestRestAPI)
calculator_tests = TestLoader().loadTestsFromTestCase(test_Calculator.TestCalculatorApp)
suite = TestSuite([restAPI_tests, calculator_tests])
current_dir = os.getcwd()
runner = HTMLTestRunner(output=current_dir)


@click.group()
def cli():
    pass


@cli.command()
def run_all_tests():
    """This script runs all the tests."""
    runner.run(suite)
    click.echo('finished')


@cli.command()
def run_restapi_tests():
    """This script runs the RestAPI related tests."""
    runner.run(restAPI_tests)
    click.echo('finished')


@cli.command()
def run_calculator_tests():
    """This script runs the Calculator app related tests."""
    runner.run(calculator_tests)
    click.echo('finished')
