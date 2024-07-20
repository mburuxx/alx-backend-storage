# 0x00. MySQL Advanced

## Description
This project involves advanced concepts and techniques in MySQL, including creating tables with constraints, optimizing queries with indexes, implementing stored procedures, functions, views, and triggers.

## Concepts
For this project, you are expected to understand the following concept:

- Advanced SQL

## Resources
Read or watch:
- [MySQL cheatsheet](https://dev.mysql.com/doc/refman/5.7/en/cheatsheets.html)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.percona.com/blog/2020/06/01/mysql-performance-how-to-leverage-mysql-database-indexing/)
- [Stored Procedure](https://dev.mysql.com/doc/refman/5.7/en/stored-procedures.html)
- [Triggers](https://dev.mysql.com/doc/refman/5.7/en/triggers.html)
- [Views](https://dev.mysql.com/doc/refman/5.7/en/views.html)
- [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)

## Learning Objectives
By the end of this project, you should be able to explain the following without external resources:

- How to create tables with constraints.
- How to optimize queries by adding indexes.
- What stored procedures and functions are, and how to implement them in MySQL.
- What views are, and how to implement them in MySQL.
- What triggers are, and how to implement them in MySQL.

## Requirements
- All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30).
- All your files should end with a new line.
- All your SQL queries should have a comment just before them (i.e., syntax above).
- All your files should start with a comment describing the task.
- All SQL keywords should be in uppercase (SELECT, WHERE, etc.).
- A `README.md` file, at the root of the folder of the project, is mandatory.
- The length of your files will be tested using `wc`.

## Usage
To run MySQL, use “container-on-demand”:
1. Request for container Ubuntu 18.04 - Python 3.7.
2. Connect via SSH or WebTerminal.
3. Start MySQL in the container:
    ```sh
    $ service mysql start
    ```

To execute a SQL script:
```sh
$ cat my_script.sql | mysql -uroot -p my_database
Enter password: 
