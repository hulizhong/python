#!/usr/bin/env python
# coding=utf-8
import psycopg2
import threading

class PgClient(object):
    """
    postgres db client
    make sure python-psycopg2 has been installed by apt-get.
    """
    def __init__(self):
        try:
            dbuser = 'spe'
            dbpasswd = 'spe'
            db = 'spe_db'
            dbhost = '127.0.0.1'
            dbport = 5432
            self.conn = psycopg2.connect(database=db, user=dbuser, password=dbpasswd, host=dbhost, port=dbport)
            self.cursor = self.conn.cursor()
            #print('connect pg succeed')
        except Exception,e:
            #traceback.print_exc()
            print 'PgClient init error, cause: ', e

    def __del__(self):
        self.conn.close()
        #print 'close connection to pg'

    def exc(self, sql, isCommit=True):
        try:
            self.cursor.execute(sql)
        except Exception, e:
            print "execute sql failed cause:", e
            raise e
        else:
            if isCommit:
                self.conn.commit()

    def cancelExe(self):
        """
        rollback since last commit()
        """
        self.conn.rollback()

    def query(self, sql):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

def fun1(id):
    steps = int(id)
    for i in range(steps):
        cc = PgClient()
        data = id
        sql = "update t_transaction set c_data = '" + data + "' where c_id = 2"
        cc.exc(sql)
        sql = "update t_transaction set c_data = '" + data + "' where c_id = 1"
        cc.exc(sql)

def fun2(id):
    steps = int(id)
    for i in range(steps):
        cc = PgClient()
        data = id
        sql = "update t_transaction set c_data = '" + data + "' where c_id = 3"
        cc.exc(sql)
        sql = "update t_transaction set c_data = '" + data + "' where c_id = 2"
        cc.exc(sql)

def fun3(id):
    steps = int(id)
    for i in range(steps):
        cc = PgClient()
        data = id
        sql = "update t_transaction set c_data = '" + data + "' where c_id = 4"
        cc.exc(sql)
        sql = "update t_transaction set c_data = '" + data + "' where c_id = 3"
        cc.exc(sql)

ts = []
t1 = threading.Thread(target=fun1, args=('10000',))
ts.append(t1)
t2 = threading.Thread(target=fun2, args=('20000',))
ts.append(t2)
t3 = threading.Thread(target=fun2, args=('30000',))
ts.append(t3)
for t in ts:
    t.setDaemon(True)
    t.start()
t.join()


'''
sql = 'select * from t_transaction'
rows = cc.query(sql)
for row in rows:
    print row
'''

