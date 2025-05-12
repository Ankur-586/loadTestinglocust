from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    
    wait_time = between(1, 5) 
    
    # @task
    # def home_page(self):
    #     url = "/health"
    #     full_url = self.client.base_url + url
    #     self.client.get(url)
    
    @task
    def api_gateway(self):
        # url = "/store/product/list"
        url = "/store/products"
        full_url = self.client.base_url + url
        print(full_url)
        self.client.get(url)
        
    # @task
    # def about_us(self):
    #     self.client.get("/aboutus", name="About Us")