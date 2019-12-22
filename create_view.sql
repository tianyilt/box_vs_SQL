DROP view IF EXISTS `dlcbuy`;
CREATE VIEW dlcbuy
as
SELECT   UserName, Dtype, Date
FROM      dlc cross join login
where dlc.uid=login.uid
ORDER BY dlc.UID;

/*dashboard
  查询用户名和最高分，以及取得最高分的时间*/

DROP view IF EXISTS `dashboard`;
CREATE VIEW dashboard
as
SELECT   UserName, Score, EndTime
FROM      gamerecord cross join login
where gamerecord.UID = login.UID
ORDER BY SCORE DESC;

DROP view IF EXISTS `ID`;
CREATE VIEW ID
as
SELECT   login.UserName, login.UID, dlc.DID, dlc.Dtype
FROM login cross join dlc on dlc.UID = login.UID;

SELECT   login.UserName, dlc.DID, dlc.Dtype
FROM (login cross join dlc on dlc.UID = login.UID)
    cross join gamerecord on gamerecord.UID=login.UID

SELECT   login.UserName, login.UID, dlc.DID, dlc.Dtype
FROM login cross join dlc on dlc.UID = login.UID;

SELECT   gamerecord.DID, gamerecord.UID
FROM gamerecord  right join dlc on gamerecord.uid = dlc.UID




SELECT   UserName, MAX(EndTime) AS LastTime, MAX(Score) AS MaxScore
FROM      gamerecord cross join login
where gamerecord.UID = login.UID
GROUP BY gamerecord.UID
ORDER BY MAXSCORE DESC;
