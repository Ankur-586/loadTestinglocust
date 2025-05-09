from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    
    wait_time = between(1, 5) 
    
    @task
    def home_page(self):
        self.client.get("/health", name="Home Page")
    
    # @task
    # def grocery_page(self):
    #     self.client.get("/grocery", name="Grocery Page")
        
    # @task
    # def about_us(self):
    #     self.client.get("/aboutus", name="About Us")