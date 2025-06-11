from unittest.mock import Mock
from lib.cat_facts import CatFacts

def test_mock_call_api_for_cat_fact():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {
        "fact":"The heaviest cat on record is Himmy, a Tabby from Queensland, Australia. He weighed nearly 47 pounds (21 kg). He died at the age of 10.",
        "length":135
    }
    
    cat_fact = CatFacts(requester_mock)
    result = cat_fact.provide()
    assert result == "Cat fact: The heaviest cat on record is Himmy, a Tabby from Queensland, Australia. He weighed nearly 47 pounds (21 kg). He died at the age of 10."
