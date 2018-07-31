select s.Score, CAST(temp.Rank as SIGNED) as Rank from Scores s left join 
(
	select t.Score, @rank := @rank + 1 as Rank from 
	(
		select Score
		from Scores
		group by Score 
		order by Score desc
	) t, (select @rank := 0) r
) temp on s.Score = temp.Score
order by s.Score desc
