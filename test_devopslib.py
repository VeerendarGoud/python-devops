from devopslib.radomFruit import fruit

def test_fruit():
    fruit_choice = fruit()
    assert fruit_choice in ["apple", "cherry", "strawberry"]