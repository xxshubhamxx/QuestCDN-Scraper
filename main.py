from flask import Flask, request, render_template
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import concurrent.futures
import time

url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"

q_num = []

options = Options()
options.headless = True  # Set to False if you want to see the browser
app = Flask(__name__)

# Default arguments
default_group = '1950787'
default_provider = '1950787'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', default_group=default_group, default_provider=default_provider)


# Function 1
def function_one():
    print("Function 1 started")
    driver1 = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    driver1.get(url)
    driver1.implicitly_wait(3)

    if len(q_num) > 0:
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
    else:
        driver1.quit()
        return 0

# Function 2
def function_two():
    print("Function 2 started")
    driver2 = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    driver2.get(url)
    driver2.implicitly_wait(3)

    if len(q_num) > 1:
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
    else:
        driver2.quit()
        return 0

# Function 3
def function_three():
    print("Function 3 started")
    driver3 = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    driver3.get(url)
    driver3.implicitly_wait(3)

    if len(q_num) > 2:
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
    else:
        driver3.quit()
        return 0

# Function 4
def function_four():
    print("Function 4 started")
    driver4 = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    driver4.get(url)
    driver4.implicitly_wait(3)

    if len(q_num) > 3:
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
    else:
        driver4.quit()
        return 0

# Function 5
def function_five():
    print("Function 5 started")
    driver5 = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    driver5.get(url)
    driver5.implicitly_wait(3)

    if len(q_num) > 4:
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
    else:
        driver5.quit()
        return 0

def find_postings():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(function_one)
        f2 = executor.submit(function_two)
        f3 = executor.submit(function_three)
        f4 = executor.submit(function_four)
        f5 = executor.submit(function_five)
        
        postings = [f1.result(), f2.result(), f3.result(), f4.result(), f5.result()]
        return postings

@app.route('/scrape', methods=['GET'])
def scrape_data():
    
    group = request.args.get('group', default=default_group)
    provider = request.args.get('provider', default=default_provider)

    options = Options()
    options.headless = True  # Set to False to see the browser

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

    url = f"https://qcpi.questcdn.com/cdn/posting/?group={group}&provider={provider}"
    driver.get(url)

    driver.implicitly_wait(5)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', {'id': 'table_id'})
    postings = []

    if table:
        rows = table.find_all('tr')
        for q in rows:
            cells = q.find_all('td')
            if len(cells) >= 11 and len(q_num) < 5:
                q_num.append(cells[1].text.strip())
        print(q_num)
        
    driver.quit()

    return render_template('result.html', postings=find_postings())

if __name__ == '__main__':
    app.run(debug=True)
