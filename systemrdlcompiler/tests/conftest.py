import tests.parser_test_validations_strings

def pytest_generate_tests(metafunc):
    test_strings = tests.parser_test_validations_strings.test_strings
    if 'error_rdl' in metafunc.fixturenames and  'error_msg' in metafunc.fixturenames:
        metafunc.parametrize('error_rdl,error_msg', [x for x in test_strings])
