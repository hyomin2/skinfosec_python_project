-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        8.0.22 - MySQL Community Server - GPL
-- 서버 OS:                        Linux
-- HeidiSQL 버전:                  11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- hyomin_db 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `hyomin_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hyomin_db`;

-- 테이블 hyomin_db.item 구조 내보내기
CREATE TABLE IF NOT EXISTS `item` (
  `icode` int NOT NULL AUTO_INCREMENT,
  `iname` varchar(100) NOT NULL,
  `iprice` int NOT NULL,
  `iqty` int NOT NULL,
  `i_date` varchar(50) NOT NULL,
  PRIMARY KEY (`icode`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='상품 테이블';

-- 테이블 데이터 hyomin_db.item:~3 rows (대략적) 내보내기
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT IGNORE INTO `item` (`icode`, `iname`, `iprice`, `iqty`, `i_date`) VALUES
	(1, 'apple', 4000, 47, '2021-01-12'),
	(3, 'iphone', 50000, 7, '2021-01-13'),
	(4, 'bag', 12000, 35, '2021-01-13');
/*!40000 ALTER TABLE `item` ENABLE KEYS */;

-- 테이블 hyomin_db.item_order 구조 내보내기
CREATE TABLE IF NOT EXISTS `item_order` (
  `ocode` int NOT NULL AUTO_INCREMENT,
  `id` varchar(100) NOT NULL,
  `order_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `icode` int NOT NULL,
  `iname` varchar(100) NOT NULL,
  `iprice` int NOT NULL,
  `order_qty` int NOT NULL,
  `order_price` int NOT NULL,
  `order_date` varchar(100) NOT NULL,
  PRIMARY KEY (`ocode`),
  KEY `FK_order_id` (`id`),
  CONSTRAINT `FK_order_id` FOREIGN KEY (`id`) REFERENCES `member` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='주문 테이블';

-- 테이블 데이터 hyomin_db.item_order:~8 rows (대략적) 내보내기
/*!40000 ALTER TABLE `item_order` DISABLE KEYS */;
INSERT IGNORE INTO `item_order` (`ocode`, `id`, `order_name`, `icode`, `iname`, `iprice`, `order_qty`, `order_price`, `order_date`) VALUES
	(1, 'test1', 'tester1', 1, 'apple', 3000, 2, 6000, '2021-01-13'),
	(2, 'test1', 'tester1', 1, 'apple', 3000, 5, 15000, '2021-01-13'),
	(3, 'test2', 'tester2', 1, 'apple', 3000, 3, 9000, '2021-01-13'),
	(4, 'test2', 'tester2', 3, 'iphone', 50000, 2, 100000, '2021-01-13'),
	(5, 'test2', 'tester2', 4, 'bag', 12000, 3, 36000, '2021-02-13'),
	(6, 'test1', 'tester1', 4, 'bag', 12000, 2, 24000, '2021-02-13'),
	(7, 'test1', 'tester1', 1, 'apple', 4000, 3, 12000, '2021-01-13'),
	(8, 'test1', 'tester1', 3, 'iphone', 50000, 2, 100000, '2021-01-13');
/*!40000 ALTER TABLE `item_order` ENABLE KEYS */;

-- 테이블 hyomin_db.member 구조 내보내기
CREATE TABLE IF NOT EXISTS `member` (
  `id` varchar(100) NOT NULL,
  `pw` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `u_date` varchar(50) NOT NULL,
  `question` varchar(100) NOT NULL,
  `answer` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='회원 테이블';

-- 테이블 데이터 hyomin_db.member:~4 rows (대략적) 내보내기
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT IGNORE INTO `member` (`id`, `pw`, `name`, `u_date`, `question`, `answer`, `email`) VALUES
	('test1', '12345', 'tester1', '2021-01-11', 'your nickname?', 'test1', 'test1@naver.com'),
	('test2', '1234', 'tester2', '2021-01-11', 'your nickname?', 'test2', 'test2@naver.com'),
	('test3', '1234', 'tester3', '2021-01-12', 'your nickname ?', 'test3', 'test3@naver.com'),
	('test4', '1234', 'tester4', '2021-01-12', 'your nickname ?', 'test4', 'test4@naver.com');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;

-- 테이블 hyomin_db.review 구조 내보내기
CREATE TABLE IF NOT EXISTS `review` (
  `rcode` int NOT NULL AUTO_INCREMENT,
  `icode` int NOT NULL,
  `id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `rtext` varchar(100) NOT NULL,
  `r_date` varchar(100) NOT NULL,
  PRIMARY KEY (`rcode`),
  KEY `review_fk_icode` (`icode`),
  KEY `review_fk_id` (`id`),
  CONSTRAINT `review_fk_icode` FOREIGN KEY (`icode`) REFERENCES `item` (`icode`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `review_fk_id` FOREIGN KEY (`id`) REFERENCES `member` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='상품 리뷰 테이블';

-- 테이블 데이터 hyomin_db.review:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
INSERT IGNORE INTO `review` (`rcode`, `icode`, `id`, `name`, `rtext`, `r_date`) VALUES
	(2, 1, 'test1', 'tester1', 'great apple !', '2021-01-14'),
	(3, 4, 'test1', 'tester1', '멋진 가방이네요 좋습니다', '2021-01-14');
/*!40000 ALTER TABLE `review` ENABLE KEYS */;

-- 테이블 hyomin_db.wishlist 구조 내보내기
CREATE TABLE IF NOT EXISTS `wishlist` (
  `id` varchar(100) NOT NULL,
  `icode` int NOT NULL,
  KEY `fk_id` (`id`),
  KEY `fk_icode` (`icode`),
  CONSTRAINT `fk_icode` FOREIGN KEY (`icode`) REFERENCES `item` (`icode`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_id` FOREIGN KEY (`id`) REFERENCES `member` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='상품 위시리스트 테이블';

-- 테이블 데이터 hyomin_db.wishlist:~2 rows (대략적) 내보내기
/*!40000 ALTER TABLE `wishlist` DISABLE KEYS */;
INSERT IGNORE INTO `wishlist` (`id`, `icode`) VALUES
	('test1', 1),
	('test1', 3);
/*!40000 ALTER TABLE `wishlist` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
