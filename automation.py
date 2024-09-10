import schedule

def call_me():
    print("I am called \n")

schedule.every(1).hour.do(call_me)

while(True):
    schedule.run_pending()