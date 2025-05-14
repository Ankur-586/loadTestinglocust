from locust import HttpUser, task, between

'''
https://crudcrud.com/api/27d9c052deec4a45b791cd5f88599b8c
'''
class CrudUsingLocust(HttpUser):
    
    wait_time = between(1, 5)
    host = 'https://crudcrud.com/api/27d9c052deec4a45b791cd5f88599b8c'
    created_post_id = None

    @task
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
            print(f"[GET] Fetched post ID {self.created_post_id}: {response.status_code}")
        else:
            print("[GET] No post ID available yet.")
    
    @task
    def update_post_data(self):
        if self.created_post_id:
            update_data = {
            "name":"Sparkle Angel", 
            "age":22, 
            "colour":"blue"
        }
            response = self.client.put(f"/resource/{self.created_post_id}", json=update_data)
            print(f"[PUT] Updated post ID {self.created_post_id}: {response.status_code}")
        else:
            print("[PUT] No post ID available yet.")

    @task
    def delete_post_data(self):
        if self.created_post_id:
            response = self.client.delete(f"/resource/{self.created_post_id}")
            print(f"[DELETE] Deleted post ID {self.created_post_id}: {response.status_code}")
            self.created_post_id = None  # reset after delete
        else:
            print("[DELETE] No post ID available yet.")
        
# locust -f main.py