import requests
import time

MAX_RETRIES = 10

def check_selenium_grid_health():
    hub_url = "http://localhost:4444/status"
    retry_count = 0  
    while retry_count < MAX_RETRIES:
        try:
            response = requests.get(hub_url)
            if response.status_code == 200:
                status = response.json()['value']['ready']
                if status:
                    print("Selenium Grid is ready!")
                    break
                else:
                    print("Selenium Grid is not ready yet. Retrying...")
            else:
                print(f"Received status code {response.status_code}. Retrying...")
        except requests.ConnectionError:
            print("Selenium Grid is not available. Retrying...")
        time.sleep(2)
        retry_count += 1  
if __name__ == "__main__":
    check_selenium_grid_health()

