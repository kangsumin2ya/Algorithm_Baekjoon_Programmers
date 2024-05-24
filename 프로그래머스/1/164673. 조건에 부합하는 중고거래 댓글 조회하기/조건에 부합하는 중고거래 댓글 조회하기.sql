-- 코드를 입력하세요
SELECT B.TITLE
       , R.BOARD_ID as BOARD_ID
       , REPLY_ID
       , R.WRITER_ID
       , R.CONTENTS
       , DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
    from USED_GOODS_REPLY as R
    left 
    join USED_GOODS_BOARD as B 
      on R.BOARD_ID = B.BOARD_ID
    where B.CREATED_DATE >= '2022-10-01' 
            and B.CREATED_DATE < '2022-11-01'
    order 
        by R.CREATED_DATE ASC, B.TITLE ASC
;