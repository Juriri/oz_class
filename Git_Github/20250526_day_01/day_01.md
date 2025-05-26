# Git&Github Day 01

담당자: 이현주
상태: 진행 중
마감일: 2025년 5월 26일
작성일: 2025년 5월 26일

# 🚀 Git 제대로 활용하기

---

## 🛠 Git 기본 설정 및 브랜치 초기화

### 🔧 기본 브랜치를 `main`으로 설정

> master는 노예제 역사와 연관된 용어로 여겨져, 현재는 main 사용을 권장함.
> 

```bash
git config --global init.defaultBranch main
```

---

## 🗂 Git 프로젝트 시작하기

### 📁 새 Git 저장소 초기화

```bash
git init
```

---

### 📝 `.gitignore`와 상태 확인

```bash
git status
```

`.gitignore` 파일에 Git이 추적하지 않을 파일/디렉토리 명시

```
# 예시
node_modules/
.env
.DS_Store
```

---

### 🔐 첫 번째 커밋 남기기

```bash
git add .
git commit -m "프로젝트 초기 설정"
```

---

## ✅ 실무에서 많이 쓰는 `git commit` 명령어

| 명령어 | 설명 |
| --- | --- |
| `git commit -m "메시지"` | 가장 기본적인 커밋 |
| `git commit -am "메시지"` | 수정된 파일을 add 없이 바로 커밋(신규 파일은 제외) |
| `git commit --amend` | 이전 커밋을 수정 (내용 또는 메시지) |
| `git commit --amend -m "새 메시지"` | 메시지만 간단히 수정 |
| `git commit -v` | 변경 diff를 보며 커밋 메시지 작성 |
| `git commit --allow-empty -m "빈 커밋"` | 실제 변경 없이 커밋 (CI 트리거 등용) |

---

## 🕵️‍♂️ 실무에서 자주 쓰는 `git log` 명령어

| 명령어 | 설명 |
| --- | --- |
| `git log` | 기본 로그 보기 |
| `git log --oneline` | 한 줄 요약 보기 |
| `git log --graph` | 브랜치 병합 흐름 시각화 |
| `git log --oneline --graph --all` | 전체 브랜치 흐름 한눈에 보기 |
| `git log -p` | 커밋 별 코드 변경(diff) 보기 |
| `git log --author="이름"` | 특정 작성자 커밋만 보기 |
| `git log --since="3 days ago"` | 최근 커밋 내역 필터링 |
| `git log --stat` | 커밋별 수정된 파일/라인 수 요약 |
| `git log <파일명>` | 특정 파일 이력만 보기 |

---

## 🧾 커밋 메시지 컨벤션 (Conventional Commits)

```bash
git commit -m "feat: 로그인 기능 추가"
git commit -m "fix: 비밀번호 암호화 오류 수정"
git commit -m "chore: 패키지 업데이트"
git commit -m "refactor: 중복 코드 제거"
git commit -m "docs: README 수정"
```

| 태그 | 용도 |
| --- | --- |
| `feat:` | 새로운 기능 추가 |
| `fix:` | 버그 수정 |
| `refactor:` | 리팩토링 (기능 변화 없음) |
| `docs:` | 문서 수정 |
| `test:` | 테스트 코드 관련 |
| `chore:` | 기타 작업 (빌드, 설정 등) |

---

## 🧹 커밋 이력 깔끔하게 정리 (Rebase)

```bash
git rebase -i HEAD~3
```

- 최근 3개의 커밋을 인터랙티브하게 정리
- `pick`, `squash`, `reword` 등으로 조작 가능

### ✅ 커밋 합치기 예시

```
pick a1b2c3 feat: 로그인
squash b2c3d4 fix: 오류 수정
squash c3d4e5 chore: 로그 제거
```

```bash
git push --force
```

> 리베이스 후에는 강제 푸시 필요
> 
> 
> 협업 브랜치에서는 주의해서 사용
> 

---

# 🔄 Git 되돌리기와 병합하기

## ⏪ 이전 커밋으로 되돌리기 (Reset)

| 명령어 | 설명 |
| --- | --- |
| `git reset --soft [커밋 해시]` | HEAD만 이동, 작업 내용과 스테이징은 유지 |
| `git reset --mixed [커밋 해시]` | HEAD 이동 + 스테이징 해제 (기본값) |
| `git reset --hard [커밋 해시]` | HEAD 이동 + 작업 내역 전부 삭제 |

> 되돌릴 때는 --hard 사용 시 주의: 변경 사항 복구 불가
> 

실수로 reset hard 명령어로 삭제한 커밋 되돌리기

git reflog

## 💥 실수로 `reset --hard`를 썼을 때 복구하는 방법

### ▶️ `git reflog`: 커밋 히스토리 추적 로그

```bash
git reflog
```

예시 출력:

```
1a2b3c4 HEAD@{0}: reset: moving to HEAD~1
3d4e5f6 HEAD@{1}: commit: 로그인 기능 추가
...
```

### 복구 방법:

1. 원하는 커밋 해시를 찾음 (예: `3d4e5f6`)
2. 해당 커밋으로 다시 이동

```bash
git reset --hard 3d4e5f6
```

✅ 삭제된 것처럼 보였던 커밋이 복구됨!

## 🌿 Git 브랜치에 대해 알아보기

## 🌱 브랜치 생성

```bash
git branch [브랜치명]
```

> 새로운 브랜치를 생성하지만 자동으로 이동되진 않음
> 

---

## 📋 브랜치 목록 확인

```bash
git branch
```

> 현재 로컬에 존재하는 브랜치 목록 확인
> 
> 
> 현재 위치한 브랜치 앞엔 `*` 표시됨
> 

---

## 🚀 브랜치 이동

```bash
git switch [브랜치명]
```

> 해당 브랜치로 이동 (checkout 대체 명령)
> 

---

### 🤔 `git switch` vs `git checkout` 차이점

| 비교 항목 | `git switch` | `git checkout` |
| --- | --- | --- |
| 도입 시기 | Git 2.23 이상 | 전통적인 방식 |
| 목적 | 브랜치 이동 전용 | 브랜치 + 파일 모두 처리 가능 |
| 사용성 | 명확하고 안전함 | 다기능이라 실수 가능성 ↑ |

> ✅ 브랜치 작업만 할 거면 switch 권장
> 
> 
> `checkout`은 파일 변경에도 쓰이므로 실수 방지 목적에서 `switch`가 명확함
> 

---

## ⚡ 브랜치 생성 + 바로 이동

```bash
git switch -c [브랜치명]
```

예시:

```bash
git switch -c oz
```

> 브랜치를 새로 만들고 바로 이동까지 한 번에 수행
> 

---

## 🧹 브랜치 삭제

```bash
git branch -d [브랜치명]
```

> 브랜치 삭제 (병합된 경우에만 삭제 가능)
> 

### ❗ `d` vs `D` 차이

| 옵션 | 설명 |
| --- | --- |
| `-d` | 병합된 브랜치만 삭제 가능 (보호용) |
| `-D` | 병합 여부 상관없이 강제 삭제 (위험) |

> 실수 방지 위해 기본은 -d, 정말 필요할 때만 -D
> 

---

## 📝 브랜치 이름 변경

```bash
git branch -m [현재 브랜치명] [새 이름]
```

예시:

```bash
git branch -m master main
```

> 로컬 브랜치의 이름을 바꿈
> 
> 
> 현재 브랜치 이름을 바꾸고 싶을 경우, `[현재 브랜치명]` 생략 가능
> 

```bash
git branch -m main
```

---

## 🔺 복잡한 이력에서 중요해지는 HEAD 이해하기

> HEAD는 현재 작업 중인 브랜치 또는 커밋을 가리키는 포인터
> 
> 
> 즉, "지금 내가 어디서 작업하고 있는지"를 나타냄
> 

```bash
git log --oneline
git show HEAD
git show HEAD^
```

- `HEAD` → 현재 커밋
- `HEAD^` 또는 `HEAD~1` → 한 단계 전 커밋
- `HEAD@{1}` → 최근 이전 HEAD 위치 (`reflog`에서 확인 가능)

---

## 🧭 마지막 커밋의 브랜치 위치 파악하기

```bash
git branch --contains HEAD
```

- 현재 커밋(HEAD)을 포함하고 있는 브랜치 목록을 확인 가능
- 이 커밋이 **어떤 브랜치에서 만들어졌는지 확인**할 때 사용

---

## 🔀 브랜치 합치기 (Merge)

```bash
git switch main
git merge feature/login
```

- `main` 브랜치에 `feature/login` 브랜치의 변경사항을 **병합**
- 변경 이력이 **모두 보존됨**

---

## 🧬 Merge의 두 가지 방식

### ✅ 1. Fast-forward

- 브랜치가 일직선상일 때 자동으로 커밋이 이어짐
- 중간에 병합 커밋이 생성되지 않음

```bash
git merge feature --ff
```

### ✅ 2. 3-way Merge

- 브랜치가 병렬로 진행된 경우
- **공통 조상(commit)을 기준으로 병합 커밋**이 생성됨

```bash
git merge feature --no-ff
```

---

## ⚙️ Merge의 다양한 옵션

| 옵션 | 설명 |
| --- | --- |
| `--ff` | 가능하면 Fast-forward로 병합 (기본값) |
| `--no-ff` | 무조건 병합 커밋을 생성함 |
| `--squash` | 여러 커밋을 하나로 합쳐서 병합 (커밋은 따로 직접 해야 함) |

예시:

```bash
git merge feature --squash
git commit -m "기능 병합 완료"
```

---

## 🔁 브랜치 병합 (Rebase 방식)

```bash
git switch feature
git rebase main
```

> feature 브랜치를 main 위로 "붙이기"
> 
- 이력 흐름이 **깔끔하게 직선으로 정리됨**
- 협업 중인 브랜치에는 주의해서 사용
- 병합 대신 이력 정리를 원할 때 유용

## 🎯 핵심 차이 요약

| 항목 | `git reset --hard` | `git rebase` |
| --- | --- | --- |
| 목적 | 브랜치 상태를 특정 커밋으로 **되돌림** | 브랜치를 다른 커밋 위에 **재배치** |
| 이력 변경 여부 | ✅ 과거 이력을 덮어씀 | ✅ 이력 재작성 (새 커밋 생성) |
| 작업 내역 | ❌ 모두 삭제됨 (되돌릴 수 없음) | ✅ 변경 내용은 보존됨 |
| 위험도 | 높음 (삭제 주의) | 중간 (충돌 가능성 있음) |
| 협업 중 사용 | ❌ 공유 브랜치에서 사용 위험 | ⚠️ 협업 시 주의 필요 |
| 사용 예 | 실수로 만든 커밋 되돌리기 | 커밋 이력 깔끔하게 정리하기 |

---

## 🍒 특정 커밋만 가져오기 (Cherry-pick)

```bash
git switch main
git cherry-pick abc1234
```

- `abc1234` 커밋만 **현재 브랜치(main)** 에 복사해서 적용
- 필요한 기능만 선택적으로 가져올 수 있어 유용

---

## ✅ 정리 요약

| 개념 | 핵심 목적 |
| --- | --- |
| `HEAD` | 현재 커밋/위치 포인터 |
| `merge` | 브랜치 변경사항 병합 |
| `rebase` | 브랜치 이력을 재배치 |
| `cherry-pick` | 특정 커밋만 선택 반영 |
| `--ff`, `--no-ff` | 병합 방식 제어 |
| `--squash` | 여러 커밋을 하나로 압축 |