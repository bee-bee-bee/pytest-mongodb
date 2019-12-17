#!/usr/bin/env python
# coding=utf-8
import sys
import traceback
import pymongo


class MongodbManager(object):
    def __init__(self, **kwargs):
        try:
            self.conn = pymongo.MongoClient(kwargs['host'], kwargs['port'])
            self.db = self.conn[kwargs['database']]  # connect db
            self.username = kwargs['username']
            self.password = kwargs['password']
            if self.username and self.password:
                self.connected = self.db.authenticate(self.username, self.password)
            else:
                self.connected = True
        except ConnectionError:
            print(traceback.format_exc())
            print('Connect Statics Database Fail.')
            sys.exit(1)

    def close(self):
        self.conn.close()

    def check_connected(self):
        # 检查是否连接成功
        if not self.connected:
            raise (NameError, 'stat:connected Error')

    def save(self, collection, value):
        # 一次操作一条记录，根据‘_id’是否存在，决定插入或更新记录
        try:
            self.check_connected()
            self.db[collection].save(value)
        except Exception:
            print(traceback.format_exc())
        finally:
            self.close()

    def insert(self, collection, value):
        # 可以使用insert直接一次性向mongoDB插入整个列表，也可以插入单条记录，但是'_id'重复会报错
        try:
            self.check_connected()
            self.db[collection].insert(value, continue_on_error=True)
        except Exception:
            print(traceback.format_exc())
        finally:
            self.close()

    def insert_many(self, data):
        """
        批量插入数据
        :param collection:
        :param data:
        :return:
        """
        try:
            if self.get_state():
                result = self.db[self.collection].insert_many(data)
                return result.inserted_id
            else:
                return self.get_state()
        except Exception as e:
            print("Mongodb Error: %s" % (e,))

    def update(self, collection, conditions, value, s_upsert=False, s_multi=False):
        try:
            self.check_connected()
            self.db[collection].update(conditions, {'$set': value}, upsert=s_upsert, multi=s_multi)
        except Exception:
            print(traceback.format_exc())
        finally:
            self.close()

    def upsert_many(self, collection, many_data):
        # 批量更新插入，根据‘_id’更新或插入多条记录。
        # 把'_id'值不存在的记录，插入数据库。'_id'值存在，则更新记录。
        # 如果更新的字段在mongo中不存在，则直接新增一个字段
        try:
            self.check_connected()
            bulk = self.db[collection].initialize_ordered_bulk_op()
            for data in many_data:
                _id = data['_id']
                bulk.find({'_id': _id}).upsert().update({'$set': data})
            bulk.execute()
        except Exception:
            print(traceback.format_exc())
        finally:
            self.close()

    def upsert_one(self, collection, data):
        # 更新插入，根据‘_id’更新一条记录，如果‘_id’的值不存在，则插入一条记录
        try:
            self.check_connected()
            query = {'_id': data.get('_id', '')}
            if not self.db[collection].find_one(query):
                self.db[collection].insert(data)
            else:
                data.pop('_id')  # 删除'_id'键
                self.db[collection].update(query, {'$set': data})
        except Exception:
            print(traceback.format_exc())
        finally:
            self.close()

    def find_one(self, collection, value):
        # 根据条件进行查询，返回一条记录
        try:
            self.check_connected()
            return self.db[collection].find_one(value)
        except Exception:
            print(traceback.format_exc())
        finally:
            self.close()

    def find(self, collection, value):
        # 根据条件进行查询，返回所有记录
        try:
            self.check_connected()
            return self.db[collection].find(value)
        except Exception:
            print(traceback.format_exc())
        finally:
            self.close()

    def delete(self, collection, condition):
        """
        删除
        :param collection:
        :param condition:
        :return:
        """
        try:
            self.check_connected()
            return self.db[collection].delete_many(filter=condition).deleted_count
        except Exception:
            print(traceback.format_exc())
        finally:
            self.close()

