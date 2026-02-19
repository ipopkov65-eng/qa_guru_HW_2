import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()

    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


@pytest.mark.google
def test_google_open(driver):
    url = "https://www.google.com/"
    driver.get(url)
    assert "Google" in driver.title
    assert "google.com" in driver.current_url


@pytest.mark.github
def test_github_open(driver):
    url = "https://github.com/"
    driver.get(url)
    assert "GitHub" in driver.title
    assert "github.com" in driver.current_url
