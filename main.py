from locust import HttpUser, task, between

'''
https://jsonplaceholder.typicode.com/posts
'''
class CrudUsingLocust(HttpUser):
    
    wait_time = between(1, 5)
    host = 'https://jsonplaceholder.typicode.com'
    created_post_id = None

    @task
    def create_post_data(self):
        post_data = {
            'title': 'test post',
            'body': 'This is my 1st test post',
            'userId': 1,
        }
        response = self.client.post("/posts", json = post_data)
        print(f"POST Response: {response.status_code}, {response.text}")
        if response.status_code == 201:
            self.created_post_id = response.json().get("id")
            print(f"[POST] Created post ID: {self.created_post_id}")
        else:
            print(f"[POST] Failed with status: {response.status_code}")
    
    @task
    def get_post_data(self):
        if self.created_post_id:
            response = self.client.get(f"/posts/{self.created_post_id}")
            print(f"[GET] Fetched post ID {self.created_post_id}: {response.status_code}")
        else:
            print("[GET] No post ID available yet.")
    
    @task
    def update_post_data(self):
        if self.created_post_id:
            update_data = {
                'title': 'Updated title',
                'body': 'Updated post content',
                'userId': 1,
            }
            response = self.client.put(f"/posts/{self.created_post_id}", json=update_data)
            print(f"[PUT] Updated post ID {self.created_post_id}: {response.status_code}")
        else:
            print("[PUT] No post ID available yet.")

    @task
    def delete_post_data(self):
        if self.created_post_id:
            response = self.client.delete(f"/posts/{self.created_post_id}")
            print(f"[DELETE] Deleted post ID {self.created_post_id}: {response.status_code}")
            self.created_post_id = None  # reset after delete
        else:
            print("[DELETE] No post ID available yet.")
    
    # @task
    # def update_post_data(self):
    #     update_data = {
    #         'title': 'update test post',
    #         'body': 'update This is my 1st test post',
    #         'userId': 10,
    #     }
    #     id = 101
    #     response = self.client.put(f"/posts/{id}", json = update_data)
    #     print(f"PUT Response: {response.status_code}, {response.text}")
    
    # @task
    # def delete_post_data(self):
    #     id = 101
    #     response = self.client.delete(f"/posts/{id}")
    #     print(f"DELETE Response: {response.status_code}, {response.text}")
        
# locust -f main.py