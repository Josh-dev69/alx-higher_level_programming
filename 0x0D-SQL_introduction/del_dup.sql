-- Delete duplicate Values

DELETE FROM second_table
WHERE score NOT IN (
    SELECT MIN(score)
    FROM second_table
    GROUP BY score
);

