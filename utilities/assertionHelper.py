class AssertionHelper:

    @staticmethod
    def verify_equal(expected, actual, message=""):
        assert expected == actual, \
            f"{message}\n\nExpected: {expected}\nActual: {actual}"

    @staticmethod
    def verify_contains(expected, actual, message=""):
        assert expected in actual, \
            f"{message}\n\nExpected '{expected}' in '{actual}'"

    @staticmethod
    def verify_not_contains(expected, actual, message=""):
        assert expected not in actual, \
            f"{message}\n\nDid not expect '{expected}' in '{actual}'"

    @staticmethod
    def verify_true(condition, message=""):
        assert condition, message

    @staticmethod
    def verify_false(condition, message=""):
        assert not condition, message

    @staticmethod
    def verify_not_none(value, message=""):
        assert value is not None, message

    @staticmethod
    def verify_none(value, message=""):
        assert value is None, message

    @staticmethod
    def verify_empty(text, message=""):
        assert text == "", message

    @staticmethod
    def verify_not_empty(text, message=""):
        assert text != "", message