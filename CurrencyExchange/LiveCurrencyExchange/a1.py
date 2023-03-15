
"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: Fadhil Lawal
Date:   7/1/2020
"""

import introcs

def before_space(s):
    """Returns a copy of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    word = s.index(" ")
    actual = s[:word]
    return actual


def after_space(s):
    '''Returns a copy of s after the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space'''

    word = s.index(" ")
    actual2 = s[word+1:]
    return actual2


def first_inside_quotes(s):
    '''Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that
    delimits it.  We typically use single quotes (') to delimit a
    string if we want to use a double quote character (") inside of it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C',
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes'''
    word = s.index("\"")
    actual = s[word+1:]
    mword = actual.index("\"")
    return actual[:mword]


def get_lhs(json):
    '''Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "lhs". For example, if the JSON is
    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query'''
    result = json.find('lhs')
    json = json[result + 6:]
    result2 = json.index(",")
    json = json[:result2-1]
    return json


def get_rhs(json):
    '''Returns the rhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "rhs". For example, if the JSON is

    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'

    then this function returns '9916.0137 Euros' (not
    '"9916.0137 Euros"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query'''
    result = json.find('rhs')
    json = json[result + 6:]
    result2 = json.index(",")
    json = json[:result2-1]
    return(json)


def has_error(json):
    '''Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the
    opposite of the value following the keyword "ok". For example,
    if the JSON is

    '{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }'

    then the query is not valid, so this function returns True (It
    does NOT return the message 'Source currency code is invalid').

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query'''
    result = json.find('err')
    json = json[result + 5:]
    json = first_inside_quotes(json)
    return(json != "")


def currency_response(src, dst, amt):
    '''Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the
    currency dst. The response should be a string of the form

    '{ "ok":true, "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'

    where the values old-amount and new-amount contain the value
    and name for the original and new currencies. If the query is
    invalid, both old-amount and new-amount will be empty, while
    "ok" will be followed by the value false (and "err" will have
    an error message).

    Parameter src: the currency on hand (the LHS)
    Precondition: src is a string with no spaces or non-letters

    Parameter dst: the currency to convert to (the RHS)
    Precondition: dst is a string with no spaces or non-letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float'''
    url = ('http://cs1110.cs.cornell.edu/2019fa/xchg?src=USD&dst=CUP&amt=2.5')
    url = url.replace("USD", src.upper())
    url = url.replace("CUP", dst.upper())
    url = url.replace("2.5", (str(amt)).upper())
    return introcs.urlread(url)


def is_currency(code):
    '''Returns: True if code is a valid (3 letter code for a) currency
    It returns False otherwise.

    Parameter code: the currency code to verify
    Precondition: code is a string with no spaces or non-letters.'''
    url = ('http://cs1110.cs.cornell.edu/2019fa/xchg?src=USD&dst=CUP&amt=2.5')
    code = code.upper()
    chi = url.replace("USD", code)
    json = introcs.urlread(chi)
    res = not(has_error(json))
    return res


def exchange(src, dst, amt):
    '''Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency 
    src to the currency dst. The value returned represents the 
    amount in currency dst.

    The value returned has type float.

    Parameter src: the currency on hand (the LHS)
    Precondition: src is a string for a valid currency code
        
    Parameter dst: the currency to convert to (the RHS)
    Precondition: dst is a string for a valid currency code
        
    Parameter amt: amount of currency to convert
    Precondition: amt is a float'''
    json = currency_response(src, dst, str(amt))
    res = before_space((get_rhs(json)))
    return float(res)
