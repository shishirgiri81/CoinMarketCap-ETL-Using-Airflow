from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator



def greet(ti):
  first_name = ti.xcom_pull(task_ids = 'getName', key = 'first_name')
  middle_name = ti.xcom_pull(task_ids = 'getName', key = 'middle_name')
  last_name = ti.xcom_pull(task_ids = 'getName', key = 'last_name')
  age = ti.xcom_pull(task_ids = 'getAge', key = 'age')
  print(f"Hello, My name is {first_name} {middle_name} {last_name} and I am {age} years old.")


def getName(ti):
  ti.xcom_push(key = 'first_name', value = 'Shishir')
  ti.xcom_push(key = 'middle_name', value = 'Raj')
  ti.xcom_push(key = 'last_name', value = 'Giri')
  
def getAge(ti):
  ti.xcom_push(key = 'age', value = 23)


with DAG(

  default_args = {
    'owner' : 'Shishir',
    'retries' : 5,
    'retry_delay' : timedelta(minutes = 2)
  },

  dag_id = 'dag2_v7',
  description = 'Second DAG',
  start_date = datetime(2025, 3, 5),
  schedule_interval = '@daily'

) as dag:

  task1 = PythonOperator(
    task_id = 'greet',
    python_callable = greet
  )

  task2 = PythonOperator(
    task_id = 'getName',
    python_callable = getName
  )

  task3 = PythonOperator(
    task_id = 'getAge',
    python_callable = getAge
  )

  [task2, task3] >> task1