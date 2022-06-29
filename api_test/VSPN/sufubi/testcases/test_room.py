import pytest

from VSPN.sufubi.api.room import Room


class TestRoom():

    room_id = 100435

    def setup(self):
        self.room = Room()

    # @pytest.mark.run(order=-1)
    # def test_process(self):
    #     re = self.room.create().join().detail().exit()
    #     assert re.status_code == 200

    # @pytest.mark.first
    def test_create_room(self):
        re = self.room.create()
        global room_id
        room_id = re["room_id"]

    def test_join_room(self):
        self.room.join(100507)

    def test_room_detail(self):
        self.room.detail(room_id)

    # @pytest.mark.parametrize("room_id", [(room_id)])
    def test_update_room(self):
        # game_loan: 传0表示不贷款，默认贷款
        re = self.room.update_room(room_id, 5, 0)
        assert re.status_code == 200
        self.room.detail(room_id)

    def test_ready(self):
        re = self.room.ready(room_id)
        assert re.status_code == 200

    def test_cancel_ready(self):
        re = self.room.cancel_ready(room_id)
        assert re.status_code == 200

    def test_exit(self):
        result = self.room.exit(room_id)
        # 退出后再调退出也没报错
        assert result.status_code == 200

    def test_room_list(self):
        result = self.room.room_list()
        print("roomlist_result: ", result)

    def test_quick_join(self):
        """传 0 表示加入拍卖艺术"""
        room_id = self.room.quick_join()["room_id"]
        print("quick join room_id: ", room_id)
        self.room.exit(room_id)

    def test_room_search(self):
        re = self.room.room_search(self.room_id)
        print("search_result: ", re)

    @pytest.mark.skip
    def test_kick_people(self):
        self.room.kick_people(self.room_id, 10000)


