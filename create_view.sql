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


/*死掉10个脑细胞的dashboard查询语句，自己用的是子查询，把用select出来的当做新表，命名为A2*/
SELECT login.UserName,B.Score,B.EndTime
    from gamerecord B, (select A.UID,MAX(A.Score) AS Ascore
from gamerecord A
group by UID) A2, login
WHERE A2.Ascore=B.Score AND A2.UID = B.UID AND login.UID=B.UID
ORDER BY B.Score DESC;
/*死掉微软脑细胞的数据表，由上面自动生成*/
SELECT   login.UserName, B.Score, B.EndTime
FROM      gamerecord AS B CROSS JOIN
                    (SELECT   A.UID, MAX(A.Score) AS Ascore
                     FROM      gamerecord AS A
                     GROUP BY UID) AS A2 CROSS JOIN
                login
WHERE   (A2.Ascore = B.Score) AND (A2.UID = B.UID) AND (login.UID = B.UID)
ORDER BY B.Score DESC

/*为查询令人深恶痛绝的username转uid did而准备的视图*/
DROP view IF EXISTS `ID`;
CREATE VIEW ID
as
SELECT   login.UserName, login.UID, dlc.DID, dlc.Dtype
FROM login cross join dlc on dlc.UID = login.UID;

