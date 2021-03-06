from __future__ import absolute_import

import pytest

from icinga2 import Icinga2API
from .constants import constants


class TestHostgroups():
    @pytest.mark.run(order=1)
    def test_add(self):
        api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=True)

        result = api.usergroups.add(constants.Test_Usergroup)

        assert result['results'][0]['code'] == 200

    @pytest.mark.run(order=5)
    def test_delete(self):
        api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=True)

        result = api.usergroups.delete(constants.Test_Usergroup['name'])

        assert result['results'][0]['code'] == 200

    @pytest.mark.run(order=2)
    def test_list(self):
        api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=True)

        result = api.usergroups.list()

        assert constants.Test_Usergroup['name'] in result

    @pytest.mark.run(order=3)
    def test_exists(self):
        api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=True)

        result = api.usergroups.exists(constants.Test_Usergroup['name'])

        assert result

    @pytest.mark.run(order=4)
    def test_objects(self):
        api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=True)

        result = api.usergroups.objects()

        assert any(res.get('name', None) == constants.Test_Usergroup['name'] for res in result)
