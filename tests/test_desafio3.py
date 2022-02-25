from desafio3 import count_anagram


def teste_se_parametro_da_funcao_count_anagram_e_string():
    assert count_anagram(123) is False


def teste_se_o_retorno_da_funcao_count_anagram_e_inteiro():
    assert type(count_anagram("ovo")) == int


def teste_se_dado_uma_string_a_funcao_retorna_o_numero_de_anagramas():
    assert count_anagram("ovo") == 2
    assert count_anagram("ifailuhkqq") == 3
    assert count_anagram("abba") == 4
