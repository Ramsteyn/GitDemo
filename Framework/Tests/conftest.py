import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as fs
from selenium.webdriver.firefox.options import Options as fo

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action= "store", default ="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        options = Options()
        options.add_experimental_option('detach', True)
        ser_obj = Service("Documents\\chromedriver.exe")
        driver = webdriver.Chrome(service=ser_obj, options=options)

    elif browser == "firefox":
        options = fo()
        #options.add_experimental_option('detach', True)
        ser_obj = fs("Documents\\geckodriver.exe")
        driver = webdriver.Firefox(service=ser_obj, options=options)

    elif browser == "IE":
        print("IE browser")

    driver.implicitly_wait(5)
    driver.get("https://www.amazon.com/")
    driver.maximize_window()

        # To pass the driver
        # request.cls.driver = driver
    request.cls.driver = driver
    #request.cls.get = get
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)


