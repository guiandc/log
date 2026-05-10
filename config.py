import os
from datetime import datetime

folder_logs = "logs"
file_name_log = f'{os.getcwd()}/{folder_logs}/log_{datetime.now().strftime("%Y%m%d%H%M%S")}.log'
