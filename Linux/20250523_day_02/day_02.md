# 리눅스 Day 02

담당자: 이현주
상태: 진행 중
마감일: 2025년 5월 23일
작성일: 2025년 5월 23일

## 📁 Linux 파일 시스템 기본

---

### 🧪 파일 생성

```bash
bash
복사편집
echo "hello world" > file.txt

```

- `file.txt`라는 **새 파일 생성**
- `"hello world"`라는 문자열이 해당 파일에 **저장됨**
- 기존에 `file.txt`가 있다면 **덮어쓰기**

---

### 📂 파일과 디렉토리 구분: `ls -F`

```bash
bash
복사편집
ls -F

```

- `ls` 명령에 `F` 옵션을 주면,
    
    → **파일/디렉토리/실행파일**을 기호로 구분해 보여줌
    

| 항목 | 예시 | 의미 |
| --- | --- | --- |
| `/` | `folder/` | 디렉토리 |
| `*` | `run.sh*` | 실행 가능한 파일 |
| (없음) | `file.txt` | 일반 파일 |

---

### 📄 출력 결과 저장

```bash
ls -F > list.txt
```

- `ls -F` 결과를 `list.txt` 파일에 저장
- 터미널에는 출력되지 않음

---

### 🔍 상세 정보 보기: `ls -l`

```bash
ls -l
```

→ 다음과 같은 형식으로 출력:

```bash
drwxr-xr-x  2 user group 4096 May 22 10:00 myfolder
-rw-r--r--  1 user group   12 May 22 10:01 file.txt
```

---

### 🔑 파일 모드 형식 해석 (예: `drwxr-xr-x`)

| 위치 | 의미 | 예시 |
| --- | --- | --- |
| 1 | 파일 유형 | `d` = 디렉토리, `-` = 파일 |
| 2–4 | 소유자 권한 | `rwx` = 읽기/쓰기/실행 |
| 5–7 | 그룹 권한 | `r-x` = 읽기/실행 |
| 8–10 | 기타 사용자 권한 | `r-x` = 읽기/실행 |

![image.png](%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%20Day%2002%201fc66f3f3c5c80208104e2f65c9b886d/image.png)

📌 예시:

```
drwxr-xr-x
```

- `d`: 디렉토리
- `rwx`: 소유자는 읽기/쓰기/실행 가능
- `r-x`: 그룹은 읽기/실행 가능
- `r-x`: 기타 사용자도 읽기/실행 가능

---

### 🧠 요약

| 명령어 | 설명 |
| --- | --- |
| `echo "text" > file.txt` | 파일 생성 및 텍스트 저장 |
| `ls -F` | 파일과 디렉토리 구분 |
| `ls -F > list.txt` | 결과를 파일로 저장 |
| `ls -l` | 파일/디렉토리의 상세 정보 확인 |

---

## 📂 디렉토리 이동 명령어 `cd` & 파일 보기 명령어 `ls -a`

---

### 📌 `cd` 명령어란?

> cd = change directory, 디렉토리(폴더)를 이동하는 명령어
> 

---

### ✅ 기본 사용법

```bash
cd [경로]
```

---

### 🔍 예제

| 명령어 | 설명 |
| --- | --- |
| `cd /` | 최상위 디렉토리(root)로 이동 |
| `cd /home/hyunju/Downloads` | 지정한 절대 경로로 이동 |
| `cd ~` | 내 홈 디렉토리로 이동 (예: `/home/hyunju`) |
| `cd ~/Downloads` | 내 홈 디렉토리 아래 `Downloads`로 이동 (상동) |

---

### 🏠 참고: `~` 기호

- `~`는 **현재 사용자 홈 디렉토리**를 의미
- 예를 들어 사용자 `hyunju`일 경우 `~ = /home/hyunju`

---

### 📄 숨김 파일까지 모두 보기: `ls -a`

```bash
ls -a
```

- 디렉토리 내 **모든 파일 및 폴더**를 표시
- `.` 또는 `..`과 같은 숨김 항목도 포함됨

| 파일 | 설명 |
| --- | --- |
| `.` | 현재 디렉토리 |
| `..` | 상위 디렉토리 |
| `.bashrc`, `.git` | 숨김 파일 또는 숨김 폴더 (이름이 `.`로 시작) |

---

### ✅ 예시 흐름

```bash
cd ~             # 홈 디렉토리로 이동
cd Downloads     # Downloads 폴더로 이동
ls -a            # 숨김 파일 포함 전체 목록 확인
```

---

### 🧠 요약

| 명령어 | 설명 |
| --- | --- |
| `cd /` | 루트 디렉토리로 이동 |
| `cd ~` | 홈 디렉토리로 이동 |
| `cd ~/Downloads` | 홈 디렉토리 아래 Downloads로 이동 |
| `ls -a` | 숨김 파일 포함 전체 파일 목록 출력 |

---

## 📁 리눅스에서의 **파일 확장자 & `file` 명령어**

---

### 📌 리눅스에서 확장자란?

> 리눅스에서는 파일 확장자(예: .jpg, .txt)가 필수적이거나 결정적이지 않음
> 
> 
> 시스템은 확장자가 아닌 **파일의 실제 내용(바이너리 시그니처)** 을 기준으로 파일 형식을 판단
> 

---

### 🔧 `file` 명령어란?

> file [파일명] 명령어는 해당 파일의 실제 내용 기반으로 타입을 추론함
> 

---

### ✅ 예시

```bash
file image.jpg
```

📄 출력 예시:

```
image.jpg: JPEG image data, ...
```

```bash
file image.png
```

📄 출력 예시:

```
image.png: PNG image data, ...
```

→ 확장자 없이도 이미지 포맷을 정확히 인식

---

### ❗ 확장자와 실제 형식이 다르면?

```bash
mv test.pdf test.txt
file test.txt
```

📄 출력 예시:

```
test.txt: PDF document, version 1.4
```

→ **파일 확장자와 무관하게 내부 형식(PDF)으로 판단함**

---

### 🧪 PDF와 텍스트 예시 비교

```bash
file sample.pdf
```

📄 출력:

```
sample.pdf: PDF document, version 1.4
```

```bash
file note.txt
```

📄 출력:

```
note.txt: ASCII text
```

→ 텍스트와 PDF는 실제 **포맷 정보가 다르게 출력**

하지만 경우에 따라 `file` 명령어가 정확히 판단하지 못하는 상황도 있으므로,

**확장자만 믿고 프로그램을 실행하면 오류 발생 가능**!

---

## 🧩 Wildcard (와일드카드)란?

> 리눅스에서 파일 이름 패턴을 지정해 검색하거나 작업할 때 사용되는 특수 문자
> 
> 
> `ls`, `cp`, `mv`, `rm` 등 다양한 명령어와 함께 사용 가능
> 

---

### 📁 기본 와일드카드 종류

| 패턴 | 의미 | 예시 |
| --- | --- | --- |
| `*` | **모든 문자 (0개 이상)** | `ls *` → 모든 파일/폴더 목록 |
| `?` | **임의의 한 문자** | `ls ?.txt` → `a.txt`, `1.txt` 등 한 글자 이름 |
| `[ ]` | **문자 클래스 지정** | `ls file[1-3].txt` → `file1.txt`, `file2.txt`, `file3.txt` |

---

### ✅ 예시로 배우는 Wildcard

### 🔹  (모든 문자)

```bash
ls *
```

- 현재 디렉토리의 모든 파일/폴더 출력

```bash
ls D*
```

- 이름이 `D`로 시작하는 파일/폴더만 출력

```bash
ls d*
```

- 소문자 `d`로 시작하는 파일/폴더
- ✅ **리눅스는 대소문자 구분함**

```bash
ls *.txt
```

- `.txt` 확장자를 가진 모든 파일 출력

---

### 🔹 `?` (한 글자 대체)

```bash
ls ?.txt
```

- 파일명이 **한 글자 + .txt**인 파일 (예: `a.txt`, `b.txt`)

```bash
ls file?.txt
```

- `file1.txt`, `fileA.txt` 등 **file + 1글자 + .txt**

```bash
ls file??.txt
```

- `file10.txt`, `fileAB.txt` 등 **file + 2글자 + .txt**

---

### 🔹 `[ ]` (특정 문자 or 범위 매칭)

```bash
ls file[123A].txt
```

- `file1.txt`, `file2.txt`, `file3.txt`, `fileA.txt` 중 존재하는 것만 출력

```bash
ls file[1-5].txt
```

- `file1.txt` ~ `file5.txt` 범위

```bash
ls file[a-z].txt
```

- `filea.txt`, `fileb.txt` 등 **소문자 a~z**

```bash
ls file[0-9][A-Z][a-z].txt
```

- 예: `file3Ba.txt`
    
    → **숫자 + 대문자 + 소문자** 조합으로 된 이름의 `.txt` 파일 찾기
    

---

### 🧠 요약 비교

| 패턴 | 설명 | 예시 |
| --- | --- | --- |
| `*` | 모든 문자 (0글자 이상) | `ls *.txt` |
| `?` | 임의의 한 문자 | `ls ?.txt` |
| `[abc]` | a, b, c 중 하나 | `ls file[abc].txt` |
| `[1-3]` | 숫자 1~3 중 하나 | `ls file[1-3].txt` |
| `[A-Z]` | 대문자 A~Z | `ls file[A-Z].txt` |

---

## 📁 파일 & 폴더 생성 명령어 정리

---

### 📝 `touch` — **빈 파일 생성**

```bash
touch file9
```

- `file9` 이라는 **빈 파일 생성**
- 이미 존재하면 **수정 시간만 업데이트됨**
- 확장자 없이도 파일 생성 가능

---

### 📂 `mkdir` — **디렉토리(폴더) 생성**

```bash
mkdir folder
```

- `folder`라는 **폴더 생성**

```bash
mkdir "a_b_c"
```

- 이름에 **언더스코어 포함된 폴더** 생성

---

### 📌 `p` 옵션 — 상위 디렉토리가 없을 경우 함께 생성

```bash
mkdir -p folder3/folder4
```

- `folder3`가 없더라도 자동으로 생성한 뒤, 그 안에 `folder4`까지 생성
    
    ✅ 중첩 폴더 구조 만들 때 필수 옵션
    

---

### 🧠 요약

| 명령어 | 설명 |
| --- | --- |
| `touch file` | 빈 파일 생성 |
| `mkdir folder` | 폴더 생성 |
| `mkdir -p a/b/c` | 중첩 폴더 구조 생성 (상위 폴더 없을 시 자동 생성) |
| `mkdir "a_b_c"` | 이름에 `_` 포함된 폴더 생성 |

---

## 📦 여러 파일·폴더 한 번에 생성하기

리눅스에서는 **중괄호 확장(Brace Expansion)** 기능을 활용해

여러 개의 디렉토리 및 파일을 **한 줄 명령어로** 생성할 수 있습니다.

---

### 📁 Step 1: 기본 디렉토리 생성

```bash
mkdir challenge1
cd challenge1
```

- `challenge1` 디렉토리를 만들고 이동

---

### 📂 Step 2: 연도 & 월별 디렉토리 한꺼번에 생성

```bash
mkdir {jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec}_{2024,2025,2026}
```

🔹 결과:

`jan_2024`, `feb_2025`, `dec_2026` 등 **36개의 디렉토리** 생성

✅ 쉼표(`,`)와 중괄호(`{}`)로 조합 가능

✅ 연도 또는 월 순서에 상관없이 자유롭게 조합 가능

---

### 📝 Step 3: 각 디렉토리에 100개의 파일 만들기

```bash
touch {jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec}_{2024..2025}/file{1..100}
```

- `2024`, `2025`년도 각 월별 폴더에 `file1 ~ file100` 생성
    
    (예: `jan_2024/file1`, `mar_2025/file100`)
    

🔸 범위(`..`) 표기법으로 연속된 숫자/문자 사용 가능

🔸 **중첩 확장**을 통해 디렉토리 안에 여러 파일도 한 번에 생성 가능

### ✅ 요약

| 명령어 | 설명 |
| --- | --- |
| `mkdir {a,b,c}` | 여러 폴더 생성 |
| `mkdir a_{1..3}` | 숫자 확장 |
| `touch a_{2023..2025}/file{1..10}` | 하위 폴더 내 다중 파일 생성 |

---

## 🗑️ 파일 삭제 명령어 `rm`

### ✅ 기본 사용법

```bash
rm [옵션] [파일명]
```

- 파일이나 디렉토리를 **삭제**하는 명령어
- 삭제 후 복구 불가 ❗ → 신중하게 사용

---

## 📌 예제 1: 단일 파일 삭제

```bash
rm delete.txt
```

> 현재 디렉토리에 있는 delete.txt 파일 삭제
> 

---

## 📌 예제 2: 경로를 이용한 삭제

```bash
touch ~/Documents/delete.txt     # 파일 생성
cd ~/Documents/                 # 디렉토리 이동
rm ~/Documents/delete.txt       # 파일 삭제
```

> 경로를 지정하면 어느 위치에 있든 해당 파일을 삭제할 수 있음
> 

---

## 🔎 와일드카드(*) 활용한 삭제

### 📌 `2`

```bash
rm *2
```

- **이름이 `2`로 끝나는 파일** 삭제
    
    예: `file2`, `test2` 등
    

---

### 📌 `2*`

```bash
rm * 2*
```

- 공백 포함 후 `2`로 시작하는 파일 삭제
    
    예: `"log 2.txt"` 등
    

---

### 📌 `[1-3]*`

```bash
rm *[1-3]*
```

- **이름에 1~3 숫자가 포함된 모든 파일** 삭제
    
    예: `file1.txt`, `log2.csv`, `report3.docx`
    

---

## 🚫 주의사항

- `rm`은 삭제된 파일을 **휴지통으로 보내지 않고 바로 제거**합니다.
- 실수로 중요한 파일을 지웠다면 복구가 **매우 어렵습니다**.

---

## 🛡️ 안전하게 삭제하려면?

```bash
rm -i filename
```

- `i` 옵션은 **삭제 전 사용자에게 확인**을 요청합니다.

```bash
rm -r folder/
```

- 폴더와 내부 파일까지 삭제하려면 `r` (recursive) 옵션 필요

---

### ✅ 요약

| 명령어 | 설명 |
| --- | --- |
| `rm file.txt` | 단일 파일 삭제 |
| `rm *2` | 이름이 2로 끝나는 파일 삭제 |
| `rm *[1-3]*` | 이름에 1~3 포함된 파일 삭제 |
| `rm -i file.txt` | 삭제 전 확인 |
| `rm -r folder/` | 디렉토리 전체 삭제 |

---

## 📄 파일/폴더 복사 명령어 `cp`

### ✅ 기본 사용법

```bash
cp [옵션] 원본 대상
```

- **파일이나 디렉토리를 복사**할 때 사용

---

## 📁 예제 1: 파일 복사

```bash
cp file1.txt file2.txt destination/
```

- `file1.txt`, `file2.txt`를 `destination/` 폴더로 복사

---

## 🗑️ 삭제 후 확인

```bash
rm file*
```

- `file`로 시작하는 파일들 삭제
- 이후 `destination/` 폴더에 복사된 파일들이 남아 있는지 확인

---

## 📁 예제 2: 디렉토리 복사

### 1️⃣ 디렉토리와 파일 생성

```bash
mkdir copyfolder
touch copyfolder/file{1..3}.txt
```

- `copyfolder/` 디렉토리 생성
- 그 안에 `file1.txt`, `file2.txt`, `file3.txt` 생성

---

### 2️⃣ `r` 옵션으로 폴더 복사

```bash
cp -r copyfolder/ destination/
```

- `copyfolder` 폴더 전체를 `destination/` 폴더로 복사
- `r` (recursive): 디렉토리와 그 내부 내용까지 모두 복사할 때 필요

---

### ✅ 요약

| 명령어 | 설명 |
| --- | --- |
| `cp file.txt backup/` | 파일을 다른 폴더로 복사 |
| `cp file1.txt file2.txt dest/` | 여러 파일을 한 폴더에 복사 |
| `cp -r folder/ backup/` | 폴더 전체 복사 |
| `cp -i file.txt dest/` | 덮어쓰기 전 확인 |

---

## 📦 파일 및 디렉토리 이동/이름 변경: `mv` 명령어

### ✅ 기본 사용법

```bash
mv [원본] [대상]
```

- **파일이나 디렉토리를 이동**하거나 **이름을 변경**할 때 사용

---

## 🔧 예제 정리

### 📁 1. 파일 생성 및 이동

```bash
touch newfolder/file{1..3}.txt
```

- `newfolder/` 폴더 안에 `file1.txt`, `file2.txt`, `file3.txt` 생성

---

### 📤 2. 폴더 안의 파일을 현재 디렉토리로 이동

```bash
mv newfolder/* .
```

- `newfolder` 폴더에 있는 **모든 파일**을 **현재 디렉토리로 이동**

---

### 📥 3. 다시 해당 파일들을 폴더로 이동

```bash
mv file* newfolder/
```

- 현재 디렉토리에 있는 `file`로 시작하는 파일들을 `newfolder`로 다시 이동

---

### 📂 4. 폴더 전체를 다른 경로로 이동

```bash
mv newfolder/ ~/Documents/
```

- `newfolder`를 사용자의 `Documents` 디렉토리로 이동

---

### ✏️ 5. 폴더 이름 변경 (이동하면서 이름 바꾸기)

```bash
mv ~/Documents/newfolder/ ./newnamedfolder
```

- `~/Documents/newfolder`를 현재 디렉토리(`./`)로 옮기면서 이름을 `newnamedfolder`로 변경

---

### ✅ 요약 정리

| 명령어 | 설명 |
| --- | --- |
| `mv file.txt folder/` | 파일을 폴더로 이동 |
| `mv old.txt new.txt` | 파일 이름 변경 |
| `mv dir1/ ~/Documents/` | 폴더를 홈의 Documents로 이동 |
| `mv ~/dir1 ./renamed_dir` | 폴더를 현재 경로로 이동하고 이름 변경 |

---

💡 **Tip:**

`mv` 명령어는 **이동**뿐 아니라 **이름 변경**도 가능하므로 매우 자주 사용되는 유틸리티입니다!

---

# ✏️ `nano` 명령어로 파일 편집하기

`nano`는 리눅스/유닉스에서 간편하게 사용할 수 있는 **터미널 기반 텍스트 편집기**입니다.

가볍고 직관적이며, 기본 단축키만 알아도 실무에 충분히 활용할 수 있습니다.

---

## 🧭 기본 실행

```bash
nano 파일명
```

- 해당 파일이 열림
- 파일이 없으면 새로 생성

---

## 🧰 자주 쓰는 단축키 (Ctrl = `^`로 표시됨)

| 단축키 | 기능 | 설명 |
| --- | --- | --- |
| `^O` (Ctrl + O) | **파일 저장 (Write Out)** | 저장 시 파일명 입력 가능 |
| `^X` (Ctrl + X) | **nano 종료** | 저장 여부 묻는 메시지 표시 |
| `^R` (Ctrl + R) | **다른 파일 내용 불러오기 (Insert)** | 현재 커서 위치에 다른 파일 삽입 |
| `^\` (Ctrl + ) | **문자열 찾고 바꾸기 (Replace)** | 검색어 입력 → 교체할 단어 입력 |
| `^W` (Ctrl + W) | **문자열 검색 (Where Is)** | 검색어로 텍스트 찾기 |
| `^K` (Ctrl + K) | **라인 잘라내기 (Cut)** | 현재 줄 삭제 (잘라내기) |
| `^U` (Ctrl + U) | **붙여넣기 (Uncut)** | 직전에 잘라낸 줄 붙여넣기 |
| `^J` (Ctrl + J) | **줄 맞춤 (Justify)** | 문단 정렬 |
| `^G` (Ctrl + G) | **도움말 표시** | nano 단축키 도움말 페이지 표시 |

---

## 📌 실무에서 자주 활용되는 사용 패턴

### ✅ 다른 파일 내용 불러오기

```bash
^R → 파일명 입력 → Enter
```

- 현재 열려있는 파일에 다른 파일의 내용을 **추가 삽입**할 수 있음

---

### ✅ 문자열 교체 (Replace)

```bash
^\ → 바꿀 단어 입력 → Enter → 교체할 단어 입력
```

- 문서 전체에서 문자열을 **찾아 바꾸기** 가능
- `Y` → 바꾸기, `N` → 건너뛰기

---

### ✅ 여러 줄 편집

- 여러 줄 삭제: `^K` 반복
- 붙여넣기: `^U`

---

## ✅ 저장 없이 나가기

- 실수로 변경했을 때 저장하지 않고 종료하고 싶다면:
    
    ```bash
    ^X → N
    ```
    

---

# 📍 `locate` 명령어 정리

`locate`는 **파일명을 빠르게 검색**할 수 있는 명령어입니다.

파일 시스템 전체를 실시간으로 스캔하지 않고, **미리 만들어진 데이터베이스**에서 검색하므로 매우 빠릅니다.

---

## 🧭 기본 사용법

```bash
locate [옵션] 검색어
```

---

## 📌 예제

### ✅ `.conf` 확장자 파일 찾기

```bash
locate *.conf
```

- `.conf`로 끝나는 모든 파일 목록 출력

---

### ❗ 대소문자 구분

```bash
locate *.CONF
```

- 대문자 확장자만 검색됨 (기본은 **대소문자 구분**)

### ✅ 대소문자 구분 없이 검색

```bash
locate -i *.conf
```

- `i` 옵션으로 대소문자 무시하고 검색

---

## 🔍 검색 개수 제한하기

```bash
locate -i --limit 3 *.conf
```

- 최대 3개 결과만 출력
    
    (※ 일부 시스템에서는 `--limit` 대신 `-n` 옵션 사용)
    

---

## 🧪 실습 예시

```bash
touch findme.txt
locate findme.txt
```

- `findme.txt` 파일 생성 후, `locate`로 검색해도 **바로는 결과가 안 나올 수 있음**

```bash
sudo updatedb
locate findme.txt
```

- `updatedb` 명령어로 **데이터베이스를 갱신한 후** 다시 `locate` → 이제 검색 가능

---

## 🚨 주의 사항

| 항목 | 설명 |
| --- | --- |
| `locate` 속도 | 매우 빠름 (DB 기반) |
| 검색 기준 | **파일명** 기준 |
| 실시간 반영 안 됨 | **최근 생성 파일은 안 보일 수 있음** |
| 해결 방법 | `sudo updatedb`로 DB 갱신 |

---

## ✅ 실전 Tip

- 자주 사용하는 설정 파일 찾기:
    
    ```bash
    locate -i bashrc
    locate -i nginx.conf
    ```
    
- 실수로 파일 이름이 기억 안 날 때 유용:
    
    ```bash
    locate -i report
    ```
    
- `find`는 느리지만 정확하고, `locate`는 빠르지만 최신 파일은 못 찾을 수 있음

---

# 🔍 `find` 명령어 정리

`find`는 디렉토리 트리에서 조건에 맞는 **파일이나 디렉토리를 검색**하는 명령어입니다.

`locate`와 달리 실시간으로 파일 시스템을 검색하므로 **최신 파일도 검색 가능**하지만 상대적으로 느립니다.

---

## 📌 기본 사용법

```bash
find [검색 시작 경로] [옵션] [조건]
```

---

## ✅ 예제

### 1️⃣ `/challenge` 디렉토리 안에서 모든 파일 찾기

```bash
find /challenge
```

- `/challenge` 디렉토리 내부의 모든 파일과 폴더 출력

---

### 2️⃣ 특정 이름의 파일 찾기

```bash
touch ~/Desktop/hello123.txt
find ~/Desktop -name "hello123.txt"
```

- `~/Desktop` 경로 아래에서 이름이 **정확히 `hello123.txt`인 파일** 검색

---

### 3️⃣ `locate`와 비교

```bash
locate hello123.txt
```

- `locate`는 **이전에 데이터베이스에 등록된 파일**만 검색됨
- `updatedb`를 하지 않으면 방금 만든 파일은 검색되지 않음

```bash
find ~/Desktop -name "hello123.txt"
```

- `find`는 실시간으로 검색하므로 **방금 만든 파일도 검색 가능**

---

## ⚠️ 주의: 오타 예시

```bash
find hello123,txt
```

- 쉼표 `,`는 잘못된 문법 → `No such file or directory` 에러 발생
- 올바른 문법:
    
    ```bash
    find . -name "hello123.txt"
    ```
    

---

## 🧠 요약 비교

| 항목 | `locate` | `find` |
| --- | --- | --- |
| 🔄 실시간 검색 | ❌ 아님 (DB 기반) | ✅ 가능 |
| ⚡ 속도 | 빠름 | 느릴 수 있음 |
| 📁 검색 대상 | DB에 있는 파일명 | 실제 파일 시스템 |
| 🧹 최신 파일 검색 | ❌ (updatedb 필요) | ✅ 가능 |
| 📚 주요 옵션 | `-i`, `--limit` | `-name`, `-type`, `-size`, `-mtime` 등 다양 |

---

## 💡 자주 쓰는 `find` 옵션

| 옵션 | 설명 |
| --- | --- |
| `-name "파일명"` | 정확한 이름으로 검색 |
| `-iname` | 대소문자 구분 없이 이름 검색 |
| `-type f` | 파일만 검색 |
| `-type d` | 디렉토리만 검색 |
| `-size +10M` | 10MB보다 큰 파일 검색 |
| `-mtime -1` | 24시간 이내 수정된 파일 검색 |