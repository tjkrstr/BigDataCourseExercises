# Assingment Solution

The following SQL is the solution to Exercise 6 - "Sentiment exercise with Hive!" The first SQL part creates the two tables (positive_words, negative_words) consisting of a single column with a unique word in each row.

Note that the _raw-tables created in exercise 3 are used.

```sql
create table positive_words as
  select explode(split(word, ',')) word 
  from positive_words_raw;

create table negative_words as
  select explode(split(word, ',')) word 
  from negative_words_raw;
```

The following SQL statements are two different examples on how to solve the last part of the assignment (first part is the full solution the next statement is an example of how to write it differently). Here we do a query where we join the tables with the word_counts table.

```sql
select w.* from (
  select 
    c.*
    , case when p.word is not null then true else false end positive
    , case when n.word is not null then true else false end negative
  from word_counts c
  left outer join positive_words p on c.word = p.word
  left outer join negative_words n on c.word = n.word
) w
where w.positive = true or w.negative = true
order by w.count desc;
```

```sql
SELECT SUM(wc.count) as positive FROM word_counts as wc LEFT JOIN positive_words as pw WHERE wc.word = pw.word;
```
