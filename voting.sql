create database voting;
use voting;
create table registration
(
f_name varchar(50),
l_name varchar(50),
email varchar(50),
pass varchar(50),
cpass varchar(50),
aadhar int,
dob int,
gender varchar(50)
);
alter table registration
add statuss varchar(50);
alter table registration
add party varchar(50);


select * from registration;
create table admin_details
(
id int,
pass varchar(50)
);
insert into admin_details(id , pass) values(12345 , 123);
select * from admin_details; 