import os
from django.core.management import call_command

db_path = os.path.join('/tmp', 'db.sqlite3')

if not os.path.exists(db_path):
    print("Initializing SQLite database...")
    call_command('migrate')
    call_command('loaddata', 'initial_data.json')  # Optional: Load fixtures if needed
