--  [BS(L4).1]�ɂ͊܂܂�Ă��邪�A[BS(L4)]�ɂ͊܂܂�Ă��Ȃ��l�𒊏o����
-- �Q�l�Fhttps://www.ilovex.co.jp/blog/system/cat820/sqlnot-in.html
SELECT
    [BS(L4)]
    ,[BS(L4).1]
FROM
    [temp]
WHERE
    [BS(L4).1] NOT IN (SELECT [BS(L4)] FROM [temp] WHERE [BS(L4)] IS NOT NULL)