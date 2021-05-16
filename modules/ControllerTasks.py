# -*- coding: utf-8 -*-
import requests, json, datetime
# from modules import Functions
from datetime import datetime

URL_API = "http://joaquindeveloper.pythonanywhere.com/"

def get_all_tasks_for_today(username):
    try:
        url = "{}/get_all_tasks_for_{}_from_{}".format(URL_API, get_actual_date(), username)
        resp = requests.get(url)
        data = json.loads(resp.text)
        if len(data) == 0:
            raise Exception("No se encontraron datos para el usuario indicado")

        dt = get_actual_date_for_user()
        tasks_text: str = ""
        
        for task in data:
            status = "Por Hacer" if task["status"] == 0 else "Finalizada"
            name = task.get("name")
            desc = task.get("description")
            tasks_text += ("**NOMBRE:** {}\n**Descripción:** {}\n**Estado:** {}\n\n".format(name, desc, status))

        return """Tareas del día {} del usuario {}\n\n{}\n\n**Organiza Mi Día - La App** """.format(dt, username, tasks_text)

    except Exception as e:
        print(e)
        raise e

def get_all_tasks_todo(username):
    pass

def get_all_task_for_this_week(username):
    pass

def get(username):
    pass

def get_actual_date():    
    return datetime.today().strftime('%Y-%m-%d')

def get_actual_date_for_user():
    dt = datetime.today().strftime('%Y-%m-%d').split("-")
    return "{}/{}/{}".format(dt[2], dt[1], dt[0])

# if __name__ == "__main__":
#     get_all_tasks_for_today("admin")
    