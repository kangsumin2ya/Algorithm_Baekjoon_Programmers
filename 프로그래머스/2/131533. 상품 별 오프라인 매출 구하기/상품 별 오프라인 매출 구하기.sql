-- 코드를 입력하세요
 SELECT  
        p.PRODUCT_CODE,
        sum(o.SALES_AMOUNT * p.PRICE) as SALES
from OFFLINE_SALE as o
    left join PRODUCT as p
    on o.PRODUCT_ID = p.PRODUCT_ID
group by p.PRODUCT_CODE
order by SALES desc, p.PRODUCT_CODE asc
;