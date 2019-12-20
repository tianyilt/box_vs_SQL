/*
Navicat MySQL Data Transfer

Source Server         : my
Source Server Version : 50725
Source Host           : 182.254.217.138:3306
Source Database       : box_vs_sql

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-12-19 16:33:32
*/

SET FOREIGN_KEY_CHECKS=0;



create table login(
UID int(10) not null primary key,
UserName varchar(55) not null,
PassWord varchar(55) not null,
NickName VARCHAR(55) not null
);

create table gamerecord(
GID int(10) not null primary key,
DID int(10) not null,
UID int(10) not null,
EndTime DATETIME,
Score int(10)
);

create table dlc(
DID int(10) not null primary key,
UID int(10) not null,
money int(10) not null,
date DATETIME
);



/*set foreign key*/
ALTER TABLE gamerecord ADD CONSTRAINT loginforeignUID
FOREIGN KEY(UID) REFERENCES login(UID);
ALTER TABLE gamerecord ADD CONSTRAINT loginforeignDID
FOREIGN KEY(DID) REFERENCES dlc(DID);
ALTER TABLE dlc ADD CONSTRAINT dlcforeignUID
FOREIGN KEY(UID) REFERENCES login(UID);
