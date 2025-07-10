SELECT setval(
  pg_get_serial_sequence('"credenciales_credencialprograma"', 'CreProCod'),
  (SELECT MAX("CreProCod") FROM "credenciales_credencialprograma")
);