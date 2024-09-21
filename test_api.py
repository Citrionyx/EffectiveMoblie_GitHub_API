import os
import unittest

import requests
from dotenv import load_dotenv


class TestGitHubAPI(unittest.TestCase):
    def load_env(self):
        load_dotenv()

        self.GITHUB_API_URL = "https://api.github.com"
        self.assertTrue(self.GITHUB_API_URL, "Failed to load GITHUB_API_URL from .env")

        self.USERNAME = os.getenv("GITHUB_USERNAME")
        self.assertTrue(self.USERNAME, "Failed to load USERNAME from .env")

        self.TOKEN = os.getenv("GITHUB_TOKEN")
        self.assertTrue(self.TOKEN, "Failed to load TOKEN from .env")

        self.REPO_NAME = os.getenv("REPO_NAME")
        self.assertTrue(self.REPO_NAME, "Failed to load REPO_NAME from .env")

    def create_repository(self):
        url = f"{self.GITHUB_API_URL}/user/repos"
        headers = {
            "Authorization": f"token {self.TOKEN}",
            "Accept": "application/vnd.github+json",
        }
        data = {
            "name": self.REPO_NAME,
            "private": False,
        }

        response = None
        try:
            response = requests.post(url, json=data, headers=headers)
        except:
            pass

        self.assertTrue(response, f"Failed a request to {url}")
        self.assertEqual(response.status_code, 201, f"Failed to create repository: {response.json()}")

    def check_repository_exists(self):
        url = f"{self.GITHUB_API_URL}/repos/{self.USERNAME}/{self.REPO_NAME}"
        headers = {
            "Authorization": f"token {self.TOKEN}",
            "Accept": "application/vnd.github+json",
        }

        response = None
        try:
            response = requests.get(url, headers=headers)
        except:
            pass

        self.assertTrue(response, f"Failed a request to {url}")
        self.assertEqual(response.status_code, 200, f"Repository '{self.REPO_NAME}' does not exist.")

    def delete_repository(self):
        url = f"{self.GITHUB_API_URL}/repos/{self.USERNAME}/{self.REPO_NAME}"
        headers = {
            "Authorization": f"token {self.TOKEN}",
            "Accept": "application/vnd.github+json",
        }

        response = None
        try:
            response = requests.delete(url, headers=headers)
        except:
            pass

        self.assertTrue(response, f"Failed a request to {url}")
        self.assertEqual(response.status_code, 204, f"Failed to delete repository: {self.REPO_NAME}")

    # Test function that goes through the entire process with assertions
    def test_api(self):
        self.load_env()
        self.create_repository()
        self.check_repository_exists()
        self.delete_repository()


if __name__ == "__main__":
    unittest.main()
