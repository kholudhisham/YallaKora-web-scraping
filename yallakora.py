import requests
from bs4 import BeautifulSoup 
import csv 
date = input("Please Enter a Date in The Following Format MM/DD/YYYY:")
page = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}")
def main(page):
    try:
        src = page.content
        soup = BeautifulSoup(src, "lxml")
        matches_details = []
        championships = soup.find_all("div", {'class': 'matchCard'})
        def get_match_info(championships):
            championship_title = championships.contents[1].find("h2").text.strip()
            all_matches = championships.contents[3].find_all("li")
            num_of_matches = len(all_matches)
            for i in range (num_of_matches) :
                #get teams names
                team_A = all_matches[i].find("div",{'class':'teamA'}).text.strip()
                team_B= all_matches[i].find("div", {'class':'teamB'}).text.strip()
                #get score 
                match_result= all_matches[i].find("div", {'class':'MResult'}).find_all('span', {'class':'score'})
                score =f"{match_result[0].text.strip()} _ {match_result[1].text.strip()}"
                #get time 
                match_time = all_matches[i].find("div", {'class':'MResult'}).find('span', {'class':'time'}).text.strip()
                matches_details.append({"نوع البطولة":championship_title, "الفريق الاول":team_A, "الفريق الثانى":team_B ,"موعد المباراه":match_time, "النتيجة":score})
    except :
        print("Error Occured")
        
        

    for i in range(len(championships)):
        get_match_info(championships[i])    
    keys = matches_details[0].keys()
    with open('C:/Users/kholud\Desktop/data analysis(udcity)/Data Analyst Portfolio/YallaKora/matches_detailes.csv','w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print("File Created")
main(page)   
       