# Git&Github Day 02

담당자: 이현주
상태: 완료
마감일: 2025년 5월 27일
작성일: 2025년 5월 27일

# 🏷️ Git Tag 기능 정리

Git의 `tag` 기능은 특정 커밋에 **버전 이름이나 마일스톤**을 부여하는 데 사용되며, 주로 **배포 버전 관리**에 활용됩니다.

---

## ✅ 기본 태그 생성

### 마지막 커밋에 태그 달기 (annotated)

```bash
git tag v2.0.0 -m "oz 버전"
```

> -m 옵션은 메시지를 포함한 annotated tag를 생성함annotated 태그는 작성자, 날짜, 메시지 등이 포함됨
> 

---

## 📌 특정 커밋에 태그 달기

```bash
git tag v1.0.0 <커밋해시> -m "굿거리 버전"
git tag v1.2.1 <커밋해시> -m "진행 완료"
```

---

## 🔍 태그 확인 및 검색

### 특정 태그 정보 보기

```bash
git show v2.0.0
```

### 특정 패턴으로 필터링

```bash
git tag -l 'v1.*'
```

> -l 옵션은 태그 리스트에서 특정 패턴만 보여줌
> 

---

## 📦 태그를 이용한 코드 버전 전환

### 해당 태그 시점으로 이동

```bash
git checkout v1.2.1
```

> 주의: Detached HEAD 상태가 됨
> 

### 이전 브랜치로 돌아가기

```bash
git switch -
```

---

## ☁️ 원격 저장소와 태그 연동

### 태그 푸시

```bash
git push origin v1.0.0
```

### 전체 태그 푸시

```bash
git push origin --tags
```

---

## ❌ 태그 삭제

### 로컬 태그 삭제

```bash
git tag -d v1.0.0
```

### 원격 태그 삭제

```bash
git push origin :refs/tags/v1.0.0
```

---

## 💼 실무에서 자주 쓰이는 예시

| 상황 | 명령어 |
| --- | --- |
| 첫 배포 | `git tag v1.0.0 -m "초기 배포"` |
| 기능 완료 | `git tag feature-login-finished -m "로그인 기능 완료"` |
| QA용 태그 | `git tag qa-ready -m "QA 완료"` |
| 긴급 핫픽스 | `git tag v1.0.1 -m "보안 패치"` |
| 이전 상태로 복귀 | `git checkout v1.0.1` |

# 🪝 Git Hooks & Gitmoji CLI 활용 정리

---

## 🎣 Git Hooks란?

- Git에서 제공하는 **자동화 스크립트 시스템**
- 특정 Git 이벤트 전후로 **자동 실행되는 스크립트**
- 프로젝트의 **커밋 메시지 검증**, **코드 포맷 검사**, **테스트 자동 실행** 등에 사용

---

## 🔧 자주 사용하는 Hook 종류

| Hook 이름 | 실행 시점 | 사용 예시 |
| --- | --- | --- |
| `pre-commit` | `git commit` 전 | 린트 검사, 테스트 수행, 포맷팅 |
| `pre-push` | `git push` 전 | 테스트, 빌드 확인 |

---

## 📍 pre-commit 사용 예시

1. `.git/hooks/pre-commit` 파일 생성 (또는 수정)
2. 실행 권한 부여

```bash
chmod +x .git/hooks/pre-commit
```

1. 예시 스크립트:

```bash
#!/bin/sh
npm run lint
```

---

## 📍 pre-push 사용 예시

1. `.git/hooks/pre-push` 파일 생성
2. 실행 권한 부여

```bash
chmod +x .git/hooks/pre-push
```

1. 예시 스크립트:

```bash
#!/bin/sh
npm test
```

---

## 😎 Gitmoji CLI로 이모지 커밋하기

### 📦 설치

```bash
brew install gitmoji
```

> macOS 기준, Linux는 npm i -g gitmoji-cli도 가능
> 

---

### 🚀 프로젝트에 Gitmoji 훅 적용

```bash
gitmoji -i
```

> -i는 git hook을 설정해 커밋 시 자동으로 gitmoji CLI를 실행하게 함
> 

---

### ✅ 사용법

```bash
git add .
gitmoji -c
```

> -c를 통해 이모지 선택 + 커밋 메시지 입력 CLI 실행
> 

---

### 🔄 커밋 후 푸시

```bash
git push origin main
```

---

## 💡 정리

| 단계 | 설명 |
| --- | --- |
| `gitmoji -i` | 프로젝트에 commit hook 적용 |
| `gitmoji -c` | 커밋 이모지 선택 후 메시지 입력 |
| `git push` | 커밋 푸시 |

# 🔗 Git Submodules 개념 및 활용 정리

---

## 1️⃣ Git Submodules란?

- 하나의 Git 프로젝트 안에 **다른 Git 저장소를 하위 모듈(서브모듈)로 포함**시키는 기능
- 대형 프로젝트에서 **공통 라이브러리, 외부 모듈** 등을 독립된 저장소로 관리하고 싶을 때 사용
- 서브모듈은 독립적으로 버전 관리되며, 메인 프로젝트에서는 서브모듈의 특정 커밋을 참조함

---

## 2️⃣ 기본 개념

| 용어 | 설명 |
| --- | --- |
| 메인 프로젝트 (main-project) | 서브모듈을 포함하는 최상위 저장소 |
| 서브모듈 (submodule) | 메인 프로젝트 안에 포함된 독립된 Git 저장소 |
| `.gitmodules` | 메인 프로젝트에 서브모듈 정보가 기록된 설정 파일 |

---

## 3️⃣ 실습 절차

### (1) 두 개의 프로젝트 준비

- `main-project` 폴더 생성 및 Git 초기화
- `submodule` 폴더 생성 및 Git 초기화
- 각각에 아무 파일 하나씩 만들고 커밋하기
- GitHub에 각각 레포지토리 생성 및 원격 연결(push)

---

### (2) main-project에 submodule 추가

```bash
cd main-project
git submodule add <submodule_깃허브_주소> [하위폴더명_생략가능]
```

- 실행 후, main-project 내에 `submodule` 폴더가 생성됨
- `.gitmodules` 파일이 자동 생성되어 서브모듈 정보가 저장됨

---

### (3) 변경사항 확인 및 커밋

```bash
git status
```

- `.gitmodules`와 `submodule` 폴더가 변경된 것을 확인 가능

```bash
git add .gitmodules submodule
git commit -m "Add submodule"
git push origin main
```

---

### (4) 서브모듈 수정 및 메인 프로젝트 확인

- 서브모듈(`submodule` 폴더)에서 파일 수정 후 커밋 & 푸시
- 메인 프로젝트로 돌아와서 `git status` 확인

> 서브모듈 내부 변경사항은 메인 프로젝트의 변경사항으로 포함되지 않음
> 

---

### (5) 서브모듈 변경사항 반영하기

- 메인 프로젝트에서 서브모듈 커밋 업데이트를 반영하려면

```bash
cd submodule
git pull origin main
cd ..
git add submodule
git commit -m "Update submodule to latest commit"
git push origin main
```

---

## 4️⃣ 주의사항

- 서브모듈은 독립 저장소이므로 **변경 사항 커밋/푸시는 각자 따로 해야 함**
- 메인 프로젝트는 서브모듈의 특정 커밋만 추적
- 클론 시, `git clone --recurse-submodules` 로 서브모듈까지 같이 내려받기 가능