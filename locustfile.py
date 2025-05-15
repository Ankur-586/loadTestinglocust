from locust import HttpUser, task, between
from requests.exceptions import RequestException

class WebsiteUser(HttpUser):
    
    wait_time = between(1, 5) 
    # host = 'https://demo.nourishstore.in/'
    host = 'https://api-dev.nourishstore.in/api'
    
    @task
    def home_page(self):
        url = "/store/products/prod_01JDS0Z98MQTWS9T61CK7QJCMY"
        full_url = self.client.base_url + url
        self.client.get(url)
    
    # @task
    # def store_products(self):
    #     # url = "/store/product/list"
    #     url = "/aboutus"
    #     full_url = self.client.base_url + url
    #     print(full_url)
    #     self.client.get(url)
    
    # @task
    # def api_store_products(self):
    #     url = "/store/product/list"
    #     # url = "/store/products"
    #     full_url = self.client.base_url + url
    #     print(full_url)
    #     self.client.get(url)
    
    # @task
    # def about_us(self):
    #     self.client.get("/aboutus", name="About Us")
    
# locust --headless -u 10 -r 2 -t 1m --loglevel INFO --logfile locust.log

'''
api-dev.nourishstore.in/api/store/products/prod_01JDS0Z98MQTWS9T61CK7QJCMY

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def home_page(self):
        url = "/"
        try:
            response = self.client.get(url, timeout=10)
            # Optionally check status
            if response.status_code == 200:
                print("Homepage loaded successfully")
            else:
                print(f"Homepage returned status code: {response.status_code}")
        except RequestException as e:
            print(f"Request failed: {e}")

    Flag	      Meaning
--headless	      Runs Locust without the web UI — purely from the terminal.
-u 10	          Spawns 10 total users (virtual users or VUs).
-r 2	          Spawn rate: 2 users per second until it reaches 10 users.
-t 1m	          Test duration: 1 minute.
--loglevel        INFO	Sets the logging level to INFO (can also be DEBUG, WARNING, etc).
--logfile         locust.log Saves all logs to the file locust.log.
'''