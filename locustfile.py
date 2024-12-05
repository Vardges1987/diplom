from locust import HttpUser, between, task


class MyUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://127.0.0.1:8000"

    @task
    def register(self):
        self.client.post("/register", {
            "username": "testuser",
            "password": "testpassword123"
        })

    @task
    def login(self):
        self.client.post("/login", {
            "username": "testuser",
            "password": "testpassword123"
        })
