import re
from playwright.sync_api import Playwright, Page, sync_playwright, expect
from behave import given, then
from behave_django.decorators import fixtures
import time

BASE_URL = "http://localhost:8000"


@when("An external user navigates to the ONS website")
def external_user_navigates_to_homepage(context):
    # context.page.goto(
    #     BASE_URL
    # )  # You can uncomment this line if you want to see the expected behaviour by hitting the local server URL
    context.page.goto(context.base_url)  # This line will hit the django test client URL, you can comment this if using the above line


@then("they can see the title ONS Static Site Template")
def user_sees_the_homepage_hero_title(context):
    expect(
        context.page.get_by_role("heading", name="ONS Static Site Template")
    ).to_be_visible()


@then(
    "they can see the text Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare nisl ac dolor dapibus, non mattis sapien egestas."
)
def user_sees_the_homepage_hero_text(context):
    expect(
        context.page.get_by_text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare nisl"
        )
    ).to_be_visible()


@then("they click on the Cookies link")
def user_navigates_to_the_cookies_link(context):
    # context.page.goto(
    #     BASE_URL
    # )  # You can uncomment this line if you want to see the expected behaviour by hitting the local server URL
    context.page.goto(context.base_url)  # This line will hit the django test client URL, you can comment this if using the above line
    context.page.get_by_role("link", name="Cookies", exact=True).click()


@then("they can see the title Cookies on the cookies page")
def user_sees_the_cookie_page_title(context):
    expect(
        context.page.get_by_role("heading", name="Cookies on the static website")
    ).to_be_visible()
