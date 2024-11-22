from playwright.sync_api import sync_playwright
from django.core.management import call_command
import os


def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False, slow_mo=2000)


def before_scenario(context, scenario):
    # call_command("flush", verbosity=0, interactive=False)
    context.page = context.browser.new_page()
    # Load the fixture before each scenario
    # fixture_path = os.path.join(os.path.dirname(__file__), "homepage_fixture.json")
    # try:
    #     call_command("loaddata", fixture_path)
    # except Exception as e:
    #     print(f"Error loading fixture: {e}")


def after_scenario(context, scenario):
    # call_command("flush", "--no-input")
    context.page.close()


def after_all(context):
    context.browser.close()
    context.playwright.stop()
