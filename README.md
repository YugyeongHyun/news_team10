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
**댓글 CRUD : 댓글 작성, 댓글 수정, 댓글 삭제**  
  - title : 댓글 제목(번호)
  - content : 댓글 내용
  - created_at : 댓글 생성 시간
  - updated_at : 댓글 수정 시간
  - author : 댓글 작성자
  - parent : 상위 댓글 _ 대댓글 구현

**글 CRUD**  
  - title : 글 제목
  - content : 글 내용
  - created_at : 글 생성 시간
  - updated_at : 글 수정 시간
  - url : 첨부 URL
  - author : 글 작성자
  - category : 글 카테고리 선택

**회원 기능 구현**  
  - username
  - password
  - password2
  - email
  - intro
  - gender

**회원 탈퇴**
  - user_remove

**좋아요**  
  - like_cnt
  - unlike_cnt

**글 검색 및 정렬**
  - title
  - pagination

    

