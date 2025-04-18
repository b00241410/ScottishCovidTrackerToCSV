import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

#get today's date as a string called today
today=str(date.today())

my_url = 'https://www.statista.com/statistics/1107118/coronavirus-cases-by-region-in-scotland/'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#parse the html via soup function made earlier
page_soup=soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"readingAid"})
filename="cases1"

f = open(today + ' covid cases by scottish health board.csv','w')
f.write('Health board:, Number of cases:\n')

#put each authority name and corresponding latest case number into array called contianer
container = containers[0]

caseList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
cohortList=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
getSize = container.findAll("td")
SizeOfArray = int(len(getSize))
x=-1
y=0
k=0
#NOTE: run time error if not array-1
while x < SizeOfArray-1: #for each of the 14 Scottish local authorities
    #(28 as health board name and case numbers are in sam list) 
    x=x+1
    covidInfoList = container.findAll("td")
    outputText = covidInfoList[x].text
    print(outputText)
    cohortList[k]=outputText
    k=k+1
    
    f.write(outputText +",")
    x=x+1
    outputText = covidInfoList[x].text
    print("Number of cases:")
    print(outputText)
    
    #remove commas from the string containing case numbers
    temp1=outputText.replace(',', '')
    f.write(temp1 +",\n")
    
    caseList[y]=int(temp1)
    y=y+1
    
    print("")
    

f.write('Correct as of '+today+'. Program by Kenneth Munro')
f.close()

s = pd.Series([caseList[0],caseList[1],caseList[2],caseList[3],caseList[4],caseList[5],caseList[6],caseList[7],caseList[8]], [cohortList[0],cohortList[1],cohortList[2],cohortList[3],cohortList[4],cohortList[5],cohortList[6],cohortList[7],cohortList[8]])

fig, ax = plt.subplots()

s.plot.bar()
fig.savefig(fname=(' '+today+' scottish covid numbers.png'), bbox_inches="tight")
