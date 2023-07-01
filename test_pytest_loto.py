from loto_oop_magic import Random_map


class TestRandom_map:

    def test_in1(self):
        card_dog = Random_map(30, 9)
        # card_dog.print_card()
        # assert False
        try:
            assert '31' in card_dog
        except:
            assert True
        else:
            assert False

    def test_in2(self):
        card_dog = Random_map(60, 15)

        try:
            assert 61 in card_dog
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

    def test_eq(self):
        card_cat = Random_map(30, 15)
        card_mouse = Random_map(30, 15)
        card_dog = card_cat
        assert card_cat == card_dog
        assert card_cat != card_mouse
