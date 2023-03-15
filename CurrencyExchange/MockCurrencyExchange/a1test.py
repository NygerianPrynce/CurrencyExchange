"""
Unit test for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: Fadhil Lawal
Date:   7/1/2020
"""
import introcs
import a1


def testA():
    result = a1.before_space("4.502 Euros")
    introcs.assert_equals('4.502', result)

    result = a1.before_space("4.502       Euros")
    introcs.assert_equals('4.502', result)

    result = a1.before_space("4.502 Euros ")
    introcs.assert_equals('4.502', result)

    result = a1.before_space(" 4.502")
    introcs.assert_equals('', result)

    result = a1.after_space("4.502 Euros")
    introcs.assert_equals('Euros', result)

    result = a1.after_space("4.502Euros ")
    introcs.assert_equals('', result)

    result = a1.after_space("4.502       Euros")
    introcs.assert_equals('      Euros', result)

    result = a1.after_space(" 4.502Euros")
    introcs.assert_equals('4.502Euros', result)


def testB():
    """
    Test procedure for Part A
    """
    result = a1.first_inside_quotes('chicken"hi"')
    introcs.assert_equals('hi', result)

    result = a1.first_inside_quotes('chicken "hi" ')
    introcs.assert_equals('hi', result)

    result = a1.first_inside_quotes('chicken""')
    introcs.assert_equals('', result)

    result = a1.first_inside_quotes('chicken" hi "')
    introcs.assert_equals(' hi ', result)

    result = a1.get_lhs('{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }')
    introcs.assert_equals("1 Bitcoin", result)

    result = a1.get_lhs('{ "ok":true, "lhs":" 1 Bitcoin ", "rhs":"9916.0137 Euros", "err":"" }')
    introcs.assert_equals(" 1 Bitcoin ", result)

    result = a1.get_lhs('{ "ok":true, "lhs":"", "rhs":"9916.0137 Euros", "err":"" }')
    introcs.assert_equals("", result)

    result = a1.get_lhs('{ "ok":true, "lhs":"   ", "rhs":"9916.0137 Euros", "err":"" }')
    introcs.assert_equals("   ", result)

    result = a1.get_rhs('{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }')
    introcs.assert_equals("9916.0137 Euros", result)

    result = a1.get_rhs('{ "ok":true, "lhs":"1 Bitcoin", "rhs":" 9916.0137 Euros ", "err":"" }')
    introcs.assert_equals(" 9916.0137 Euros ", result)

    result = a1.get_rhs('{ "ok":true, "lhs":"1 Bitcoin", "rhs":"", "err":"" }')
    introcs.assert_equals("", result)

    result = a1.get_rhs('{ "ok":true, "lhs":"1 Bitcoin", "rhs":"   ", "err":"" }')
    introcs.assert_equals("   ", result)

    result = a1.has_error('{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"Currency" }')
    introcs.assert_equals(True, result)

    result = a1.has_error('{ "ok":true, "lhs":"1 Bitcoin", "rhs":" 9916.0137 Euros ", "err":" " }')
    introcs.assert_equals(True, result)

    result = a1.has_error('{ "ok":true, "lhs":"1 Bitcoin", "rhs":"", "err":"Currency Amount" }')
    introcs.assert_equals(True, result)

    result = a1.has_error('{ "ok":true, "lhs":"1 Bitcoin", "rhs":"   ", "err":"" }')
    introcs.assert_equals(False, result)

def testC():
    """
    Test procedure for Part A
    """
    result = a1.currency_response('USD','CUP','2.5')
    introcs.assert_equals('{ "ok":true, "lhs":"2.5 United States Dollars", "rhs":"64.375 Cuban Pesos", "err":"" }', result)

    result = a1.currency_response('AED','AFN','37')
    introcs.assert_equals('{ "ok":true, "lhs":"37 United Arab Emirates Dirhams", "rhs":"808.89391183895 Afghan Afghanis", "err":"" }', result)

    result = a1.currency_response('azn','bam',42)
    introcs.assert_equals('{ "ok":true, "lhs":"42 Azerbaijani Manat", "rhs":"42.859883700441 Bosnia-Herzegovina Convertible Marks", "err":"" }', result)

    result = a1.currency_response('USD','bam',3)
    introcs.assert_equals('{ "ok":true, "lhs":"3 United States Dollars", "rhs":"5.212068 Bosnia-Herzegovina Convertible Marks", "err":"" }', result)


def testD():
    """
    Test procedure for Part A
    """
    result = a1.is_currency("USD")
    introcs.assert_equals(True, result)

    result = a1.is_currency("usd")
    introcs.assert_equals(True, result)

    result = a1.is_currency("PPP")
    introcs.assert_equals(False, result)

    result = a1.is_currency("ppp")
    introcs.assert_equals(False, result)

    result = a1.exchange('USD','CUP','2.5')
    introcs.assert_floats_equal(64.375, result)

    result = a1.exchange('AED','AFN','37')
    introcs.assert_floats_equal(808.89391183895, result)

    result = a1.exchange('azn','bam',42)
    introcs.assert_floats_equal(42.859883700441, result)

    result = a1.exchange('USD','bam',3)
    introcs.assert_floats_equal(5.212068, result)

testA()
testB()
testC()
testD()
print("Module al passed all tests")
