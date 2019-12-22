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
SELECT   login.UserName, B.Score, B.EndTime
FROM      gamerecord AS B CROSS JOIN
                    (SELECT   A.UID, MAX(A.Score) AS Ascore
                     FROM      gamerecord AS A
                     GROUP BY UID) AS A2 CROSS JOIN
                login
WHERE   (A2.Ascore = B.Score) AND (A2.UID = B.UID) AND (login.UID = B.UID)
ORDER BY B.Score DESC



SELECT login.UserName,B.Score,B.EndTime
    from gamerecord B, (select A.UID,MAX(A.Score) AS Ascore
from gamerecord A
group by UID) A2, login
WHERE A2.Ascore=B.Score AND A2.UID = B.UID AND login.UID=B.UID
ORDER BY B.Score DESC;

SELECT   login.UserName, B.Score, B.EndTime
FROM      gamerecord AS B CROSS JOIN
                    (SELECT   A.UID, MAX(A.Score) AS Ascore
                     FROM      gamerecord AS A
                     GROUP BY UID) AS A2 CROSS JOIN
                login
WHERE   (A2.Ascore = B.Score) AND (A2.UID = B.UID) AND (login.UID = B.UID)
ORDER BY B.Score DESC

select A.UID,MAX(A.Score) AS Ascore
from gamerecord A
group by UID



select A.UID, A.Score, A.EndTime
from gamerecord A,gamerecord B
WHERE A.Score=B.Score;





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
