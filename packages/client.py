import requests


class Calculator:

    def __init__(self, base_url):
        self.base_url = base_url

    def create_request(self, num1, num2, action):
        data = {
            "left_operand": num1,
            "operation": action,
            "right_operand": num2
        }
        return data

    def send_request(self, data):
        result = requests.post(url=self.base_url, json=data)

        return result
