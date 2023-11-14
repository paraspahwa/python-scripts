# Backup a specified directory to a zip file

import shutil
import os
import datetime

source_dir = "/path/to/source"
backup_dir = "/path/to/backup"

zip_filename = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
shutil.make_archive(os.path.join(backup_dir, zip_filename), 'zip', source_dir)
print(f"Backup completed to {backup_dir}")
