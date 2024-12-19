-- 코드를 작성해주세요
SELECT
    YEAR(DIFFERENTIATION_DATE) AS YEAR,
    MAX_SIZE_OF_COLONY - SIZE_OF_COLONY AS YEAR_DEV,
    ID
FROM
    ECOLI_DATA AS A,
    (
        SELECT 
            MAX(SIZE_OF_COLONY) AS MAX_SIZE_OF_COLONY,
            YEAR(DIFFERENTIATION_DATE) AS YEAR   
        FROM
            ECOLI_DATA
        GROUP
            BY YEAR(DIFFERENTIATION_DATE)
    ) AS B
WHERE -- 분화된 연도별 대장균 크기의 편차
    YEAR(DIFFERENTIATION_DATE) = B.YEAR
ORDER BY -- 1) 연도에 대해 오름차순으로 정렬, 2) 대장균 크기의 편차에 대해 오름차순
    YEAR,
    YEAR_DEV
;