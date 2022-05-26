import pytest


def test_first() -> None:
    assert 1 == 1


@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 2 == 1


@pytest.mark.skipif(4 > 1, reason='Skipped if 4 > 1')  # (True, reason='Skipped if smth is true')
def test_should_be_skipped_if_true() -> None:
    assert 2 == 2


@pytest.mark.skipif(4 < 1, reason='Skipped if 4 > 1')  # (False, reason='Skipped if smth is false')
def test_should_be_skipped_if_true() -> None:
    assert 2 == 2


@pytest.mark.xfail
def test_dont_care_if_it_fails() -> None:
    assert 2 > 4


@pytest.mark.slow
def test_with_custom_mark() -> None:  # don't forget to registrate your custom mark in pytest.ini
    pass


class Company:
    def __init__(self, name: str, stock_symbol: str):
        self.name = name
        self.stock_symbol = stock_symbol

    def __str__(self):
        return f'{self.name}:{self.stock_symbol}'


@pytest.fixture
def company() -> object:
    return Company(name='Slice of life', stock_symbol='Slice of life')


def test_with_fixture(company: object) -> None:
    print(company)


@pytest.mark.parametrize(
    'company_name',
    ['Mac', 'KFC', 'BurgerKing'],
    ids=['MAC TEST', 'KFC TEST', 'BURGERKING TEST'],  # the order takes matter
)
def test_parametrized(company_name: str) -> None:
    print(f'\nTest with {company_name}')


def raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception")


def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "CoronaVirus Exception" == str(e.value)

