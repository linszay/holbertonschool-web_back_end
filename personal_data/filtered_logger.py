#!/usr/bin/env python3
"""filter_datum returns log message obfuscated(type annotated)"""
import re
from typing import List
import logging
import csv
import mysql.connector
from mysql.connector import MySQLConnection
import os


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """updated to accept fields"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    sep = SEPARATOR
    red = REDACTION

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records using filter_datum"""
        message = super(RedactingFormatter, self).format(record)
        for field in self.fields:
            message = filter_datum([field], self.red, message, self.sep)
        return message


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """use regex to replace occurences of certain field values"""
    """select separator char and its surrounding parentheses"""
    """"|".join(map(re.escape, creates pattern to match/join fields"""
    """capture separator character after field"""
    """replace 1st capture group with 3rd capture group"""
    r = re.escape
    s = separator
    red = redaction
    f = fields
    return re.sub(rf'({r(s)})({"|".join(map(r, f))})({r(s)})',
                  rf'\1{red}\3', message)


def get_logger() -> logging.Logger:
    """logs up to logging.INFO level and has a streamhandler"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELD))
    logger.addHandler(stream_handler)
    return logger


def get_db() -> MySQLConnection:
    """returns a connector to the database"""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username, password=password, host=host, database=database
    )


def main() -> None:
    """get database connection, retrieve rows and display formatted"""
    logger: Logger = logging.getLogger('user_data')
    db: MySQLConnection = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields_to_filter = ["name", "email", "phone", "ssn", "password"]

    ftf = fields_to_filter
    fd = filter_datum
    for row in cursor:
        log_msg = "; ".join([f"{field}={fd(ftf, '***', str(value), ';')}"
                            for field, value in zip(ftf, row)])
        logger.info(log_msg)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
