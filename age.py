from datetime import datetime
from dateutil.relativedelta import relativedelta

def obAge(birth):
    birth = datetime.strptime(birth, '%Y-%m-%d')
    age = relativedelta(datetime.now(), birth )
    return age

    
