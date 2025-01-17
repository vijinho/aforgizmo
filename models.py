# -*- coding: utf-8 -*-
'''
Pocket Philosopher Database Models
===================================

Models to handle aphorism data
'''

import click
from peewee import *
from datetime import datetime
import json
import kivy
kivy.require('1.8.0')
from kivy import platform

def get_database():
    if platform == 'android':
        file = '/sdcard/pocketphilosopher/aphorisms.db'
    else:
        import ConfigParser
        config = ConfigParser.RawConfigParser()
        config.read('config.ini')
        file = config.get('database', 'file')
    return SqliteDatabase(file)


class BaseModel(Model):

    """(Peewee) Base Database model for Aphorisms App"""
    class Meta:
        database = get_database()


class Aphorism(BaseModel):

    """Database model for Aphorisms"""
    author = CharField()
    source = CharField()
    aphorism = TextField()
    tags = TextField()
    created = DateTimeField(default=datetime.now)

    def AsHash(self):
        """Return a representation of the object field data as a hash
        hack was required to make bulk insert possible by replacing 'T' in
        isoformat
        """
        data = {
            'id': self.id,
            'created': self.created.isoformat().replace('T', ' '),
            'author': self.author,
            'source': self.source,
            'aphorism': self.aphorism,
            'tags': self.tags
        }
        return data

    def ToJSON(self):
        """Return a representation of the object field data as JSON"""
        return json.dumps(self.AsHash(), indent=4, sort_keys=True)

    def ToOneLine(self, length=80):
        """Return a string of the object data as a one line string"""
        string = '{0}: \"{1}\"'.format(self.author, self.aphorism)
        return "{0}".format(
            (string[:length] + '"...') if len(string) > length else string)

    def RemoveDuplicates(self):
        """Remove duplicate aphorisms by date created"""
        dupes = self.raw("SELECT id, aphorism "
                        "FROM aphorism "
                        "WHERE aphorism IN (SELECT aphorism "
                        "                   FROM aphorism "
                        "                   GROUP BY aphorism "
                        "                   HAVING COUNT(aphorism) > 1"
                        "                   ORDER BY aphorism) "
                        "ORDER BY aphorism, created")
        last = None
        removed = 0
        for a in dupes.execute():
            if last is None:
                last = a
                continue
            if last.aphorism == a.aphorism:
                try:
                    a.delete_instance()
                except Exception as e:
                    pass
                else:
                    removed = removed + 1
            else:
                last = a
        return removed

def CreateTables():
    """Create database tables for Aphorisms in SQLite"""
    try:
        Aphorism.create_table()
    except OperationalError as e:
        click.secho('Aphorism table already exists!' + e, fg='red')
    else:
        click.secho('Aphorism table successfully created.', fg='green')

if __name__ == "__main__":
    CreateTables()
