MARKER = """
unit: Mark unit tests
integration: Mark integration tests
high: High Priority
medium: Medium Priority
low: Low Priority
"""


def pytest_configure(config):
    map(lambda line: config.addinivalue_line("markes"), MARKER.split("\n"))
