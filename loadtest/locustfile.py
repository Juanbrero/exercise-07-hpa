# TODO: Locust load test
# from locust import HttpUser, task
# Hit /health and /api/nodes endpoints

from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def health(self):
        self.client.get("/health")

    @task
    def nodes(self):
        self.client.get("/api/nodes")

