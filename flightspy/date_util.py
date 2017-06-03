from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

#TODO: Either leave as is or add to run function
start_date = date(2017, 6, 3)
end_date = date(2017, 6, 30)

today = date.today()

date_list = []


for single_date in daterange(start_date, end_date):
    date_form = single_date.strftime("%Y-%m-%d")
    date_list.append(date_form)
    print(date_form)
