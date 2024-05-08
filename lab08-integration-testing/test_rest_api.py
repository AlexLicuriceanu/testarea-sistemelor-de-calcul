import requests
import uuid

ENDPOINT = 'https://todo.pixegami.io/'

# Task 1.
def test_create_task():
    payload = create_payload()

    create_task_response = requests.put(ENDPOINT + '/create-task', json=payload)
    assert create_task_response.status_code == 200

    create_task_data = create_task_response.json()
    task_id = create_task_data['task']['task_id']

    get_task_response = requests.get(ENDPOINT + f'/get-task/{task_id}')
    assert get_task_response.status_code == 200

    get_task_data = get_task_response.json()

    assert get_task_data['content'] == payload['content']
    assert get_task_data['user_id'] == payload['user_id']
    assert get_task_data['is_done'] == payload['is_done']

    
# Task 2.
def test_update_task():
    payload = create_payload()
    
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200

    task_id = create_task_response.json()['task']['task_id']

    new_payload = {
        'user_id': payload['user_id'],
        'task_id': task_id,
        'content': 'Updated test task',
        'is_done': True
    }

    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200


    get_task_response = requests.get(ENDPOINT + f'/get-task/{task_id}')
    assert get_task_response.status_code == 200

    get_task_data = get_task_response.json()
    assert get_task_data['content'] == new_payload['content']
    assert get_task_data['user_id'] == new_payload['user_id']
    assert get_task_data['is_done'] == new_payload['is_done']


# Task 3.
def test_list_tasks():
    nr_tasks = 3
    payload = create_payload()

    for i in range(nr_tasks):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    user_id = payload['user_id']
    list_tasks_response = list_tasks(user_id)

    assert list_tasks_response.status_code == 200

    data = list_tasks_response.json()
    tasks = data['tasks']

    assert len(tasks) == nr_tasks

# Task 4.
def test_delete_task():
    payload = create_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200

    task_id = create_task_response.json()['task']['task_id']

    delete_task_response = requests.delete(ENDPOINT + f'/delete-task/{task_id}')
    assert delete_task_response.status_code == 200

    get_task_response = requests.get(ENDPOINT + f'/get-task/{task_id}')
    assert get_task_response.status_code == 404


def get_task(task_id):
    return requests.get(ENDPOINT + f'/get-task/{task_id}')

def list_tasks(user_id):
    return requests.get(ENDPOINT + f'/list-tasks/{user_id}')

def create_task(payload):
    return requests.put(ENDPOINT + '/create-task', json=payload)

def update_task(payload):
    return requests.put(ENDPOINT + '/update-task', json=payload)

def create_payload():
    user_id = f'test_user_{uuid.uuid4().hex}'
    content = f'test_content_{uuid.uuid4().hex}'

    return {
        'content': content,
        'user_id': user_id,
        'is_done': False
    }