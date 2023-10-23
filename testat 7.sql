SELECT
    strftime('%Y-%m-%d %H:00:00', datetime(zeitstempel, 'unixepoch')) AS datum,
    COUNT(*) AS nachrichten_anzahl
FROM
    nachricht
GROUP BY
    datum
ORDER BY
    datum;