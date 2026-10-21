
-- 1. Check the total number of records
SELECT COUNT(*) AS total_records
FROM superstore;

-- 2. Calculate overall sales and profit
SELECT
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2)
        AS profit_margin_percentage
FROM superstore;

-- 3. Compare sales and profit by category
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore
GROUP BY Category
ORDER BY total_sales DESC;

-- 4. Compare performance by region
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore
GROUP BY Region
ORDER BY total_profit DESC;

-- 5. Find loss-making sub-categories
SELECT
    [Sub-Category],
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore
GROUP BY [Sub-Category]
HAVING SUM(Profit) < 0
ORDER BY total_profit ASC;

-- 6. Analyze profit at different discount levels
SELECT
    CASE
        WHEN Discount = 0 THEN 'No Discount'
        WHEN Discount <= 0.20 THEN 'Low Discount'
        WHEN Discount <= 0.40 THEN 'Medium Discount'
        ELSE 'High Discount'
    END AS discount_group,
    COUNT(*) AS transaction_rows,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(AVG(Profit), 2) AS average_profit
FROM superstore
GROUP BY discount_group
ORDER BY AVG(Discount);

-- 7. Find the top 10 products by profit
SELECT
    [Product Name],
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore
GROUP BY [Product Name]
ORDER BY total_profit DESC
LIMIT 10;

-- 8. Find the 10 products with the lowest profit
SELECT
    [Product Name],
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore
GROUP BY [Product Name]
ORDER BY total_profit ASC
LIMIT 10;

