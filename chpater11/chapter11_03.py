#외부패키지 를 다운로드 설치하는 방법
#https://pypi.org/ 현재 80만개 패키지가 등록되어있음
#pip install beatifulsoup4
#해당되는 패키지에 사용하는 방법들이 설명되어있다.(Read.me)

from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

