import tinydb
from tinydb import Query
from tinydb.storages import JSONStorage

class NoSQLDatabase:
    def __init__(self, db_path='db.json'):
        self.db = tinydb.TinyDB(db_path, storage=JSONStorage)

    def insert(self, table_name, data):
        table = self.db.table(table_name)
        return table.insert(data)

    def get_all(self, table_name):
        table = self.db.table(table_name)
        return table.all()

    def query(self, table_name, field, value):
        table = self.db.table(table_name)
        User = Query()
        return table.search(User[field] == value)

    def update(self, table_name, field, value, updates):
        table = self.db.table(table_name)
        User = Query()
        return table.update(updates, User[field] == value)

    def delete(self, table_name, field, value):
        table = self.db.table(table_name)
        User = Query()
        return table.remove(User[field] == value)

    def close(self):
        self.db.close()

# Example usage:
if __name__ == "__main__":
    db = NoSQLDatabase()

    # Insert data
    db.insert('users', {'name': [
        {'first': 'Alice', 'last': 'Smith'}
    ],
                         'age': 30})
    db.insert('users', {'name': 'Bob', 'age': 25})

    # Get all data
    print("All users:", db.get_all('users'))

    # Query data
    print("Users named Alice:", db.query('users', 'name', 'Alice'))

    # Update data
    db.update('users', 'name', 'Alice', {'age': 31})
    print("Updated users:", db.get_all('users'))

    # # Delete data
    # db.delete('users', 'name', 'Bob')
    # print("Users after deletion:", db.get_all('users'))

    db.close()