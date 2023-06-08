from random import randint

import pytest

from mysqlsb.builder import MySQLStatementBuilder
from mysqlsb import Sort


def test_insert_statement():
    stmnt = MySQLStatementBuilder(None)
    val_a = randint(0, 100)
    val_b = randint(0, 100)
    val_c = randint(0, 100)
    stmnt.insert('test_table', ['col_a', 'col_b', 'col_c']).set_values([val_a, val_b, val_c])

    print("The query: ")
    print(stmnt.query)
    assert stmnt.query == 'INSERT INTO `test_table` (`col_a`, `col_b`, `col_c`) VALUES (%s, %s, %s) '
    assert stmnt.values == [val_a, val_b, val_c]


def test_insert_statement_multiple():
    stmnt = MySQLStatementBuilder(None)
    val_a = randint(0, 100)
    val_b = randint(0, 100)
    val_c = randint(0, 100)
    val_d = randint(0, 100)

    stmnt.insert('test_table', ['col_a', 'col_b'])
    stmnt.set_values([[val_a, val_b], [val_c, val_d]])

    assert stmnt.query == 'INSERT INTO `test_table` (`col_a`, `col_b`) VALUES (%s, %s), (%s, %s) '
    assert stmnt.values == [val_a, val_b, val_c, val_d]


def test_bad_insert_statement():
    stmnt = MySQLStatementBuilder(None)
    stmnt.insert('test_table', ['col_a', 'col_b', 'col_c'])

    with pytest.raises(TypeError):
        stmnt.set_values('a', 'b', 'c')

    with pytest.raises(TypeError):
        stmnt.set_values(1, 2, 3)


# Write unit tests for the rest of the builder methods
def test_select_statement():
    stmnt = MySQLStatementBuilder(None)
    stmnt.select('test_table', ['col_a', 'col_b', 'col_c'])

    assert stmnt.query == 'SELECT `col_a`,`col_b`,`col_c` FROM test_table '
    assert stmnt.values == []


def test_count_statement():
    stmnt = MySQLStatementBuilder(None)
    stmnt.count('test_table')

    assert stmnt.query == 'SELECT COUNT(*) as count FROM test_table '
    assert stmnt.values == []


def test_update_statement():
    stmnt = MySQLStatementBuilder(None)
    stmnt.update('test_table', 'col_a = %s', [33])

    assert stmnt.query == 'UPDATE test_table SET col_a = %s '
    assert stmnt.values == [33]


def test_delete_statement():
    stmnt = MySQLStatementBuilder(None)
    stmnt.delete('test_table')

    print("The query: ")
    print(stmnt.query)
    assert stmnt.query == 'DELETE FROM test_table '
    assert stmnt.values == []


def test_order_by_statement():
    stmnt = MySQLStatementBuilder(None)
    stmnt.order_by(['col_a', 'col_b'], Sort.ASCENDING)

    print("The query: ")
    print(stmnt.query)
    assert stmnt.query == 'ORDER BY `col_a`, `col_b` ASC '
    assert stmnt.values == []


def test_complex_query():
    stmnt = MySQLStatementBuilder(None)
    stmnt.select('test_table', ['col_a', 'col_b', 'col_c'])

    value_a = randint(0, 100)
    value_b = randint(0, 100)
    random_limit = randint(0, 100)
    random_offset = randint(0, 100)

    stmnt.where('col_a = %s, col_b = %s', [value_a, value_b])
    stmnt.order_by(['col_c', 'col_d'], Sort.DESCENDING)
    stmnt.limit(random_limit)
    stmnt.offset(random_offset)

    print("The query: ")
    print(stmnt.query)
    assert stmnt.query == f'SELECT `col_a`,`col_b`,`col_c` FROM test_table WHERE col_a = %s, col_b = %s ORDER BY `col_c`, `col_d` DESC LIMIT {random_limit} OFFSET {random_offset} '
    assert stmnt.values == [value_a, value_b]
