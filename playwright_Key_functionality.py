from playwright.sync_api import sync_playwright

browser = sync_playwright().start().chromium.launch(headless=False)
page = browser.new_page()

#Navigation
page.goto("https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671")
page.screenshot(path="accuweather.png")

'''
#clicking
page.click("text=Hourly")
page.screenshot(path="full_forecast.png")
'''
''''
#typing
page.fill("input[name='q']", "Playwright")
page.press("input[name='q']", "Enter")
page.screenshot(path="search_results.png")

#waiting for elements
page.wait_for_selector("text=Playwright: Fast and reliable end-to-end testing for modern web apps")
page.screenshot(path="search_results_loaded.png")
'''

#Extracting the data
title = page.title()
print(f"Page title: {title}")
#browser.close()