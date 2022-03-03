import pytest
import yaml

from selenium_wework_main.pages.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    @pytest.mark.parametrize('member', yaml.safe_load(open('../data/add_member.yml', encoding="utf-8")))
    def test_add_member(self, member):
        add_member = self.main.goto_add_member()
        add_member.add_member(member)
        assert add_member.get_member(member['username'])
