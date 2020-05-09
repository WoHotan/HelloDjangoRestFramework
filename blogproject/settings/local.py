from .common import *

SECRET_KEY = 'development-secret-key'

DEBUG = True

ALLOWED_HOSTS = ['*']

# 搜索设置
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://hellodjango_rest_framework_tutorial_elasticsearch_local:9200/'
