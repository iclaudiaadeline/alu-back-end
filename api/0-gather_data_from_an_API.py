import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)
    
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Invalid employee ID")
        return
    
    user_data = user_response.json()
    todos_data = todos_response.json()
    
    employee_name = user_data.get("name")
    completed_tasks = [task["title"] for task in todos_data if task["completed"]]
    total_tasks = len(todos_data)
    done_tasks = len(completed_tasks)
    
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        get_employee_todo_progress(int(sys.argv[1]))

