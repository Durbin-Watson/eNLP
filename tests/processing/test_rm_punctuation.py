import pytest

# Explicitly set path so don't need to run setup.py - if we have multiple copies of the code we would otherwise need
# to setup a separate environment for each to ensure the code pointers are correct.
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from enlp.processing.stdtools import rm_punctuation

import spacy

@pytest.fixture(scope="module")
def norwegian_language_model():
    return spacy.load('nb_dep_ud_sm')

@pytest.fixture(scope="module")
def english_language_model():
    return spacy.load('en_core_web_md')


# SIMPLE TESTS - lower case, no numbers
@pytest.mark.parametrize("langModel,text,expectedOutput", [
    pytest.param(english_language_model(),
                 'the quick brown fox jumped over the lazy dog.',
                 "the quick brown fox jumped over the lazy dog",
                 id='en_test1_simple'),
    pytest.param(english_language_model(),
                 'oak is strong and also gives shade.',
                 "oak strong gives shade",
                 id='en_test2_simple'),
    pytest.param(norwegian_language_model(),
                 'den raske brune reven hoppet over den late hunden.',
                 "den raske brune reven hoppet over den late hunden",
                 id='no_test1_simple'),
    pytest.param(norwegian_language_model(),
                 'eiken er sterk og gir også skygge.',
                 "eiken er sterk og gir også skygge",
                 id='no_test2_simple'),
])

def test_rm_punctuation_simple(langModel, text, expectedOutput):

    # arange - not needed

    # act
    new_text = rm_punctuation(langModel, text)

    # assert
    assert new_text == expectedOutput



# COMPLEX TESTS - mixed case, numbers
@pytest.mark.parametrize("langModel,text,expectedOutput", [
    pytest.param(english_language_model(),
                 'Cats and dogs each hate the other.',
                 "Cats and dogs each hate the other",
                 id='en_test1_complex'),
    pytest.param(english_language_model(),
                 'I better have passed that test - it is 90 percent of the class grade.',
                 "I better have passed that test it is 90 percent of the class grade",
                 id='en_test2_complex'),
    pytest.param(norwegian_language_model(),
                 'Katter og hunder hater hverandre.',
                 "Katter og hunder hater hverandre",
                 id='no_test1_complex'),
    pytest.param(norwegian_language_model(),
                 'Krana tåler maks 100 kilo.',
                 "Krana tåler maks 100 kilo",
                 id='no_test2_complex'),
])
def test_rm_punctuation_simple(langModel, text, expectedOutput):

    # arange - not needed

    # act
    new_text = rm_punctuation(langModel, text)

    # assert
    assert new_text == expectedOutput

