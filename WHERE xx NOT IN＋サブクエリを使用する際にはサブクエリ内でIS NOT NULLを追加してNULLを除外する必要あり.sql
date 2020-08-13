--  [BS(L4).1]には含まれているが、[BS(L4)]には含まれていない値を抽出する
-- 参考：https://www.ilovex.co.jp/blog/system/cat820/sqlnot-in.html
SELECT
    [BS(L4)]
    ,[BS(L4).1]
FROM
    [temp]
WHERE
    [BS(L4).1] NOT IN (SELECT [BS(L4)] FROM [temp] WHERE [BS(L4)] IS NOT NULL)