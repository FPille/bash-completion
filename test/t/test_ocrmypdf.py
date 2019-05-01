import pytest


class TestOcrmypdf:
    @pytest.mark.complete("ocrmypdf ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ocrmypdf --")
    def test_2(self, completion):
        assert completion
