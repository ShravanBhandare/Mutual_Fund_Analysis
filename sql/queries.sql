SELECT
    d.scheme_name,
    d.fund_house,
    p.aum_crore
FROM fact_performance p
JOIN dim_fund d
ON p.amfi_code = d.amfi_code
ORDER BY p.aum_crore DESC
LIMIT 5;

SELECT
    strftime('%Y-%m', nav_date) AS month,
    ROUND(AVG(nav),2) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM fact_sip_inflows
ORDER BY month;


SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;


SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


SELECT
    d.scheme_name,
    d.fund_house,
    p.return_5yr_pct
FROM fact_performance p
JOIN dim_fund d
ON p.amfi_code = d.amfi_code
ORDER BY p.return_5yr_pct DESC
LIMIT 10;


SELECT
    d.scheme_name,
    d.fund_house,
    p.sharpe_ratio
FROM fact_performance p
JOIN dim_fund d
ON p.amfi_code = d.amfi_code
ORDER BY p.sharpe_ratio DESC
LIMIT 10;


SELECT
    d.scheme_name,
    d.fund_house,
    p.morningstar_rating
FROM fact_performance p
JOIN dim_fund d
ON p.amfi_code = d.amfi_code
ORDER BY p.morningstar_rating DESC;

SELECT
    gender,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr),2) AS total_investment
FROM fact_transactions
GROUP BY gender;



SELECT
    d.scheme_name,
    d.fund_house,
    p.sharpe_ratio,
    p.sortino_ratio
FROM fact_performance p
JOIN dim_fund d
ON p.amfi_code = d.amfi_code
ORDER BY p.sharpe_ratio DESC,
         p.sortino_ratio DESC
LIMIT 10;
