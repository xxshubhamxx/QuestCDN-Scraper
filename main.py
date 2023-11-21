from flask import Flask, request, render_template
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)

# Default arguments
default_group = '1950787'
default_provider = '1950787'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', default_group=default_group, default_provider=default_provider)

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
        q_num = []
        for q in rows:
            cells = q.find_all('td')
            if len(cells) >= 11 and len(q_num) <= 5:
                q_num.append(cells[1].text.strip())
        print(q_num)
        postings = []
        for i in range(len(q_num)):
            
            # driver.refresh()
            driver.implicitly_wait(5)
                    
            js_function_call = f"prevnext({q_num[i]})"
            driver.execute_script(js_function_call)
                    
            
            description_cell = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[3]/div/table/tbody/tr[3]/td[2]")
            description = description_cell.get_attribute('innerHTML').strip()

            est_value_cell = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[3]/td[2]")
            est_value = est_value_cell.get_attribute('innerHTML').strip()

            closing_date_cell = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[2]")
            closing_date = closing_date_cell.get_attribute('innerHTML').strip()

            posting = {
                'Quest Number': q_num[i-1],
                'Description': description,
                'Est Value': est_value,
                'Closing Date': closing_date
            }
            
            if len(postings) <= 5:
                postings.append(posting)
            else:
                print("Breaking due to else")
                break
            try:
                wait = WebDriverWait(driver, 10)
                WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "//div[@id='preloader'][@ng-show='loading']")))
                next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='id_prevnext_next']")))
                next_button.click()
                driver.implicitly_wait(5)
            except:
                print("Breaking due to except")
                break
            
        if len(postings) <= 5:
            print("Failed to extract the required number of postings")
        else:
            print("Scraping successful")
    postings = postings[1:]

    driver.quit()

    return render_template('result.html', postings=postings)

if __name__ == '__main__':
    app.run(debug=True)
