/*
Navicat MySQL Data Transfer

Source Server         : my
Source Server Version : 50725
Source Host           : 182.254.217.138:3306
Source Database       : box_vs_sql

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-12-20 21:29:04
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `dlc`
-- ----------------------------
DROP TABLE IF EXISTS `dlc`;
CREATE TABLE `dlc` (
  `DID` int(10) NOT NULL,
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
