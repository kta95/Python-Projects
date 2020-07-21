from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
today = datetime.today()


def today_task(my_day='Today', day_=today.date()):
    row = session.query(Task).filter(Task.deadline == day_).all()
    print()
    print(f"{my_day} {day_.day} {day_.strftime('%b')}:")
    if len(row) == 0:
        print('Nothing to do!')
    else:
        for i in range(len(row)):
            count = str(i + 1)
            print(f'{count}. {row[i]}')


def add_task(new_task, date_):
    new_row = Task(task=new_task, deadline=datetime.strptime(date_, '%Y-%m-%d').date())
    session.add(new_row)
    session.commit()


def week_plan():
    day_week = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
                4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    day = today.weekday()
    for i in range(7):
        temp = i
        temp += day
        if temp > 6:
            temp = 0
        my_day = today + timedelta(days=i)
        today_task(day_week[temp], my_day.date())


def all_task():
    rows = session.query(Task).all()
    print('All tasks:')
    if len(rows) == 0:
        print('Nothing to do!')
    else:
        for row in rows:
            print(f'{row.id}. {row.task}')


def miss_task():
    print()
    print('Missed tasks:')
    result = session.query(Task).filter(Task.deadline < today.date()).order_by(Task.deadline).all()
    if len(result) == 0:
        print('Nothing is missed!')
    else:
        for i in range(len(result)):
            print(f"{i + 1}. {result[i]}. {result[i].deadline.day} {result[i].deadline.strftime('%b')}")


def delete_task():
    print()
    print('Chose the number of the task you want to delete:')
    result = session.query(Task).order_by(Task.deadline).all()
    if len(result) == 0:
        print('Nothing to delete!')
    else:
        for i in range(len(result)):
            print(f"{i + 1}. {result[i]}. {result[i].deadline.day} {result[i].deadline.strftime('%b')}")
        to_delete = int(input())
        specific_row = result[to_delete - 1]
        session.delete(specific_row)
        session.commit()
        print('The task has been deleted')


def start():
    while True:
        print()
        print("1) Today's tasks")
        print("2) Week's tasks")
        print("3) All tasks")
        print("4) Missed tasks")
        print("5) Add task")
        print("6) Delete task")
        print("0) Exit")
        action = int(input().strip())
        if action == 1:
            today_task()
        elif action == 2:
            week_plan()
        elif action == 3:
            all_task()
        elif action == 4:
            miss_task()
        elif action == 5:
            print()
            to_do = input('Enter task\n')
            deadline = input('Enter deadline\n')
            add_task(to_do, deadline)
            print('The task has been added!')
        elif action == 6:
            delete_task()
        elif action == 0:
            print('Bye!')
            exit()


start()
