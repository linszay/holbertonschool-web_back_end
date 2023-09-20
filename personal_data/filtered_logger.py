#!/usr/bin/env python3
"""filter_datum returns log message obfuscated(type annotated)"""
import re
from typing import List, None
import logging
import csv
import mysql.connector
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

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records using filter_datum"""
        message = super(RedactingFormatter, self).format(record)
        for field in self.fields:
            message = filter_datum([field], self.REDACTION, message, self.SEPARATOR)
        return message

PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """use regex to replace occurences of certain field values"""
    """select separator char and its surrounding parentheses"""
    """"|".join(map(re.escape, creates regex pattern to match fields and joins them"""
    """capture separator character after field"""
    """replace 1st capture group with 3rd capture group"""
    ree = re.escape
    sep = separator
    red = redaction
    return re.sub(
        rf'({ree(sep)})({"|".join(map(ree, fields))})({ree(sep)})', rf'\1{red}\3',
        message
    )

def get_logger() -> logging.Logger:
        """logs up to logging.INFO level and has a streamhandler"""
        logger = logging.getLogger('user_data')
        logger.setLevel(logging.INFO)
        logger.propagate = False
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELD))
        logger.addHandler(stream_handler)
        return logger

def get_db() -> mysql.connector.connection.MySQLConnection:
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

    for row in cursor:
        log_message = "; ".join([f"{field}={filter_datum(fields_to_filter, '***', str(value), ';')}" for field, value in zip(fields_to_filter, row)])
        logger.info(log_message)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
