-- 코드를 입력하세요
SELECT user_id, product_id
FROM ONLINE_SALE
group by user_id, product_id
having count(*) >= 2
order by user_id , product_id desc