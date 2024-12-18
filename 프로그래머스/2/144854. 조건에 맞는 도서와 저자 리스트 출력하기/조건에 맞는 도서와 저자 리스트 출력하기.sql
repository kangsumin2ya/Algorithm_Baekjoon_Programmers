-- 코드를 입력하세요
SELECT
    BOOK_ID, 
    AUTHOR_NAME, 
    date_format(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from BOOK as b
    left join AUTHOR as a
    on b.AUTHOR_ID = a.AUTHOR_ID
where CATEGORY = '경제'
order by PUBLISHED_DATE asc
;