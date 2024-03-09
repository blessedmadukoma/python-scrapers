# Question: Find and report the largest contentful paint of the webpage and the duration in seconds.

"""
 NOTE: CHANGE THE DIRECTORY OF YOUR SELENIUM DRIVER LOCATION ON YOUR LAPTOP
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def measure_lcp(url):
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # To run Chrome in headless mode
    chrome_driver_path = '/path/to/chromedriver'  # Update this path with the actual path to your ChromeDriver

    # Initialize the Chrome webdriver with the configured options
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigate to the webpage
    driver.get(url)

    # Wait for LCP metric to be available
    lcp = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'largest-contentful-paint'))
    )

    # Extract the LCP value
    lcp_value = lcp.get_attribute('textContent')

    # Report the LCP value
    print(f"Largest Contentful Paint (LCP): {lcp_value}")

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    url = input("Enter URL:")
    measure_lcp(url)
