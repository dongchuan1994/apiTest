import pytest
from py._xmlgen import html
from datetime import datetime

# driver = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        # xfail = hasattr(report, 'wasxfail')
        # if (report.skipped and xfail) or (report.failed and not xfail):
        #     file_name = report.nodeid.replace("::", "_")+".png"
        #     screen_img = _capture_screenshot()
        #     if file_name:
        #         html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:900px;height:600px;" ' \
        #                'onclick="window.open(this.src)" align="right"/></div>' % screen_img
        #         extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")

# def _capture_screenshot():
#     return driver.get_screenshot_as_base64()

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(3, html.td(datetime.now(), class_='col-time'))