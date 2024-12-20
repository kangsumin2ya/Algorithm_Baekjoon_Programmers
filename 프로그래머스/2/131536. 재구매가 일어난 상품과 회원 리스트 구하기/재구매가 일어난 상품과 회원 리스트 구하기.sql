-- 코드를 입력하세요
SELECT
    USER_ID,
    PRODUCT_ID
FROM
    ONLINE_SALE
GROUP BY -- 동일한 회원이 동일한 상품을 재구매한 데이터
    USER_ID,
    PRODUCT_ID
    HAVING COUNT(*) > 1
ORDER BY -- 1)회원 ID를 기준으로 오름차순 정렬, 2)상품 ID를 기준으로 내림차순 정렬
    USER_ID ASC, PRODUCT_ID DESC
;