# Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

- What NoSQL means
- What is the difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements

### MongoDB Command File

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- All your files should end with a new line
- The first line of all your files should be a comment: `// my comment`
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

## More Info

### Install MongoDB 4.2 in Ubuntu 18.04

[Official installation guide](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...

$ sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
...
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'

Potential issue if documents creation doesn’t work or this error: Data directory /data/db not found., terminating
$ sudo mkdir -p /data/db

