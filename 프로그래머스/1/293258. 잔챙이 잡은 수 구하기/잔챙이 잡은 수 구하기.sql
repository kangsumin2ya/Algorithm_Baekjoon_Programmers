-- 코드를 작성해주세요
SELECT
    COUNT(ID) AS FISH_COUNT
FROM
    FISH_INFO
WHERE -- 길이가 10cm 이하인 물고기의 수
    LENGTH IS NULL
;