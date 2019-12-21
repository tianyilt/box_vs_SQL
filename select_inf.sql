select * from dlcbuy;
select * from dlc;

SELECT   dlc.Dtype
FROM      login CROSS JOIN
                dlc
WHERE   (login.uid = dlc.UID) AND (login.username = 'tianyilt')

SELECT   dlc.Dtype
FROM      login CROSS JOIN
                dlc
WHERE   (login.uid = dlc.UID) AND (login.username = 'tianyilt')




show processlist ;