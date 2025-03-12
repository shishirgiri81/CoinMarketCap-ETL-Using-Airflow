from datetime import datetime, timedelta

from airflow import DAG

from airflow.operators.bash import BashOperator





with DAG(

  default_args = {
    'owner': 'Shishir',
    'retries': 5,
    'retry_delay': timedelta(minutes = 2)
  },

  dag_id = 'dag1_v5',
  description = 'My first DAG',
  start_date = datetime(2025, 3, 5),
  schedule_interval = '@daily'

) as dag:

  task1 = BashOperator(
    task_id = 'first_task',
    bash_command = 'echo Hello World!!'
  )

  task2 = BashOperator(
    task_id = 'second_task',
    bash_command = 'echo Second Task'
  )

  task3 = BashOperator(
    task_id = 'third_task',
    bash_command = 'echo Third Task!'
  )

  # Task Dependency Method 1
  # task1.set_downstream(task2)
  # task1.set_downstream(task3)


  # Task Dependency Method 2
  # task1 >> task2
  # task1 >> task3

  # Task Dependency Method 3
  task1 >> [task2, task3]



