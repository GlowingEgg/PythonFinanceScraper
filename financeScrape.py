import urllib2
import time

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        year = None
        month = None
        day = None
    def getInfo(self):
        year = int(time.strftime("%Y"))
        month = str(int(time.strftime("%m")) -1).zfill(2)
        day = str(int(time.strftime("%d"))).zfill(2)
        lastyear = year - 1
        url = "http://ichart.yahoo.com/table.csv?s={0}&a={1}&b={2}&c={3}&d={4}&e={5}&f={6}&g=d&ignore=.csv".format(self.ticker,month,day,lastyear,month,day,year)
        print url
        original = urllib2.urlopen(url)
        newCSV = open("%s.csv"%self.ticker, "wb")
        newCSV.write(original.read())
        newCSV.close()
        print "ya bitch"

current = None
stock = []
year = int(time.strftime("%Y"))
month = str(int(time.strftime("%m")) -1).zfill(2)
day = str(int(time.strftime("%d"))).zfill(2)
lastyear = year - 1
print year, month, day, lastyear
while(1):
    ticker = raw_input("Enter ticker(type done if done):")
    url = "http://ichart.yahoo.com/table.csv?s={0}&a={1}&b={2}&c={3}&d={4}&e={5}&f={6}&g=d&ignore=.csv".format(ticker,month,day,lastyear,month,day,year)
    if ticker == "done":
        break
    stock.append(Stock(ticker.upper()))
    stock[-1].getInfo()



