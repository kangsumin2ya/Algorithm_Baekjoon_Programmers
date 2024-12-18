-- 코드를 입력하세요
SELECT
    ANIMAL_ID,
    NAME
FROM
    ANIMAL_INS
WHERE -- 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회
    NAME
    LIKE '%EL%'
AND
    ANIMAL_TYPE = 'Dog'
ORDER BY
    NAME ASC
;