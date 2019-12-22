/*这里把操作数据库用到的命令都列在这里*/
select * from dlcbuy;
select * from dlc;
select * from login;
select * from ID;
select * from gamerecord;
select * from dashboard limit 10;
select * from dashboard where username = 'tianyilt' limit 10;
select UserName, DID, UID, Dtype from ID where UserName = 'tianyilt' and Dtype = 1

SELECT   dlc.Dtype
FROM      login CROSS JOIN
                dlc
WHERE   (login.uid = dlc.UID) AND (login.username = 'tianyilt')

SELECT   dlc.Dtype
FROM      login CROSS JOIN
                dlc
WHERE   (login.uid = dlc.UID) AND (login.username = 'tianyilt')

insert into dlc values
(1,1,1,20,'2019-12-03 18:00:01');

show processlist ;

SELECT Dtype FROM dlcbuy WHERE username = '2'