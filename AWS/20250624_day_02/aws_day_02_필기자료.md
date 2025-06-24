# AWS Day 02

담당자: 이현주
상태: 진행 중
마감일: 2025년 6월 24일
작성일: 2025년 6월 24일

# ✅ AWS 기초 학습

---

## 1. **리전(Region)**

- 서울 = `ap-northeast-2` 같이 물리적으로 분리된 **데이터 센터**
- 서비스 선택 시 **가장 가까운 리전 선택** → 지연시간 감소
- 리전 안에는 **가용 영역(AZ)** 존재 (ex. ap-northeast-2a, 2b)
    
    → 각 AZ는 독립된 네트워크로, 한 곳 장애 시 다른 AZ 영향 없음
    

---

## 2. **계정 (Root vs IAM) + MFA**

### 설명

- **Root 계정**: AWS 가입 시 만든 관리자 계정 (ex. 이메일 계정으로 노출)
    
    → 실사용 금지 권장
    
- **IAM 계정**: 일반 사용자용 계정 (ex. 닉네임@ 형식)
    
    → 별도로 생성해서 사용
    
- **MFA(다중 인증)**: OTP 앱을 이용한 2차 인증 (루트/IAM 사용자 모두 설정 가능)

> 보안을 위해 IAM 사용자에도 MFA 필수!
> 

---

### IAM과 IAM 사용자 차이

| 용어 | 설명 |
| --- | --- |
| **IAM** | AWS 리소스에 누가 어떤 권한 가지는지 관리하는 서비스 |
| **IAM 사용자** | 실제 로그인하거나 API 호출하는 계정 |

---

### IAM 구성요소

| 용어 | 설명 |
| --- | --- |
| 사용자(User) | 실제 사람 또는 시스템 계정 (로그인 가능) |
| 그룹(Group) | 사용자 묶음, 정책 일괄 적용 |
| 역할(Role) | 로그인하지 않는 서비스에 권한 위임 |
| 정책(Policy) | 권한 정의 파일 (JSON), 읽기/쓰기/삭제 등 제어 |

---

### 정책 형태

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::my-bucket",
      ]
    }
  ]
}
```

---

### ✅ IAM 사용자에 `AdministratorAccess` 권한 부여 실습

1. AWS 콘솔 > **IAM > 사용자** 이동
2. 권한 부여할 사용자 클릭
3. **[권한] 탭** 클릭 > **[권한 편집]** 클릭
4. **정책 직접 연결** 선택 > `AdministratorAccess` 검색 후 체크
5. 저장 후 권한 탭에서 `AdministratorAccess` 연결 확인

---

## 3. **S3**

### 설명

- 객체(Object) 저장용 스토리지 서비스
- **정적 웹 호스팅 가능** (ex. index.html)

---

### 정적 vs 동적 웹사이트 비교

| 항목 | 정적 웹사이트 | 동적 웹사이트 |
| --- | --- | --- |
| 페이지 구성 | HTML, CSS, JS | 데이터에 따라 실시간 내용 변경 |
| 백엔드 서버 | 불필요 | 필요 (PHP, Node.js 등) |
| DB 연동 | 불가능 | 가능 |
| 예시 | 블로그, 회사 소개 페이지 | 쇼핑몰, 게시판, 로그인 기능 |

---

### S3 버킷 생성 및 설정

1. AWS 콘솔 > S3 서비스 이동 > **버킷 생성** 클릭
2. 버킷 이름 입력 (유일하게 네이밍 필수, 소문자+숫자+하이픈만 가능)
3. 리전 선택 (ex. 서울 `ap-northeast-2`)
4. 퍼블릭 접근 차단 설정 단계에서
    - **기본 체크된 `모든 퍼블릭 액세스 차단` 해제**
    - 경고 팝업 확인 후 **확인** 클릭
5. 기본 옵션 유지 후 **버킷 생성**

> **AWS는 기본적으로 퍼블릭 차단을 권장하므로, 해제하지 않으면 객체 URL 접근 차단됨.**
> 

---

### S3 정적 웹 호스팅용 index.html 예시

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>S3 Web Hosting</title>
</head>
<body>
  <h1>Hello, S3 Web Hosting!</h1>
</body>
</html>
```

---

### index.html 업로드 후 접속

- S3 버킷에 `index.html` 업로드
- 정적 웹 호스팅 설정 후 나오는 URL로 접속 (예: `http://bucket-name.s3-website.ap-northeast-2.amazonaws.com`)
    
    ![image.png](AWS%20Day%2002%2021c66f3f3c5c8044bdc6fa0295415d0c/image.png)
    

---

## 8. **EC2 Ubuntu 생성**

- AMI 선택: Ubuntu
- 인스턴스 유형: `t2.micro` (프리 티어 가능)
- 키페어 생성(`.pem`), 보안 그룹 설정 후 시작

---

## 9. **.pem vs .ppk (Windows/macOS 접속용)**

| 확장자 | 설명 |
| --- | --- |
| `.pem` | 기본 키 파일, macOS에서 사용 |
| `.ppk` | Windows에서 Putty 접속 시 변환 필요 |
- macOS에서 `.pem` 권한 변경 명령

> public-ip는 AWS에서 생성한 EC2 정보탭에서 확인 가능
> 
> 
> ```bash
> chmod 400 key.pem
> ssh -i key.pem ubuntu@<public-ip>
> ```
> 

---

## 10. **보안 그룹(Security Group)**

- AWS 인스턴스 앞 가상 방화벽 역할
- **인바운드(Inbound)**: 들어오는 트래픽 허용 (ex. SSH, HTTP)
- **아웃바운드(Outbound)**: 나가는 트래픽 허용 (기본 모두 허용)

---

### 보안 그룹 설정 방법

1. AWS 콘솔 > EC2 > 네트워크 및 보안 > 보안 그룹 이동
2. **보안 그룹 생성** 클릭
3. 이름, 설명 입력 및 VPC 선택
4. 인바운드 규칙 추가
    - SSH(22/TCP), HTTP(80/TCP), HTTPS(443/TCP), MySQL(3306/TCP) 등
5. 아웃바운드 규칙 기본 확인 (모두 허용)
6. EC2 인스턴스 생성 시 또는 기존 인스턴스 선택 후 보안 그룹 연결

---

### 보안 그룹 인바운드 규칙 예시

> 아래 포트 정도는 외우자!
> 

| 포트 | 프로토콜 | 설명 |
| --- | --- | --- |
| 22 | TCP | SSH 접속용 |
| 80 | TCP | HTTP 웹서버 |
| 443 | TCP | HTTPS 웹서버 |
| 3306 | TCP | MySQL (RDS용) |

---