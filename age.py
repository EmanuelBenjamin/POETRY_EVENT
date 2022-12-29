from datetime import datetime
from dateutil.relativedelta import relativedelta

def obAge(date_of_birth ):
    date_of_birth = datetime().strptime(date_of_birth , '%Y-%m-%d')
    age = relativedelta(datetime.now(), date_of_birth )
    return age

    
