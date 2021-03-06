import datetime
from mongoengine import *

class Crawler(Document):
  url = StringField(required=True)
  _id = StringField(required=True, primary_key=True)
  title = StringField(required=True)
  body = ListField(StringField(required=True))
  hub = FloatField(required=True, default=1.0)
  authority = FloatField(required=True, default=1.0)
  pageRank = FloatField(required=True, default=1.0)
  created_at = DateTimeField(default=datetime.datetime.now())
  updated_at = DateTimeField(default=datetime.datetime.now())

class InvertedIndex(Document):
  term = StringField(required=True, primary_key=True)
  termNum=IntField(required=True, min_value=0)
  doc_info = ListField(DictField(required=True), default=[])
  idf = FloatField(required=True, default=1)
  tfidf = DictField(default={})
  created_at = DateTimeField(default=datetime.datetime.now())
  updated_at = DateTimeField(default=datetime.datetime.now())

class User(Document):
  userid = StringField(required=True, primary_key=True)
  password = StringField(required=True)
  likes = DictField(required=True, default={})
  dislikes = DictField(required=True, default={})
  history = DictField(required=True, default={})
  created_at = DateTimeField(default=datetime.datetime.now())
  updated_at = DateTimeField(default=datetime.datetime.now())

databaseName = 'ChefmateDB'
# databaseName = 'ChefmateDB_Alt'

databaseAddr = '3.21.167.180'
# databaseAddr = '18.222.251.5'

