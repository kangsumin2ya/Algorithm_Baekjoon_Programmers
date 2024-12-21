-- 코드를 작성해주세요
SELECT -- 개발자의 ID, 이메일, 이름, 성
    ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
FROM
    DEVELOPERS
WHERE -- Python이나 C# 스킬
    SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python')
    OR SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#')
ORDER BY -- ID를 기준으로 오름차순 정렬
    ID ASC
;