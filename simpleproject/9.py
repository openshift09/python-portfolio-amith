import datetime, shutil
shutil.copy("data.csv",f"backup_{datetime.date.today()}.csv`")