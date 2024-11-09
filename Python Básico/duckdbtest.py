import duckdb

with duckdb.connect('prueba.db') as con:
    con.sql('DROP TABLE IF EXISTS test')
    con.sql('CREATE TABLE test(i INTEGER)')
    con.sql('INSERT INTO test VALUES (42)')
    con.table('test').show()