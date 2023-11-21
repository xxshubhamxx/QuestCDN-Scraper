import concurrent.futures
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your GeckoDriver executable
gecko_driver_path = '../geckodriver.exe'

options = Options()
options.headless = True  # Set to False if you want to see the browser

# Set the Firefox WebDriver with the specified options
driver = webdriver.Firefox(executable_path=gecko_driver_path, options=options)

url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"
driver.get(url)

# Get the page source after waiting for a few seconds (adjust the time as needed)
driver.implicitly_wait(3)
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', {'id': 'table_id'})
postings = []

if table:
    rows = table.find_all('tr')
    q_num = []
    for q in rows:
        cells = q.find_all('td')
        if len(cells) >= 11 and len(q_num) < 5:
            q_num.append(cells[1].text.strip())
    print(q_num)

# Function 1
def function_one():
    print("Function 1 started")
    driver1 = webdriver.Firefox(executable_path=gecko_driver_path, options=options)
    driver1.get(url)
    driver1.implicitly_wait(3)

    js_function_call = f"prevnext({q_num[0]})"
    driver1.execute_script(js_function_call)
    driver1.implicitly_wait(3)
    
    description_cell = driver1.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[3]/div/table/tbody/tr[3]/td[2]")
    description = description_cell.get_attribute('innerHTML').strip()

    est_value_cell = driver1.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[3]/td[2]")
    est_value = est_value_cell.get_attribute('innerHTML').strip()

    closing_date_cell = driver1.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[2]")
    closing_date = closing_date_cell.get_attribute('innerHTML').strip()

    posting = {
        'Quest Number': q_num[0],
        'Description': description,
        'Est Value': est_value,
        'Closing Date': closing_date
    }
    driver1.quit()
    return posting

# Function 2
def function_two():
    print("Function 2 started")
    driver2 = webdriver.Firefox(executable_path=gecko_driver_path, options=options)
    driver2.get(url)
    driver2.implicitly_wait(3)

    js_function_call = f"prevnext({q_num[1]})"
    driver2.execute_script(js_function_call)
    driver2.implicitly_wait(3)
    
    description_cell = driver2.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[3]/div/table/tbody/tr[3]/td[2]")
    description = description_cell.get_attribute('innerHTML').strip()

    est_value_cell = driver2.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[3]/td[2]")
    est_value = est_value_cell.get_attribute('innerHTML').strip()

    closing_date_cell = driver2.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[2]")
    closing_date = closing_date_cell.get_attribute('innerHTML').strip()

    posting = {
        'Quest Number': q_num[1],
        'Description': description,
        'Est Value': est_value,
        'Closing Date': closing_date
    }
    driver2.quit()
    
    return posting

# Function 3
def function_three():
    print("Function 3 started")
    driver3 = webdriver.Firefox(executable_path=gecko_driver_path, options=options)
    driver3.get(url)
    driver3.implicitly_wait(3)

    js_function_call = f"prevnext({q_num[2]})"
    driver3.execute_script(js_function_call)
    driver3.implicitly_wait(3)
    
    description_cell = driver3.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[3]/div/table/tbody/tr[3]/td[2]")
    description = description_cell.get_attribute('innerHTML').strip()

    est_value_cell = driver3.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[3]/td[2]")
    est_value = est_value_cell.get_attribute('innerHTML').strip()

    closing_date_cell = driver3.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[2]")
    closing_date = closing_date_cell.get_attribute('innerHTML').strip()

    posting = {
        'Quest Number': q_num[2],
        'Description': description,
        'Est Value': est_value,
        'Closing Date': closing_date
    }
    driver3.quit()
    
    return posting

# Function 4
def function_four():
    print("Function 4 started")
    driver4 = webdriver.Firefox(executable_path=gecko_driver_path, options=options)
    driver4.get(url)
    driver4.implicitly_wait(3)

    js_function_call = f"prevnext({q_num[3]})"
    driver4.execute_script(js_function_call)
    driver4.implicitly_wait(3)
    
    description_cell = driver4.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[3]/div/table/tbody/tr[3]/td[2]")
    description = description_cell.get_attribute('innerHTML').strip()

    est_value_cell = driver4.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[3]/td[2]")
    est_value = est_value_cell.get_attribute('innerHTML').strip()

    closing_date_cell = driver4.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[2]")
    closing_date = closing_date_cell.get_attribute('innerHTML').strip()

    posting = {
        'Quest Number': q_num[3],
        'Description': description,
        'Est Value': est_value,
        'Closing Date': closing_date
    }
    driver4.quit()
    
    return posting

# Function 5
def function_five():
    print("Function 5 started")
    driver5 = webdriver.Firefox(executable_path=gecko_driver_path, options=options)
    driver5.get(url)
    driver5.implicitly_wait(3)

    js_function_call = f"prevnext({q_num[4]})"
    driver5.execute_script(js_function_call)
    driver5.implicitly_wait(3)
    
    description_cell = driver5.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[3]/div/table/tbody/tr[3]/td[2]")
    description = description_cell.get_attribute('innerHTML').strip()

    est_value_cell = driver5.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[3]/td[2]")
    est_value = est_value_cell.get_attribute('innerHTML').strip()

    closing_date_cell = driver5.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[2]")
    closing_date = closing_date_cell.get_attribute('innerHTML').strip()

    posting = {
        'Quest Number': q_num[4],
        'Description': description,
        'Est Value': est_value,
        'Closing Date': closing_date
    }
    driver5.quit()
    
    return posting

def run_parallel_functions():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit functions to the executor
        future_one = executor.submit(function_one)
        future_two = executor.submit(function_two)
        future_three = executor.submit(function_three)
        future_four = executor.submit(function_four)
        future_five = executor.submit(function_five)

        # Gather the results
        results = [future_one.result(), future_two.result(), future_three.result(), future_four.result(), future_five.result()]

        # Wait for all functions to complete
        concurrent.futures.wait([future_one, future_two, future_three])

    # Printing or using the results
    print(results)

if __name__ == "__main__":
    run_parallel_functions()
