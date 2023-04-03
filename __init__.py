import requests

class CapSolver:
    def __init__(self, client_key):
        self.client_key = client_key
        self.base_url = "https://api.capsolver.com"
        
    def _make_request(self, endpoint, payload):
        response = requests.post(f"{self.base_url}/{endpoint}", json=payload)
        data = response.json()
        if data["errorId"] != 0:
            raise Exception(data["errorDescription"])
        return data
    
    def get_balance(self):
        return self._make_request("getBalance", {"clientKey": self.client_key})["balance"]
    
    def create_task(self, task_type, task_body, app_id=None, callback_url=None):
        payload = {"clientKey": self.client_key, "appId": app_id, "callbackUrl": callback_url, "task": {"type": task_type, "body": task_body}}
        return self._make_request("createTask", payload)["taskId"]
    
    def get_task_result(self, task_id):
        return self._make_request("getTaskResult", {"clientKey": self.client_key, "taskId": task_id})["solution"]
    
solver = CapSolver(client_key="CAI-A1CE97683E84CB481AB55C0E1F99322D")
balance = solver.get_balance()
print(f"Your balance is {balance}") 
