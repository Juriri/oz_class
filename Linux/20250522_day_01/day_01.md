# 리눅스 Day 01

담당자: 이현주
상태: 완료
마감일: 2025년 5월 22일
작성일: 2025년 5월 22일

# 🐧 Linux 명령어 요약 정리

## 1️⃣ 타임존 변경 (UTC ➡️ KST)

### 🔧 방법 A: `timedatectl` 명령어 사용

```bash
sudo timedatectl set-timezone Asia/Seoul
```

### 🔧 방법 B: 심볼릭 링크로 직접 설정

```bash
sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
```

| 구성 요소 | 설명 |
| --- | --- |
| `ln` | 링크(link)를 만드는 명령어 |
| `-s` | 심볼릭 링크(symbolic link) 생성 (바로가기) |
| `-f` | 기존 파일이 있을 경우 강제로 덮어쓰기 |
| `/usr/share/zoneinfo/Asia/Seoul` | 한국 시간대 정보가 들어 있는 파일 |
| `/etc/localtime` | 시스템이 사용하는 현재 시간대 설정 파일 |

---

## 2️⃣ 달력 및 시간 확인

### 📅 달력 확인

```bash
cal 12 2023           # 12월 달력
cal -A 1 12 2023      # 12월 + 이후 1개월
cal -A 1 -B 1 12 2023 # 11월, 12월, 1월
```

### 🕒 현재 시간 확인

```bash
date        # 현재 시간 (시스템 기준)
date -u     # UTC 시간
```

---

## 3️⃣ 폴더 위치 확인

```bash
echo $PATH      # 실행 가능한 경로 리스트
which <명령어>  # 해당 명령어의 실행 파일 경로 확인
```

예시:

```bash
which node
which python3
```

---

## 4️⃣ 이전 명령어 확인

```bash
history      # 명령어 히스토리 출력
!!           # 직전 명령어 다시 실행
!3           # history 3번 명령어 실행
```

---

## 5️⃣ 대소문자 구분

- **리눅스는 기본적으로 대소문자를 구분(case sensitive)** 합니다.
- `file.txt` 와 `File.txt` 는 완전히 **다른 파일**로 인식합니다.
- 경로(`/`로 구분)도 대소문자에 민감합니다.

---

# 📚 리눅스 명령어 학습 정리 - `man`, `which`, `ls`

---

## 📘 1. `man` 명령어

> 명령어의 설명서(매뉴얼 페이지) 를 보여주는 명령어입니다.
> 

### 📌 기본 사용법

```bash
man [명령어]
```

예:

```bash
man ls
```

### 📌 섹션 번호 지정

```bash
man [섹션번호] [명령어]
```

예:

```bash
man 1 which
```

- `man 1 which` → **1번 섹션 (사용자 명령어)** 에 있는 `which` 설명서 표시

---

## 🔎 `man` 섹션 종류

| 번호 | 설명 |
| --- | --- |
| 1 | 사용자 명령어 |
| 2 | 시스템 호출 |
| 3 | C 라이브러리 함수 |
| 4 | 디바이스 및 드라이버 설명 |
| 5 | 설정 파일 형식 |
| 8 | 관리자 명령어 (root 등) |

---

## 🔍 2. `man -k`: 관련 명령어 검색

```bash
man -k [키워드]
```

예:

```bash
man -k content
```

> contents라는 키워드를 포함한 모든 man 페이지 항목 검색
> 
> 
> → 결과에 `ls`, `tar`, `cat` 등 다양한 명령어가 나올 수 있음
> 

---

## ✅ 3. `which` 명령어

```bash
which [명령어]
```

> 명령어의 실행 파일 경로를 출력합니다.
> 

예:

```bash
which echo
which whic
```

| 입력 | 출력 예시 |
| --- | --- |
| `which echo` | `/bin/echo` |
| `which which` | `/usr/bin/which` |

---

## 📁 4. 메뉴얼을 통해 명령어 찾기

> 사용하고 싶은 기능 또는 키워드를 알고 있을 때는 man -k 또는 apropos 명령어를 사용합니다.
> 

```bash
man -k list
```

→ list라는 키워드가 포함된 명령어들을 보여줍니다.

---

## 📂 5. `ls` 명령어 및 옵션 예시

```bash
ls -l
```

| 옵션 | 설명 |
| --- | --- |
| `-l` | 긴 형식으로 목록 보기 (파일 정보 포함) |
| `-h` | 사람이 읽기 쉬운 크기(KB, MB)로 출력 (human-readable) |

예시 출력:

```
-rw-r--r-- 1 user user 1.2K May 22 10:30 file.txt
```

---

## 🎯 빠른 요약

| 명령어 | 설명 |
| --- | --- |
| `man [명령어]` | 매뉴얼 보기 |
| `man 1 which` | 섹션 1에서 `which` 설명 보기 |
| `man -k [키워드]` | 키워드 관련 명령어 검색 |
| `which [명령어]` | 명령어의 실제 실행 경로 확인 |
| `ls -lh` |  |

---

# 🐱 `cat` 명령어 + 출력 리디렉션 정리

---

## ✅ 기본 사용법

```bash
cat [옵션] [파일명]
```

📌 예시:

```bash

cat output.txt
```

→ `output.txt`의 내용을 터미널에 출력

```bash
cat file1.txt file2.txt
```

→ 두 파일의 내용을 연결해서 출력

---

## 🔁 출력 리디렉션: `1>`, `>`, `>>`

### 📌 `1> output.txt`

```bash
cat file.txt 1> output.txt
```

- **표준 출력(stdout)** 을 `output.txt`로 보냄
- 기존 파일은 **덮어쓰기**

---

### 📌 단순화된 표현: `>`

```bash
cat file.txt > output.txt
```

- 위 명령과 동일 (숫자 `1` 생략 가능)

---

### 📌 `>>` (추가 저장)

```bash
cat file.txt >> output.txt
```

- 기존 내용은 유지하고 **뒤에 이어서 저장**

---

## ❗ 에러 리디렉션: `2>`, `2>>`

| 구문 | 설명 |
| --- | --- |
| `2>` | **표준 에러(stderr)**를 파일로 저장 (**덮어쓰기**) |
| `2>>` | **표준 에러(stderr)**를 파일에 추가 (**append**) |

---

### ✅ 예제 1: 에러 메시지 저장

```bash
cat -k adosfiajnf 2> error.txt
```

- `k`: 존재하지 않는 옵션
- `adosfiajnf`: 존재하지 않는 파일
    
    → 에러 발생 → `error.txt`에 저장
    

📄 `error.txt` 내용 예시:

```
cat: invalid option -- 'k'
Try 'cat --help' for more information.
```

---

### ✅ 예제 2: 에러 메시지 추가 저장

```bash
cat -z hello.txt 2>> error.txt
```

- 기존 `error.txt` 유지
- 에러 메시지를 **뒤에 추가**

---

## 🔀 출력 & 에러 동시 저장

```bash
cat file1.txt file2.txt &> all.txt
```

- **표준 출력 + 에러**를 동시에 `all.txt`에 저장

---

## 🧪 리디렉션 요약표

| 구문 | 의미 |
| --- | --- |
| `>` 또는 `1>` | 표준 출력 저장 (덮어쓰기) |
| `>>` | 표준 출력 추가 저장 |
| `2>` | 표준 에러 저장 (덮어쓰기) |
| `2>>` | 표준 에러 추가 저장 |
| `&>` | 출력 + 에러 모두 저장 |

---

## ✅ 표준 입력 리디렉션: `0<`

```bash
cat 0< input.txt
```

- `0<`는 **표준 입력(stdin)** 을 `input.txt`에서 받겠다는 의미
- 결과적으로 `cat input.txt`와 동일한 동작

---

📌 참고: 표준 입출력 파일 디스크립터

| 이름 | 번호 | 설명 |
| --- | --- | --- |
| `stdin` | `0` | 표준 입력 (키보드 입력 등) |
| `stdout` | `1` | 표준 출력 (터미널 출력 등) |
| `stderr` | `2` | 표준 에러 출력 (오류 메시지) |

---

# 🔗 Piping (`|`) + `cut` 명령어 정리

---

## ✅ Piping (`|`) 이란?

- **파이프**(`|`)는 한 명령어의 출력을 다음 명령어의 입력으로 전달하는 기능입니다.

```bash
command1 | command2
```

예:

```bash
date | cut -d " " -f 1
```

→ `date` 명령어의 결과에서 첫 번째 필드만 추출

---

## 🛠 `cut` 명령어 기본 형식

```bash
cut -d [구분자] -f [필드번호]
```

| 옵션 | 의미 |
| --- | --- |
| `-d` 또는 `--delimiter` | 필드를 나누는 구분자 설정 |
| `-f` 또는 `--fields` | 출력할 필드 번호 지정 (1부터 시작) |

---

## 📌 실습 예제

### ✅ 예제 1: `date` 결과를 파일로 저장 후 `cut` 사용

```bash
date 1> date.txt
cut -d " " -f 1 < date.txt
```

- `date`의 출력을 `date.txt`에 저장
- `cut`으로 첫 번째 필드(예: 요일)만 출력

---

### ✅ 예제 2: 파이프를 사용해 한 줄로 처리

```bash
date | cut -d " " -f 1
```

- `date` 명령 결과를 직접 `cut`으로 전달
- 파일 없이 한 줄로 처리 가능 ✅

---

### ✅ 예제 3: 결과를 파일에 저장

```bash
date | cut -d " " -f 1 > today.txt
```

- 요일 정보를 추출하고 `today.txt`에 저장

---

Tee 명령어

date | tee date.txt | cut —delimiter=” “ —field=1

# 🧵 `tee` 명령어란?

## ✅ 기본 개념

> tee는 표준 입력을 받아 파일에 저장하면서, 동시에 표준 출력으로도 보내는 명령어입니다.
> 

### 📌 형식

```bash
command1 | tee file.txt | command2
```

- `command1`의 출력 👉 `file.txt`에 저장
- 동시에 `command2`로도 **파이프 전달**

## 🎯 예시로 이해하기

```bash
date | tee date.txt | cut --delimiter=" " --field=1 > today.txt
```

### 1️⃣ `date`

```
Thu May 22 14:00:00 KST 2025
```

### 2️⃣ `tee date.txt`

- 위 출력을 **`date.txt`에 저장**
- 동시에 **다음 명령어(`cut`)로 전달**

### 3️⃣ `cut --delimiter=" " --field=1`

- 전달된 문자열에서 공백 기준으로 **첫 번째 필드 추출 → `Thu`  → today.txt 파일에 저장**

---

# 🧰 `xargs` 명령어 정리

## ✅ `xargs`란?

> 표준 입력(stdin) 으로 받은 데이터를 명령어의 인자(argument) 로 변환해서 실행하는 명령어입니다.
> 
- 일반적인 파이프 `|`는 **표준 입력**으로 다음 명령어에 전달
- `xargs`는 입력을 받아서 **명령어 뒤에 인자로 붙여 실행**

---

## 📌 차이 비교

| 예제 | 설명 |
| --- | --- |
| `date | echo` | `echo`는 stdin을 받지 않기 때문에 **출력 없음** |
| `date | xargs echo` | `date`의 결과가 `echo`에 **인자로 전달**되어 출력됨 |

```bash
date
# 출력: Thu May 22 14:00:00 KST 2025

date | echo
# 출력: (없음)

date | xargs echo
# 출력: Thu May 22 14:00:00 KST 2025
```

---

## ✅ 응용 예시

### 🔹 `cut`과 함께 사용

```bash
date | cut --delimiter=" " --fields=1 | xargs echo
```

- `cut` 결과 (`Thu`)를 `echo`의 **인자로 전달**해서 출력
- 반면, `cut ... | echo`는 **출력 없음** (이유: `echo`는 인자만 출력)

---

## 🗑️ 파일 삭제 예시

### 🚫 잘못된 예시

```bash
cat file.txt | rm
```

- `rm`은 **표준 입력을 인자로 인식하지 않음** → 에러 발생

### ✅ `xargs` 사용

```bash
cat file.txt | xargs rm
```

- `file.txt`에 적힌 파일 이름들을 `rm`의 인자로 전달 → 정상 삭제

예:

```
date.txt
today.tx
```

위 파일들을 한 번에 삭제함.

---

## 🔁 명령어 조합 예시

```bash
commandA | commandB | tee snapshot.txt | command
```

- `commandB`가 **입력을 인자로 받아야 한다면**, 그냥 파이프 `|`로는 안 됨
- 이럴 땐 이렇게 바꿔야 함:

```bash
commandA | xargs commandB
```

---

## 🧠 요약 정리

| 구조 | 의미 |
| --- | --- |
| `commandA | commandB` |
| `commandA | xargs commandB` |
| `xargs` | 입력 → 인자(argument)로 바꾸는 중간 처리 도구 |

## ✅ 핵심 차이 요약

| 항목 | `tee` | `xargs` |
| --- | --- | --- |
| 역할 | 데이터를 **중간에 저장하고 넘김** | 데이터를 **명령어의 인자(argument)** 로 전달 |
| 데이터 흐름 | **표준 입력 → 파일 저장 + 다음 명령어로 전달** | **표준 입력 → 인자로 변환해서 실행** |
| 사용 목적 | 출력 내용을 **보면서 동시에 저장** | 입력값을 **명령어에 인자로 넘김** |
| 동작 방식 | **출력을 복제** | **인자를 재구성** |

---

# 🧩 Aliases (별칭) 정리

### 📝 Aliases란?

- 자주 사용하는 **긴 명령어를 짧은 이름으로 저장**하는 기능
- 터미널에서 반복되는 작업을 간편하게!

---

### 🧪 기본 사용법

```bash
alias [별칭이름]='[실제 명령어]'
```

### 📌 예시:

```bash
alias ll='ls -alF'
```

> 이제 ll만 입력해도 ls -alF가 실행됩니다.
> 

---

## 🔧 실전 예제: `getdates`

```bash
alias getdates='date | tee ~/date.txt | cut --delimiter=" " --fields=1 | tee ~/shortdate.txt | xargs echo hello'
```

---

### 📂 동작 순서

| 단계 | 설명 |
| --- | --- |
| 1️⃣ `date` | 현재 날짜 출력 |
| 2️⃣ `tee ~/date.txt` | 날짜를 `date.txt`에 저장하고 다음 명령으로 전달 |
| 3️⃣ `cut` | 공백 기준 첫 번째 필드 (요일) 추출 |
| 4️⃣ `tee ~/shortdate.txt` | 요일을 `shortdate.txt`에 저장 |
| 5️⃣ `xargs echo hello` | 결과 요일을 인자로 받아 `hello 요일` 출력 |

---

### ✅ 실행 예시

```bash
getdates
```

📤 출력:

```
hello Thu
```

📄 파일 생성:

- `~/date.txt`: 전체 날짜 (예: Thu May 22 14:10:00 KST 2025)
- `~/shortdate.txt`: 요일만 (예: Thu)

---

### 🧹 alias 삭제 방법

```bash
unalias getdates
```