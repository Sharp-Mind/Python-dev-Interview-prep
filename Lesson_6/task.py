import sqlite3
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper

db_path = '/home/redlance/Geekbrains/Python  prepare/Repository/Python-dev-Interview-prep/Lesson_6/db1'

engine = create_engine(f'sqlite:///{db_path}', echo=True)

con = sqlite3.connect(db_path)
cursorObj = con.cursor()


metadata = MetaData()
all_tables = engine.table_names()

if 'categories' not in all_tables:
    categories = Table('categories', metadata,
                       Column('category_name', String,
                              unique=True, primary_key=True),
                       Column('category_description', String),
                       )
else:
    print('Table "categories" already exists')

if 'units' not in all_tables:
    units = Table('units', metadata,
                  Column('unit', String,
                         unique=True, nullable=False, primary_key=True),
                  )
else:
    print('Table "units" already exists')


if 'positions' not in all_tables:
    positions = Table('positions', metadata,
                      Column('position', String,
                             unique=True, nullable=False, primary_key=True),
                      )
else:
    print('Table "positions" already exists')


if 'goods' not in all_tables:
    goods = Table('goods', metadata,
                  Column('good_id', Integer,
                         unique=True, nullable=False, primary_key=True),
                  Column('good_unit', String,
                         unique=True, nullable=False, foreign_keys='units.unit'),
                  Column('good_cat', String, nullable=False,
                         foreign_keys='categories.category_name'),
                  )
else:
    print('Table "goods" already exists')


if 'employees' not in all_tables:
    employees = Table('employees', metadata,
                      Column('employee_id', Integer,
                             unique=True, nullable=False, primary_key=True),
                      Column('employee_fio', String, nullable=False),
                      Column('employee_position', String, nullable=False,
                             foreign_keys='positions.position'),
                      )
else:
    print('Table "employees" already exists')


if 'vendors' not in all_tables:
    employees = Table('vendors', metadata,
                      Column('vendor_id', Integer,
                             unique=True, nullable=False, primary_key=True),
                      Column('vendor_name', String, nullable=False),
                      Column('vendor_ownerchipform', String),
                      Column('vendor_address', String, nullable=False),
                      Column('vendor_phone', String, nullable=False),
                      Column('vendor_email', String),
                      )
else:
    print('Table "vendors" already exists')

metadata.create_all(engine)
