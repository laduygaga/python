import csv
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1",
  database="csv"
)

cursor = mydb.cursor()

# create database
cursor.execute("CREATE DATABASE csv")

# create table
cursor.execute("CREATE TABLE categories (id bigint not null auto_increment primary key, category_id varchar(255), parent_id varchar(255), path varchar(255), name varchar(255), include_in_menu varchar(255), meta_title varchar(255) , meta_description varchar(255), url_key varchar(255), url_path varchar(255), Smartweb_ID varchar(255))")

# insert into table 
with open('categories.csv') as csv_file: 
    csv_data = csv.reader(csv_file, delimiter=',')
    for row in csv_data:
        cursor.execute('INSERT INTO categories (category_id, parent_id, path, name, include_in_menu, meta_title, meta_description, url_key, url_path, Smartweb_ID) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")', row)


mydb.commit()
cursor.close()

