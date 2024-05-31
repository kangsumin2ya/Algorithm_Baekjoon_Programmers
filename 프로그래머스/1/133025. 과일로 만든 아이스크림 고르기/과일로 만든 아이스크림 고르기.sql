-- 코드를 입력하세요
SELECT o.FLAVOR -- o.FLAVOR
from FIRST_HALF as O
    left join ICECREAM_INFO as I
      on O.FLAVOR = I.FLAVOR
where TOTAL_ORDER >= 3000
   and INGREDIENT_TYPE = 'fruit_based'
order by TOTAL_ORDER desc
;