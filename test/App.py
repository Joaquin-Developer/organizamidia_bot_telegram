import requests, json

def get_data():
    try:
        req = requests.get("http://127.0.0.1:5000/test_get_all_questions_by_topic_Geografia")
        print("Datos de la request:\n")
        print("Estado: {}\n".format(req.status_code))
        print("Headers: {}\n".format(req.headers))
        print("JSON: {}\n".format(req.json))
        print("Text: {}\n".format(req.text))

        data = json.loads(req.text)
        message = """Lista de tus tareas del día de hoy:\n\n"""

        for elem in data:
            message += (elem.get("question") + "\n\n")
        print(message)

    except Exception as e: print(e) 

if __name__ == "__main__": get_data()
