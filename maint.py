from locust import HttpUser, task, between, TaskSet

class CRUDSequence(TaskSet):
    
    def on_start(self):
        self.created_post_id = None
        self.create_post_data()
        
    def create_post_data(self):
        post_data = {
            "name":"Sparkle Angel", 
            "age":2, 
            "colour":"blue"
        }
        response = self.client.post("/resource", json = post_data)
        print(f"POST Response: {response.status_code}, {response.text}")
        if response.status_code == 201:
            self.created_post_id = response.json().get("_id")
            print(f"[POST] Created post ID: {self.created_post_id}")
        else:
            print(f"[POST] Failed with status: {response.status_code}")
            
    @task
    def get_post_data(self):
        if self.created_post_id:
            response = self.client.get(f"/resource/{self.created_post_id}")
            print(f"GET Response: {response.status_code}, {response.text}")
            print(f"[GET] Post ID: {self.created_post_id}")
            self.update_post_data()
        else:
            print("[GET] No ID")
            
    def update_post_data(self):
        if self.created_post_id:
            data = {
                "name":"Sparkle Angel", 
                "age":2, 
                "colour":"blue"
            }
            response = self.client.put(f"/resource/{self.created_post_id}", json=data)
            print(f"PUT Response: {response.status_code}, {response.text}")
            print(f"[PUT] Updated ID: {self.created_post_id}")
            self.delete_post_data()
            
    def delete_post_data(self):
        if self.created_post_id:
            self.client.delete(f"/resource/{self.created_post_id}")
            print(f"[DELETE] Deleted ID: {self.created_post_id}")
            self.created_post_id = None
            
class CRUDUser(HttpUser):
    wait_time = between(1, 5)
    host = "https://crudcrud.com/api/27d9c052deec4a45b791cd5f88599b8c"
    tasks = [CRUDSequence]