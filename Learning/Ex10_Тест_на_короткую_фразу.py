def test_check_len_of_phrase():
    word = input('Введите любую фразу короче 15 символов: ')
    assert len(word) < 15, f'Длина фразы равна {len(word)}, в то время как должна быть короче 15'
