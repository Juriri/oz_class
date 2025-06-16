-- 1. PetOwner
CREATE TABLE PetOwners (
    ownerId INT AUTO_INCREMENT PRIMARY KEY COMMENT '고객 고유 ID',
    name VARCHAR(100) NOT NULL COMMENT '고객 이름',
    contact VARCHAR(50) COMMENT '고객 연락처'
);

-- 2. Pets
CREATE TABLE Pets (
    petId INT AUTO_INCREMENT PRIMARY KEY COMMENT '반려동물 고유 ID',
    ownerId INT NOT NULL COMMENT '소유자 ID',
    name VARCHAR(100) NOT NULL COMMENT '반려동물 이름',
    species VARCHAR(50) COMMENT '종 (예: 개, 고양이 등)',
    breed VARCHAR(100) COMMENT '품종',
    FOREIGN KEY (ownerId) REFERENCES PetOwners(ownerId)
        ON DELETE CASCADE
);

-- 3. Rooms
CREATE TABLE Rooms (
    roomId INT AUTO_INCREMENT PRIMARY KEY COMMENT '객실 고유 ID',
    roomNumber VARCHAR(20) NOT NULL COMMENT '객실 번호',
    roomType VARCHAR(50) COMMENT '객실 타입 (예: 스탠다드, 디럭스 등)',
    pricePerNight DECIMAL(10,2) COMMENT '1박당 가격'
);

-- 4. Reservations
CREATE TABLE Reservations (
    reservationID INT AUTO_INCREMENT PRIMARY KEY COMMENT '예약 고유 ID',
    petID INT NOT NULL COMMENT '예약된 반려동물 ID',
    roomID INT NOT NULL COMMENT '예약된 객실 ID',
    startDate DATE NOT NULL COMMENT '예약 시작 날짜',
    endDate DATE NOT NULL COMMENT '예약 종료 날짜',
    FOREIGN KEY (petID) REFERENCES Pets(petId)
        ON DELETE CASCADE,
    FOREIGN KEY (roomID) REFERENCES Rooms(roomId)
        ON DELETE CASCADE
);

-- 5. Services
CREATE TABLE Services (
    serviceID INT AUTO_INCREMENT PRIMARY KEY COMMENT '서비스 고유 ID',
    reservationID INT NOT NULL COMMENT '예약 ID',
    serviceName VARCHAR(100) COMMENT '서비스 이름 (예: 목욕, 산책 등)',
    servicePrice DECIMAL(10,2) COMMENT '서비스 가격 (예약 시점)',
    FOREIGN KEY (reservationID) REFERENCES Reservations(reservationID)
        ON DELETE CASCADE
);
