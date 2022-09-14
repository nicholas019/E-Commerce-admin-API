# E-Commerce-admin-API 
원티드 프리온보딩 백엔드 기업 과제

## 목차
1. [프로젝트 개요](#프로젝트-개요)
2. [프로젝트 기술 스택](#프로젝트-기술-스택)
3. [개발 기간](#개발-기간)
4. [팀 구성](#팀-구성)
5. [역할](#역할)
6. [ERD](#ERD)
7. [API 목록](#API-목록)
8. [프로젝트 시작 방법](#프로젝트-시작-방법)


<br>


## 프로젝트 개요
E 커머스 관리자 페이지 API



<br>

## 과제 요구사항 분석 및 구현사항
### **order**
- Create
- Read-List :
    - [x]  list : 제품 주문 내역 열람,
    - [x]  search : 주문 내역 검색, 주문자명으로 검색
    - [x]  filter : 주문 상태, 시작일자, 종료일자에 따른 필터
- Read-Detail
    - [x]  detail : 제품 주문 상세 내역 열람
- Update
    - [x]  주문건에 대하여 발송 처리
        - delivery_state 수정 : 제품 배송 상태 업데이트, 제품의 배송 상태를 배송 중, 배송 완료 등으로 수정 가능

### 2. **Coupon**

- 새로운 쿠폰 타입 신설
    - 쿠폰은 다음의 방식이 있음
        - 배송비 할인
        - % 할인
        - 정액 할인
- Create
    - [x]  특정 신규 쿠폰 코드 발급
    - [x]  쿠폰 코드 등록
    - [x]  신규 쿠폰 타입 생성
- Read - List
    - [x]  쿠폰 관리
        - [x]  filter : 쿠폰 타입 별 사용 횟수
        - [x]  filter : 발급된 쿠폰의 사용 내역 열람
        - [ ]  총할인액   
- Read - Detail
- Update
- Delete

### 3. TEST Code 

- [ ]간단히 구매 내역을 추가 할 수 있도록 구매하기 테스트 코드
    - 쿠폰 사용에 따른 사용 할인 적용
    - 구매 국가, 구매 갯수에 따른 배송비 적용
    - 달러단위 배송비인 경우 일괄 1200원 = 1달러 로 적용하여 배송비를 추가 합니다.
    - 일괄 적용이 아닌 현재 원-달러 환율을 가져와서 배송비를 적용 하는 경우 가산점을 부여 합니 다.

<br>

### 구현사항
**orders app**
1. 주문에 대한 내역 조회API
   주요기능 : 주문 리스트 조회, 주문리스트 검색(주문자명, 주문자ID, 주문상태, 주문시간, 배송상태), 주문리스트 정렬(주문시간별, 주문상태별)
2. 주문내역에 대한 상세페이지 조회 및 배송상태 업데이트 API
   배송상태 변경은 총 4가지로 가능(배송준비, 배송중, 배송완료, 주문취소)
   에러처리 : 배송준비, 배송중, 배송완료, 주문취소 4개 이외의 데이터가 들어올시 에러처리
**coupons app**
1. 쿠폰 발급 내역 조회 및 필터링 API + 발급쿠폰 등록 API
   주요기능 : 
    - 필터링1(쿠폰 사용 여부) :  /?search=1(사용완료), /?search=0(미사용)
    - 필터링2(쿠폰 타입별 ) : /?q=1(%할인), /?q=2(배송비무료), /?q=3()
    - 필터링3(필터링1+2 동시사용) : 사용완료이면서 배송비무료쿠폰, 사용완료이면서 1000원할인쿠폰 등 조합 가능, 예) /?search=1&q=2
    - 발급 쿠폰 등록 : /api/coupon/new/ 에서 발급된 쿠폰번호를 입력하면 선정된 유저에 등록
    - 페이지네이션 기능 추가 페이지당 게시글수는 20개
    - 타입별 사용횟수확인은 사용완료(search=1)와 쿠폰타입으로 필터를 하면 상단의 "count" 값으로 출력
   에러처리 : 발급쿠폰 등록시 사용된 쿠폰이면 "쿠폰번호가 이미 사용되었습니다." 에러메시지 반환
2. 신규 쿠폰 생성 및 생성된 쿠폰 확인 API 
    기능설명 : 신규 쿠폰번호와 쿠폰타입을 지정하면 신규쿠폰 생성, 쿠폰번호는 999,999,999 ~ 10,000,000,000사이 정수만 사용 가능
    에러처리 : 쿠폰번호 중복시 "쿠폰번호가 중복입니다. 쿠폰번호를 확인해주세요." 에러메세지 반환
3. 신규 쿠폰 타입 생성 및 쿠폰 타입 확인 API
    기능설명 : 신규 쿠폰타입 생성 기능, 쿠폰 타입 확인 기능
    에러처리 : 쿠폰번호 중복시 "쿠폰 타입이 중복입니다. 쿠폰 타입을 확인해주세요." 에러메세지 반환

   



## 프로젝트 기술 스택

### Backend
<section>
<img src="https://img.shields.io/badge/Django-092E20?logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Django%20REST%20Framework-092E20?logo=Django&logoColor=white"/>
</section>

### DB
<section>
<img src="https://img.shields.io/badge/MySQL-4479A1?logo=MySQL&logoColor=white"/>
</section>

### Tools
<section>
<img src="https://img.shields.io/badge/GitHub-181717?logo=GitHub&logoColor=white"/>
<img src="https://img.shields.io/badge/Discord-5865F2?logo=Discord&logoColor=white">
<img src="https://img.shields.io/badge/Postman-FF6C37?logo=Postman&logoColor=white">
</section>
<!-- | 백엔드 | DB   |  Tools   |
| ---- | ------ | --- |
|      |        |    | -->


<br>


## 개발 기간
- 2022/09/08~2022/09/14 (추석연휴 4일 제외)


<br>


## 팀 구성
| 김현수 | 유혜선 | 임한구 |  최보미  |
| ------ | ------ | ------ | --- |
| [Github](https://github.com/HyeonsooKim) | [Github](https://github.com/Hyes-y)   | [Github](https://github.com/nicholas019/)   |  [Github](https://github.com/BomiChoi)   |


<br>


## ERD
ERD 

<img width="1242" alt="스크린샷 2022-09-14 오후 10 34 40" src="https://user-images.githubusercontent.com/103249222/190168114-c507c21d-d53d-4526-a30e-a0289397bd1e.png">


<br>


## API 목록
API 명세 주소

<br>


## 프로젝트 시작 방법
1. 로컬에서 실행할 경우
```bash
# 프로젝트 clone(로컬로 내려받기)
git clone -b develop --single-branch ${github 주소}
cd ${디렉터리 명}

# 가상환경 설정
python -m venv ${가상환경명}
source ${가상환경명}/bin/activate
# window (2 ways) 
# 1> ${가상환경명}/Scripts/activate
# 2> activate

# 라이브러리 설치
pip install -r requirements.txt
# 실행
python manage.py runserver
```

<br>
