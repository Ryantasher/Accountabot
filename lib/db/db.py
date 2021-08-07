from os.path import isfile
from sqlite3 import connect #sql db handler
from apscheduler.triggers.cron import CronTrigger #used to create timed db events


DB_PATH = "./data/db/database.db" #path to the database
BUILD_PATH = "./data/db/build.sql" #path to the database buildfile

#check_same_thread may need to be updated, for now just stops some errors
cxn = connect(DB_PATH, check_same_thread=False) #object that represents the DB itself
cur = cxn.cursor() #cursor allows for SQL commands

def with_commit(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        commit()
    return inner

#call script 
@with_commit
def build():
    if isfile(BUILD_PATH):
        scriptexec(BUILD_PATH)

def commit():
    cxn.commit()

def autosave(sched):
    sched.add_job(commit, CronTrigger(second=0))
    
def close():
    cxn.close()

def field(command, *values):
    cur.execute(command, tuple(values))

    if (fetch := cur.fetchone()) is not None:
        return fetch[0]

def record(command, *values):
    cur.execute(command, tuple(values))

    return cur.fetchone()

def records(command, *values):
    cur.execute(command, tuple(values))

    return cur.fetchall()

def column(command, *values):
    cur.execute(command, tuple(values))

    return [item[0] for item in cur.fetchall()]

#used to modify the database
def execute(command, *values):
    cur.execute(command, tuple(values))

def multiexec(command, valueset):
    cur.executemany(command, valueset)

#reads build path, issues commit, and executes build path within sql
def scriptexec(path):
    with open(path, "r", encoding="utf-8") as script:
        cur.executescript(script.read())
        
