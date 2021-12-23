import pytest
from IndianStatesCensusException import IndianStatesCensusException
from main import state_census_problem, count_records

class TestIndianStateCensusProblem:
    csv_file = 'D:/BrizePython/IndianStatesCencusProblem/IndianCensus - Sheet1.csv'

    @pytest.fixture()
    def test_indian_states_census(self):
        data = state_census_problem()
        return data

    def test_match_records(self, test_indian_states_census):
        expected = test_indian_states_census.count_records(self.csv_file)
        assert expected == 29


