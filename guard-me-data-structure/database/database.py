import os
from os.path import isfile

conn = psycopg2.connect(env['DATABASE_NAME'], env['HOST'], env['USER'], env['PASS'], env['PORT'])
