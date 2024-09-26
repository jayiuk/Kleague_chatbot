import langchain
import langchain_core
import langsmith
from langchain_community.document_loaders import SeleniumURLLoader
from selenium.webdriver.common.by import By


class document_loader():
    def __init__(self, list):
        self.list = list

    def url2doc(self):
        url_list = self.list
        loader = SeleniumURLLoader(url_list, browser = 'chrome')
        doc_list = loader.load()
        for doc in doc_list:
            text = '로그인\n\n회원가입\n\nKR\n\n뉴스\n\n전체\n\n공지사항\n\n리그\n\n구단\n\n유소년\n\n팬\n\n영상\n\n전체\n\n하이라이트\n\n골\n\n케튜브\n\n구단\n\nK리그 TV\n\n일정/결과/티켓\n\nK리그1\n\nK리그2\n\n기록\n\n팀 순위\n\n선수 순위\n\nADIDAS POINT\n\n데이터 포털\n\n선수/감독\n\n유소년\n\nK리그 주니어\n\nK리그 유스 챔피언십\n\nYOUTH TRUST\n\nSOCIAL MEDIA\n\n유소년 부가데이터\n\n이벤트\n\nK리그 판타지\n\n사회공헌\n\nK League Assist\n\n모두의축구장 모두의K리그\n\n드림어시스트\n\n그린킥오프\n\n유니파이드컵\n\n케어프로젝트\n\nAbout K League\n\n인사말\n\n연혁\n\nCI소개\n\n조직도\n\n스폰서\n\n정관/규정\n\n대회요강\n\n경영공시\n\n자료실\n\n역대 엠블럼\n\n아카데미\n\nK리그 클린센터\n\n찾아오시는 길\n\n경력증명서발급\n\nK리그 폰트\n\n명예의 전당\n\n뉴스\n\nK리그1・2의 최신 소식을 모두 확인 할 수 있는 공간입니다.\n\n'
            text2 = '\n\n뉴스\n\n전체\n\n공지사항\n\n리그\n\n구단\n\n유소년\n\n팬\n\n영상\n\n전체\n\n하이라이트\n\n골\n\n케튜브\n\n구단\n\nK리그 TV\n\n일정/결과/티켓\n\nK리그1\n\nK리그2\n\n기록\n\n팀 순위\n\n선수 순위\n\nADIDAS POINT\n\n데이터 포털\n\n선수/감독\n\n유소년\n\nK리그 주니어\n\nK리그 유스 챔피언십\n\nYOUTH TRUST\n\nSOCIAL MEDIA\n\n유소년 부가데이터\n\n이벤트\n\nK리그 판타지\n\n사회공헌\n\nK League Assist\n\n모두의축구장 모두의K리그\n\n드림어시스트\n\n그린킥오프\n\n유니파이드컵\n\n케어프로젝트\n\nAbout K League\n\n인사말\n\n연혁\n\nCI소개\n\n조직도\n\n스폰서\n\n정관/규정\n\n대회요강\n\n경영공시\n\n자료실\n\n역대 엠블럼\n\n아카데미\n\nK리그 클린센터\n\n찾아오시는 길\n\n경력증명서발급\n\nK리그 폰트\n\n명예의 전당\n\nT 02) 2002 - 0663 A 서울 종로구 경희궁길 46 축구회관 5층\n\nFamily Sites\n\nCopyright 2021 © K LEAGUE. All right reserved.\n\n개인정보처리방침\n\n이용약관\n\n경력증명서발급\n\n찾아오시는 길'
            doc.page_content = doc.page_content.replace(text, "")
            doc.page_content = doc.page_content.replace(text2, "")
            doc.page_content = doc.page_content.replace('\n\nclub', '\n\ndate')
        return doc_list