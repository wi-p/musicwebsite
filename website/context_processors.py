from datetime import datetime

def showData(request):
    return {'date' : datetime.today()}