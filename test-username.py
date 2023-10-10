import unittest
from unittest.mock import patch
from username import get_user_repositories_with_commits

class TestGitHubAPI(unittest.TestCase):

    @patch('username.fetch_data_from_github')
    @patch('username.count_commits')
    def test_get_user_repositories_with_commits(self, mock_count_commits, mock_fetch_data_from_github):
        mock_fetch_data_from_github.return_value = [
            {'name': 'repo1'},
            {'name': 'repo2'}
        ]
        mock_count_commits.side_effect = [3, 5]

        result = get_user_repositories_with_commits('testuser')

        self.assertEqual(result, [
            {"Repo": "repo1", "Number of commits": 3},
            {"Repo": "repo2", "Number of commits": 5}
        ])

if __name__ == '__main__':
    unittest.main()
