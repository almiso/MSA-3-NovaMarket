from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    # Wait time between requests from a single user
    wait_time = between(1, 5)

    @task
    def index(self):
        # Generate a GET request to the root path
        self.client.get("/")
