import requests as r
from bs4 import BeautifulSoup as bs
from vacancy import Vacancy


def salary_parser(salary):
    salary = salary.split()
    try:
        result = int(salary[0]) + int(salary[1].split("-")[1])
        result = result*1000/2
        return result

    except:
        result = int(salary[1])*1000
        return result


def get_pager(req):
    session = r.Session()
    request = session.get(req, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, "html.parser")
        div = soup.findAll("a", attrs={"data-qa": "pager-page"})[-1].text
        return int(div)-1


def parser(req):
    session = r.Session()
    request = session.get(req, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, "html.parser")
        divs = soup.findAll("div", attrs={"data-qa": "vacancy-serp__vacancy"})

        for div in divs:
            try:
                title = div.find(
                    "a", attrs={"data-qa": "vacancy-serp__vacancy-title"}).text
                employer = div.find(
                    "a", attrs={"data-qa": "vacancy-serp__vacancy-employer"}).text
                salary = div.find(
                    "div", attrs={"data-qa": "vacancy-serp__vacancy-compensation"}).text

                vac = Vacancy(title, employer, salary_parser(salary))
                vac.insert()
            except:
                print("Vacancy Error!")
    else:
        print("ERROR!")


headers = {"accept": "*/*",
           "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36"}

url = "https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=%s&page=%i"


reqs = ["Python", "Сварщик", "Грузчик", "Учитель", "JavaScript", "Pascal"]
for req in reqs:
    url_total = url % (req, 0)
    summary_page = get_pager(url_total)
    for page in range(0, summary_page):
        print(url % (req, page))
        parser(url % (req, page))
