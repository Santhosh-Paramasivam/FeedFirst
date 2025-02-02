use FeedFirst;

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'FeedFirst';

select * from foodvouchers;

select * from requesteditem;

select * from item;

insert into item(storage_units_used, request_units_used, current_stock, item_name) values ('jars','g / grams','Medium','Peanut Butter');
insert into item(storage_units_used, request_units_used, current_stock, item_name) values ('cans','g / grams','High','Canned Beans');
insert into item(storage_units_used, request_units_used, current_stock, item_name) values ('cans','g / grams','High','Canned Chicken');
insert into item(storage_units_used, request_units_used, current_stock, item_name) values ('cans','g / grams','High','Canned Fish');
insert into item(storage_units_used, request_units_used, current_stock, item_name) values ('cans','g / grams','Low','Canned Fruit');
insert into item(storage_units_used, request_units_used, current_stock, item_name) values ('cans','g / grams','Medium','Instant Mashed Potatoes');
insert into item(storage_units_used, request_units_used, current_stock, item_name) values ('kg / kilograms','kg / kilograms','High','Pasta');
insert into item(storage_units_used, request_units_used, current_stock, item_name) values ('kg / kilograms','kg / kilograms','Medium','Rice');
insert into item(storage_units_used, request_units_used, current_stock, item_name) values ('kg / kilograms','kg / kilograms','High','Powdered Milk');

set AUTOCOMMIT = 1;
set AUTOCOMMIT = 0;