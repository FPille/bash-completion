import pytest


@pytest.mark.bashcomp(cmd="ether-wake")
class TestEtherWake:
    @pytest.mark.complete("ether-wake ")
    def test_1(self, completion):
        assert completion
