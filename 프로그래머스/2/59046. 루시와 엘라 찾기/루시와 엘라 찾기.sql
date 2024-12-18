-- 코드를 입력하세요
SELECT
    ANIMAL_ID,
    NAME,
    SEX_UPON_INTAKE
FROM
    ANIMAL_INS
WHERE    -- 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물
    NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY
    ANIMAL_ID ASC
;