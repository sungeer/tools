


'上传耗时', '上传结果写入耗时', '统计耗时', '测厚耗时'

'写入数据库耗时', '获取芯片UID耗时', '扫码耗时'

'获取烧录链接耗时', '执行烧录耗时', '烧录总耗时'


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




"operation"
"写入烧录到本地耗时"
"复核整体耗时"
"执行写入操作细微耗时"
"执行烧录耗时"
"扫码耗时"
"测厚耗时"
"添加APP记录耗时"
"添加URL记录耗时"
"清空NDEF写入缓冲队列耗时"
"烧录整体耗时"
"获取烧录链接耗时"
"获取芯片UID耗时"












