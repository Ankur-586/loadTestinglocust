from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    
    wait_time = between(1, 5) 
    host = 'https://demo.nourishstore.in'
    
    @task
    def home_page(self):
        url = "/"
        full_url = self.client.base_url + url
        self.client.get(url)
    
    @task
    def store_products(self):
        # url = "/store/product/list"
        url = "/aboutus"
        full_url = self.client.base_url + url
        print(full_url)
        self.client.get(url)
    
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
    Flag	      Meaning
--headless	      Runs Locust without the web UI — purely from the terminal.
-u 10	          Spawns 10 total users (virtual users or VUs).
-r 2	          Spawn rate: 2 users per second until it reaches 10 users.
-t 1m	          Test duration: 1 minute.
--loglevel        INFO	Sets the logging level to INFO (can also be DEBUG, WARNING, etc).
--logfile         locust.log Saves all logs to the file locust.log.
'''