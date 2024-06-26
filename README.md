# 🔡Spartanews

# 📝프로젝트 소개
Geeknews 레퍼런스 삼아 Spartanews 구현 프로젝트

# 📅개발 기간
* 2024.05.03일 - 2024.05.09일
  
## 👥멤버 구성
*  박지원 : 댓글 CRUD 구현, 댓글 좋아요 구현, 발표
*  안채연 : 글 좋아요 구현, 글 검색 및 페이지네이션 구현, ERD 작성
*  현유경 : 글 CRUD 구현, readme 작성
*  홍민서 : 회원 기능(로그인 / 로그아웃 / 회원 가입 / 회원 수정 및 탈퇴), readme 작성
  
# 🖥️개발 환경
* Django-drf
* DB : SQLite

# API 명세

<img width="659" alt="image" src="https://github.com/YugyeongHyun/news_team10/assets/160835276/be6d1a22-f529-4b66-b892-d76ea57875c6">




## ERD 문서

<img width="655" alt="image"  src="https://github.com/YugyeongHyun/news_team10/assets/159987685/db007268-230c-4fd1-b805-b66d2df8f29f">



# ✅주요 기능
**댓글 CRUD : 댓글 작성, 댓글 수정, 댓글 삭제**  
  - title : 댓글 제목(번호)
  - content : 댓글 내용
  - created_at : 댓글 생성 시간
  - updated_at : 댓글 수정 시간
  - author : 댓글 작성자
  - parent : 상위 댓글
      - 대댓글 구현

**글 CRUD**  
  - title : 글 제목
  - content : 글 내용
  - created_at : 글 생성 시간
  - updated_at : 글 수정 시간
  - url : 첨부 URL
  - author : 글 작성자
  - category : 글 카테고리
      - 글 작성 시 뉴스, ASK, Show와 같은 카테고리 선택 작성 가능

**회원 기능 구현**  
  - username
  - password
  - password2
  - email
    - 회원가입 및 회원수정
  - intro
    - 회원수정
  - gender

**비밀번호 변경**  
  - password

**회원 탈퇴**
  - user_remove

**좋아요**  
  - like_cnt
    - 글 like 지수 구현
  - unlike_cnt
    - 글의 unlike 지수 구현

**글 검색 및 정렬**
  - title
    - 글 제목 검색
  - pagination
    - pagesize = 5로 설정하여, 글 정렬
   


