/*
Navicat MySQL Data Transfer

Source Server         : my
Source Server Version : 50725
Source Host           : 182.254.217.138:3306
Source Database       : box_vs_sql

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-12-21 11:39:10
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `dlc`
-- ----------------------------
DROP TABLE IF EXISTS `dlc`;
CREATE TABLE `dlc` (
  `DID` int(10) NOT NULL,
  `Dtype` int(10) NOT NULL,
  `UID` int(10) NOT NULL,
  `money` int(10) NOT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`DID`),
  KEY `dlcforeignUID` (`UID`),
  CONSTRAINT `dlcforeignUID` FOREIGN KEY (`UID`) REFERENCES `login` (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of dlc
-- ----------------------------
INSERT INTO `dlc` VALUES ('1', '1', '1', '20', '2019-12-03 18:00:01');
INSERT INTO `dlc` VALUES ('2', '2', '1', '20', '2019-12-03 20:00:01');
INSERT INTO `dlc` VALUES ('3', '1', '2', '20', '2019-12-03 18:00:01');
INSERT INTO `dlc` VALUES ('4', '1', '3', '20', '2019-12-03 20:00:01');
INSERT INTO `dlc` VALUES ('5', '5', '1', '20', '2019-12-03 20:00:01');

-- ----------------------------
-- Table structure for `gamerecord`
-- ----------------------------
DROP TABLE IF EXISTS `gamerecord`;
CREATE TABLE `gamerecord` (
  `GID` int(10) NOT NULL,
  `DID` int(10) NOT NULL,
  `UID` int(10) NOT NULL,
  `EndTime` datetime DEFAULT NULL,
  `Score` int(10) DEFAULT NULL,
  PRIMARY KEY (`GID`),
  KEY `loginforeignUID` (`UID`),
  KEY `loginforeignDID` (`DID`),
  CONSTRAINT `loginforeignDID` FOREIGN KEY (`DID`) REFERENCES `dlc` (`DID`),
  CONSTRAINT `loginforeignUID` FOREIGN KEY (`UID`) REFERENCES `login` (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of gamerecord
-- ----------------------------
INSERT INTO `gamerecord` VALUES ('1', '1', '1', '2019-12-04 18:00:01', '20');
INSERT INTO `gamerecord` VALUES ('2', '5', '1', '2019-12-05 18:00:01', '100');
INSERT INTO `gamerecord` VALUES ('3', '3', '2', '2019-12-06 18:00:01', '21');
INSERT INTO `gamerecord` VALUES ('4', '4', '3', '2019-12-07 18:00:01', '33');

-- ----------------------------
-- Table structure for `login`
-- ----------------------------
DROP TABLE IF EXISTS `login`;
CREATE TABLE `login` (
  `UID` int(10) NOT NULL,
  `UserName` varchar(55) NOT NULL,
  `PassWord` varchar(55) NOT NULL,
  `NickName` varchar(55) NOT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of login
-- ----------------------------
INSERT INTO `login` VALUES ('1', 'tianyilt', '123', 'mdzz');
INSERT INTO `login` VALUES ('2', 'alpha', '123', 'md');
INSERT INTO `login` VALUES ('3', 'beta', '123', 'mdz');

-- ----------------------------
-- View structure for `dashboard`
-- ----------------------------
DROP VIEW IF EXISTS `dashboard`;
CREATE ALGORITHM=UNDEFINED DEFINER=`ZNDY`@`%` SQL SECURITY DEFINER VIEW `dashboard` AS select `gamerecord`.`UID` AS `UID`,max(`gamerecord`.`Score`) AS `MAXSCORE` from `gamerecord` group by `gamerecord`.`UID` order by `MAXSCORE` desc ;

-- ----------------------------
-- View structure for `dlcbuy`
-- ----------------------------
DROP VIEW IF EXISTS `dlcbuy`;
CREATE ALGORITHM=UNDEFINED DEFINER=`ZNDY`@`%` SQL SECURITY DEFINER VIEW `dlcbuy` AS select `dlc`.`UID` AS `UID`,`dlc`.`Dtype` AS `Dtype`,`dlc`.`date` AS `Date` from `dlc` order by `dlc`.`UID` ;
