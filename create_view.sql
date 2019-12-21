DROP view IF EXISTS `dlcbuy`;
CREATE VIEW dlcbuy
as
SELECT   UserName, Dtype, Date
FROM      dlc cross join login
where dlc.uid=login.uid
ORDER BY dlc.UID;

CREATE VIEW dashboard
as
SELECT   UID, MAX(Score) AS MAXSCORE
FROM      gamerecord
GROUP BY UID
ORDER BY MAXSCORE DESC;
