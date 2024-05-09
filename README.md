# 🔡Spartanews

# 📝프로젝트 소개
Geeknews 구현 프로젝트

# 📅개발 기간
* 2024.05.03일 - 2024.05.09일
  
## 👥멤버 구성
*  박지원 : 댓글 CRUD 구현, 댓글 좋아요 구현
*  안채연 : 글 좋아요 구현, 글 검색 및 페이지네이션 구현
*  현유경 : 글 CRUD 구현
*  홍민서 : 회원 기능(로그인 / 로그아웃 / 회원 가입 / 회원 수정 및 탈퇴)
  
## 🖥️개발 환경
* Django-drf
* DB : SQLite

# ✅주요 기능
**댓글 CRUD**  
  - title 
  - content
  - created_at
  - updated_at
  - author
  - parent

**글 CRUD**  
  - title
  - content
  - created_at
  - updated_at
  - url
  - author
  - category

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

    

    

