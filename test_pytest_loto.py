from loto_oop import Random_map


class TestRandom_map:

    def test_examin1(self):
        card_dog = Random_map(30, 9)
        # card_dog.print_card()
        # assert False
        try:
            assert card_dog.examin(31)
        except:
            assert True
        else:
            assert False

    def test_examin2(self):
        card_dog = Random_map(60, 15)

        try:
            assert card_dog.examin(61)
        except AssertionError:
            assert True
        else:
            assert False

    def test_init1(self):
        card_dog = Random_map(30, 12)
        assert len(card_dog.list_1) == 4
        assert len(card_dog.list_2) == 4
        assert len(card_dog.list_3) == 4

    def test_init2(self):
        card_dog = Random_map(30, 15)
        assert card_dog.list_1[0] < card_dog.list_1[1]
        assert card_dog.list_1[1] < card_dog.list_1[2]
