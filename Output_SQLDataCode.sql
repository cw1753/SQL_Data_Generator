DELETE FROM Share;
DELETE FROM Member;
DELETE FROM FriendGroup;
DELETE FROM Comment;
DELETE FROM Tag;
DELETE FROM Content;
DELETE FROM Person;
INSERT INTO Person (username, password, first_name, last_name) VALUES
('User1','e9cac23f4b09ddec0c7cafa2b927f888','Yahir','Yan'),
('User2','e9cac23f4b09ddec0c7cafa2b927f888','Quinn','Qi'),
('User3','e9cac23f4b09ddec0c7cafa2b927f888','Zachary','Zheng'),
('User4','e9cac23f4b09ddec0c7cafa2b927f888','Isaac','Irving'),
('User5','e9cac23f4b09ddec0c7cafa2b927f888','Xavier','Xiang'),
('User6','e9cac23f4b09ddec0c7cafa2b927f888','Gabriel','Garcia'),
('User7','e9cac23f4b09ddec0c7cafa2b927f888','Benjamin','Brown'),
('User8','e9cac23f4b09ddec0c7cafa2b927f888','Christopher','Chan'),
('User9','e9cac23f4b09ddec0c7cafa2b927f888','Uriel','Underwood'),
('User10','e9cac23f4b09ddec0c7cafa2b927f888','Henry','Hernandez'),
('User11','e9cac23f4b09ddec0c7cafa2b927f888','Samuel','Smith'),
('User12','e9cac23f4b09ddec0c7cafa2b927f888','Alexander','﻿Anderson'),
('User13','e9cac23f4b09ddec0c7cafa2b927f888','Ryan','Ross'),
('User14','e9cac23f4b09ddec0c7cafa2b927f888','Owen','Orz'),
('User15','e9cac23f4b09ddec0c7cafa2b927f888','Kevin','Kumar'),
('User16','e9cac23f4b09ddec0c7cafa2b927f888','Parker','Peterson');



INSERT INTO Content (id, username, timest, file_path, content_name, public) VALUES
(0,'User12','2018-11-03 01:20:18','file_path4','Graduation',0),
(1,'User5','2015-09-13 10:30:25','file_path5','Party',1),
(2,'User6','2015-06-03 04:28:44','file_path0','Graduation',0),
(3,'User4','2016-07-25 09:27:54','file_path4','New Year',1),
(4,'User15','2015-06-11 11:40:34','file_path6','Christmas',1),
(5,'User10','2018-06-14 10:52:51','file_path2','Graduation',0),
(6,'User14','2015-11-24 03:07:40','file_path4','Birthday',0),
(7,'User7','2018-04-08 07:11:27','file_path5','Party',0);



INSERT INTO Tag (id, username_tagger, username_taggee, timest, status) VALUES
(6,'User1','User5','2018-10-05 10:39:43',1),
(7,'User3','User6','2016-07-06 05:47:03',0),
(3,'User9','User13','2017-04-22 09:05:57',1),
(4,'User13','User15','2017-03-04 01:44:55',1),
(2,'User14','User14','2018-08-05 12:25:36',0),
(1,'User2','User16','2015-03-24 07:12:16',0),
(5,'User8','User9','2016-03-24 07:23:39',1),
(0,'User15','User8','2018-02-07 11:15:10',0);



INSERT INTO Comment (id, username, timest, comment_text) VALUES
(2,'User5','2016-12-08 02:01:47','What a wonderful Meal!'),
(0,'User13','2015-07-25 11:08:16','It was a great day!'),
(6,'User7','2018-01-26 02:47:38','What a wonderful Meal!'),
(3,'User3','2017-05-22 10:55:17','I\'m commenting again!'),
(5,'User14','2018-08-27 11:44:19','Lol'),
(4,'User11','2016-09-08 06:35:34','Glad I was able to come!'),
(7,'User12','2017-02-18 11:58:16','What a wonderful Meal!'),
(1,'User2','2016-12-20 11:12:25','Hello there!!!');



INSERT INTO FriendGroup (group_name, username, description) VALUES
('Game','User6','All of my friends'),
('Game','User8','My entire family'),
('Family','User14','School classmates'),
('Gym','User16','My entire family'),
('NYU','User9','School classmates'),
('Family','User1','My entire family'),
('NYU','User10','Some of my coworkers'),
('Basketball Team','User5','My friends');



INSERT INTO Member (username, group_name, username_creator) VALUES
('User14','NYU','User9'),
('User6','Gym','User16'),
('User1','Game','User8'),
('User10','NYU','User10'),
('User8','Basketball Team','User5'),
('User9','Family','User1'),
('User2','Family','User14'),
('User3','Game','User6');



INSERT INTO Share (id, group_name, username) VALUES
(1,'Basketball Team','User5'),
(0,'NYU','User10'),
(7,'Family','User14'),
(5,'Game','User8'),
(2,'Game','User6'),
(4,'NYU','User9'),
(3,'Family','User1'),
(6,'Gym','User16');



