# business layer

def get_data(todo_data):
    data = []
    for i in todo_data:
        data.append({"id": i.id, "title": i.title, "status": i.status})
    return data
