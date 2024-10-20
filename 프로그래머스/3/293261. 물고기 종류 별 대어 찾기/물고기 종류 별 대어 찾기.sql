-- 코드를 작성해주세요
select 
    I.ID, N.FISH_NAME, I.LENGTH
from
    FISH_INFO as I
join 
    FISH_NAME_INFO as N
on 
   I.FISH_TYPE = N.FISH_TYPE
where
    I.LENGTH in(
        select 
            max(LENGTH)
        from 
            FISH_INFO
        where
            FISH_TYPE = I.FISH_TYPE
        group by
            FISH_TYPE
    )
order by
    I.ID
;