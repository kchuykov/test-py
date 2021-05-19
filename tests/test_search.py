"""
These tests cover Yahoo page.
"""


def test_print_links(browser):
    browser.get('https://yahoo.com/')
    browser.find_element_by_link_text('More...')
    links = browser.find_elements_by_css_selector('#ybar-navigation a')
    for link in links:
        print(link.text)
    assert False
