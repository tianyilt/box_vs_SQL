/*
Navicat MySQL Data Transfer

Source Server         : my
Source Server Version : 50725
Source Host           : 182.254.217.138:3306
Source Database       : box_vs_sql

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-12-22 19:18:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `dlc`
-- ----------------------------
DROP TABLE IF EXISTS `dlc`;
CREATE TABLE `dlc` (
  `DID` int(10) NOT NULL AUTO_INCREMENT,
  `Dtype` int(10) NOT NULL,
  `UID` int(10) NOT NULL,
  `money` int(10) NOT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`DID`),
  KEY `dlcforeignUID` (`UID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of dlc
-- ----------------------------
INSERT INTO `dlc` VALUES ('1', '1', '1', '20', '2019-12-03 18:00:01');
INSERT INTO `dlc` VALUES ('2', '2', '1', '20', '2019-12-03 20:00:01');
INSERT INTO `dlc` VALUES ('3', '1', '2', '20', '2019-12-03 18:00:01');
INSERT INTO `dlc` VALUES ('4', '1', '3', '20', '2019-12-03 20:00:01');
INSERT INTO `dlc` VALUES ('5', '5', '1', '20', '2019-12-03 20:00:01');
INSERT INTO `dlc` VALUES ('6', '3', '1', '6', '2019-12-22 00:30:52');
INSERT INTO `dlc` VALUES ('7', '0', '6', '6', '2019-12-22 02:45:55');
INSERT INTO `dlc` VALUES ('8', '1', '6', '6', '2019-12-22 02:46:06');
INSERT INTO `dlc` VALUES ('9', '0', '6', '6', '2019-12-22 02:52:45');
INSERT INTO `dlc` VALUES ('10', '0', '6', '6', '2019-12-22 02:52:50');
INSERT INTO `dlc` VALUES ('11', '0', '6', '6', '2019-12-22 02:58:39');
INSERT INTO `dlc` VALUES ('12', '1', '6', '6', '2019-12-22 02:58:48');
INSERT INTO `dlc` VALUES ('13', '2', '6', '6', '2019-12-22 02:58:58');
INSERT INTO `dlc` VALUES ('14', '0', '8', '0', '2019-12-22 11:31:47');
INSERT INTO `dlc` VALUES ('15', '1', '8', '6', '2019-12-22 11:47:52');
INSERT INTO `dlc` VALUES ('16', '2', '8', '6', '2019-12-22 11:57:20');

-- ----------------------------
-- Table structure for `gamerecord`
-- ----------------------------
DROP TABLE IF EXISTS `gamerecord`;
CREATE TABLE `gamerecord` (
  `GID` int(10) NOT NULL AUTO_INCREMENT,
  `DID` int(10) NOT NULL,
  `UID` int(10) NOT NULL,
  `EndTime` datetime DEFAULT NULL,
  `Score` int(10) DEFAULT NULL,
  PRIMARY KEY (`GID`),
  KEY `loginforeignUID` (`UID`),
  KEY `loginforeignDID` (`DID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of gamerecord
-- ----------------------------
INSERT INTO `gamerecord` VALUES ('1', '1', '1', '2019-12-04 18:00:01', '20');
INSERT INTO `gamerecord` VALUES ('3', '3', '2', '2019-12-06 18:00:01', '21');
INSERT INTO `gamerecord` VALUES ('4', '4', '3', '2019-12-07 18:00:01', '33');
INSERT INTO `gamerecord` VALUES ('5', '1', '1', '2019-12-22 02:48:41', '100');
INSERT INTO `gamerecord` VALUES ('6', '16', '8', '2019-12-22 12:02:23', '2');

-- ----------------------------
-- Table structure for `login`
-- ----------------------------
DROP TABLE IF EXISTS `login`;
CREATE TABLE `login` (
  `UID` int(10) NOT NULL AUTO_INCREMENT,
  `UserName` varchar(55) NOT NULL,
  `PassWord` varchar(55) NOT NULL,
  `NickName` varchar(55) NOT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of login
-- ----------------------------
INSERT INTO `login` VALUES ('1', 'tianyilt', '123', 'mdzz');
INSERT INTO `login` VALUES ('2', 'alpha', '123', 'md');
INSERT INTO `login` VALUES ('3', 'beta', '123', 'mdz');
INSERT INTO `login` VALUES ('4', 'ty', '123', 'tt');
INSERT INTO `login` VALUES ('5', 'tianyilty', '123', 'lltyy');
INSERT INTO `login` VALUES ('6', '1', '1', '1');
INSERT INTO `login` VALUES ('7', 'nagaofen', '1', 'nagaofen');
INSERT INTO `login` VALUES ('8', '2', '2', '2');

-- ----------------------------
-- View structure for `dashboard`
-- ----------------------------
DROP VIEW IF EXISTS `dashboard`;
CREATE ALGORITHM=UNDEFINED DEFINER=`ZNDY`@`%` SQL SECURITY DEFINER VIEW `dashboard` AS select `box_vs_sql`.`login`.`UserName` AS `UserName`,`B`.`Score` AS `Score`,`B`.`EndTime` AS `EndTime` from ((`box_vs_sql`.`gamerecord` `B` join (select `A`.`UID` AS `UID`,max(`A`.`Score`) AS `Ascore` from `box_vs_sql`.`gamerecord` `A` group by `A`.`UID`) `A2`) join `box_vs_sql`.`login`) where ((`A2`.`Ascore` = `B`.`Score`) and (`A2`.`UID` = `B`.`UID`) and (`box_vs_sql`.`login`.`UID` = `B`.`UID`)) order by `B`.`Score` desc ;

-- ----------------------------
-- View structure for `dlcbuy`
-- ----------------------------
DROP VIEW IF EXISTS `dlcbuy`;
CREATE ALGORITHM=UNDEFINED DEFINER=`ZNDY`@`%` SQL SECURITY DEFINER VIEW `dlcbuy` AS select `login`.`UserName` AS `UserName`,`dlc`.`Dtype` AS `Dtype`,`dlc`.`date` AS `Date` from (`dlc` join `login`) where (`dlc`.`UID` = `login`.`UID`) order by `dlc`.`UID` ;

-- ----------------------------
-- View structure for `ID`
-- ----------------------------
DROP VIEW IF EXISTS `ID`;
CREATE ALGORITHM=UNDEFINED DEFINER=`ZNDY`@`%` SQL SECURITY DEFINER VIEW `ID` AS select `login`.`UserName` AS `UserName`,`login`.`UID` AS `UID`,`dlc`.`DID` AS `DID`,`dlc`.`Dtype` AS `Dtype` from (`login` join `dlc` on((`dlc`.`UID` = `login`.`UID`))) ;
