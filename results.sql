use test
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product

-- 2. Выбрать названия всех автоматизированных складов
select * FROM store where is_automated = 1

-- 3. Посчитать общую сумму в деньгах всех продаж
select sum(total) from sale

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
select distinct store_id from sale

-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
select store.store_id from store left join sale on store.store_id = sale.store_id where sale.store_id is null;

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
select name, sum(total)/sum(quantity) as 'avg(total/quantity)' from product natural join sale group by name order by avg(total/quantity);

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select temp.name from (select product.name, count(distinct store.name) as cd from product natural join sale join store on sale.store_id = store.store_id group by product.name having cd = 1) as temp;

-- 8. Получить названия всех складов, с которых продавался только один продукт
select t.name from (select st.name, count(distinct p.name) d from store st natural join sale sa join product p on sa.product_id = p.product_id group by st.name having d=1) as t;

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select * from sale s where s.total = (select max(total) from sale);

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select date from (select date, sum(total) as mt from sale group by date) as t where mt = (select max(t.mt) from (select date, sum(total) as mt from sale group by date) as t);
