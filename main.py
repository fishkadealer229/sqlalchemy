import datetime
from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = 'Scott'
    user.name = "Ridley"
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = 'Billy'
    user.name = "Herringtone"
    user.age = 43
    user.position = 'master'
    user.speciality = 'cleaning'
    user.address = 'dungeon'
    user.email = "billy_herringtone@gacha.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = 'Gafarov'
    user.name = "Vadim"
    user.age = 18
    user.position = 'mayor'
    user.speciality = 'programmer'
    user.address = 'Enginerring'
    user.email = "midav.06@mail.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    jobs = Jobs()
    jobs.team_leader = 1
    jobs.job = 'deployment of residential modules 1 and 2'
    jobs.work_size = 15
    jobs.collaborators = '2, 3'
    jobs.start_date = datetime.datetime.now()
    jobs.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()
