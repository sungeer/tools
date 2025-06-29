





-- 查询 烧录 最慢的
SELECT *
FROM
    mix
WHERE
    OPERATION = '烧录总耗时'
ORDER BY duration_ms DESC;




-- 查询 执行 烧录耗时
SELECT *
FROM
    mix
WHERE
    OPERATION = '执行烧录耗时'
ORDER BY duration_ms DESC;
















