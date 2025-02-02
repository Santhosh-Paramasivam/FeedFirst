use FeedFirst;

select * from foodvouchers;
select * from requesteditem;

select * from recepients

delete from foodvouchers;
delete from requesteditem;

select recepient_id from recepients where username = 'santhoshp';
insert into foodvouchers(recepient_id, status) values (1,"PENDING");

INSERT INTO requesteditem(item_ID, voucher_ID, requested_quantity) VALUES(1, cursor.lastrowid, 10)

delete from foodvouchers where voucher_id = 16;

UPDATE recepients SET priority = 'MEDIUM' WHERE recepient_ID = 2

update foodvouchers set status = 'PENDING' where status = 'APPROVED'

alter table requesteditem add voucher_item_ID INT primary key auto_increment

commit

SELECT item_ID FROM item WHERE item_name = 'Peanut Butter'

select * from pantryitembatches

