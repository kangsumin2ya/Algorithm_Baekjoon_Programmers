-- 코드를 작성해주세요
SELECT -- ID와 길이
    ID,
    LENGTH
FROM
    FISH_INFO
 --  가장 큰 물고기 10마리  
ORDER BY -- 1)길이를 기준으로 내림차순 정렬, 2)물고기의 ID에 대해 오름차순 정렬
    LENGTH DESC,
    ID ASC
LIMIT 10
;