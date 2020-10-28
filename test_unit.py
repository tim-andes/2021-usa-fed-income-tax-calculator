import pytest
import fedtaxcalc

#fedtaxcalc
@pytest.mark.parametrize("filing_status, taxable_income, expected",
                         [('single', 45000, 5448.5),
                          ('single', 100000, 18021),
                          ('single', 0, 0),
                          ('single', 100000000, 36964072.25),
                          ('married', 10000, 1000),
                          ('married', 600000, 159088.5),
                          ('married', 0, 0),
                          ('married', 100000000, 36936522.5)])
def test_calc_fex_tax(filing_status, taxable_income, expected):
    assert fedtaxcalc.calc_fed_tax(filing_status, taxable_income) == expected


@pytest.mark.parametrize("taxable_income, fed_tax_yr, expected",
                         [(45000, 5448.5, 3295.9583333333335),
                          (100000, 18021, 6831.583333333333),
                          (0, 0, 0),
                          (100000000, 36964072.25, 5252993.979166667),
                          (10000, 1000, 750),
                          (600000, 159088.5, 36742.625),
                          (0, 0, 0),
                          (100000000, 36936522.5, 5255289.791666667)])
def test_net_income_func(taxable_income, fed_tax_yr, expected):
    assert  fedtaxcalc.net_income_func(taxable_income, fed_tax_yr) == expected