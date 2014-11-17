from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

firefox_path = '/opt/homebrew-cask/Caskroom/firefox/latest/Firefox.app/Contents/MacOS/firefox-bin'
binary = FirefoxBinary(firefox_path)

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(firefox_binary=binary)

test_url = 'http://jsfiddle.net/z9ssr05o/4/'
driver.get(test_url)
driver.switch_to.frame('result')

frames = driver.find_elements_by_xpath('//iframe')
frame = frames[1]
driver.switch_to.frame(frame)
print driver.find_element_by_id('test2').text
driver.quit()

# the page is ajaxy so the title is originally this:
# print driver.title

# find the element that's name attribute is q (the google search box)
# inputElement = driver.find_element_by_name("q")

# type in the search
# inputElement.send_keys("cheese!")

# submit the form (although google automatically searches now without submitting)
# inputElement.submit()

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    # WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    # print driver.title
    pass

finally:
    # driver.quit()
    pass