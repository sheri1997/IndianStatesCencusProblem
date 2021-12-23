import pytest
from IndianStatesCensusException import IndianStatesCensusException
from main import IndianStatesCensus


class TestIndianStateCensusProblem:
    csv_file = 'D:/BrizePython/IndianStatesCencusProblem/IndianCensus - Sheet1.csv'
    txt_file = 'D:/BrizePython/IndianStatesCencusProblem/IndianCensus - Sheet1.txt'

    @pytest.fixture()
    def test_indian_states_census(self):
        data = IndianStatesCensus()
        return data

    def test_match_records(self, test_indian_states_census):
        expected = test_indian_states_census.count_records(self.csv_file)
        assert expected == 29

    def test_match_extention(self, test_indian_states_census):
        actual = test_indian_states_census.csv_file_correct(self.csv_file)
        expected = '.csv'
        assert actual == expected

    def test_unmatch_extention(self, test_indian_states_census):
        with pytest.raises(IndianStatesCensusException) as exception:
            test_indian_states_census.csv_file_correct(self.txt_file)
        assert exception.value.message == "Invalid File Name"

    def test_delimitor(self, test_indian_states_census):
        expected = ','
        accual = test_indian_states_census.delimitor(self.csv_file)
        assert accual == expected

    def test_not_delimitor(self, test_indian_states_census):
        with pytest.raises(IndianStatesCensusException) as exception:
            test_indian_states_census.delimitor(self.txt_file)
        assert exception.value.message == "Delimitor Not Matched"

    def test_header(self, test_indian_states_census):
        expected = True
        accual = test_indian_states_census.header_validate(self.csv_file)
        assert accual == expected

    def test_not_header(self, test_indian_states_census):
        with pytest.raises(IndianStatesCensusException) as exception:
            test_indian_states_census.header_validate(self.txt_file)
        assert exception.value.message == "Header Not Matched"




