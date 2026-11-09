select max(single_num.num) as num
from (
    select num
    from MyNumbers
    group by num
    having count(*) = 1
) as single_num