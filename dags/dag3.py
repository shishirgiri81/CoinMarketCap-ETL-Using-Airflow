from datetime import datetime, timedelta

from airflow.decorators import dag, task


@dag(
  
  default_args = {
    'owner' : 'Shishir',
    'retries' : 5,
    'retry_delay' : timedelta(minutes = 2)
  },

  dag_id = 'dag3',
  start_date = datetime(2025, 3, 7),
  schedule_interval = '@daily'

)
def hello_world():

  @task(multiple_outputs = True)
  def getName():
    return {
      'firstName' : 'Shishir',
      'middleName' : 'Raj',
      'lastName' : 'Giri'
    }

  @task()
  def getAge():
    return 23

  @task()
  def greet(firstName, middleName, lastName, age):
    print(f"Hello, My name is {firstName} {middleName} {lastName} and I am {age} years old.")

  nameDict = getName()
  age = getAge()

  greet(firstName = nameDict['firstName'],
        middleName = nameDict['middleName'],
        lastName = nameDict['lastName'],
        age = age)


hello_world()
