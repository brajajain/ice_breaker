import os
import requests


def scrape_linkedin_profiles(linkedin_profile_url: str):
    """Scrape information from LinkedIn profiles,
    Manually scrape information from the LinkedIn profile.

    Args:
        linkedin_profile_url (str): URL of the linkedin profile.
    """
    data = requests.get(linkedin_profile_url).json()

    data = {
        k: v for k, v in data.items() if v not in ([], "", None) and k not in ["people_also_view", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    linkedin_profile_url = "https://gist.githubusercontent.com/brajajain/39d2c27a8d8920fe638861b14353f819/raw/5b1c156bd716cc172f0df8703d52c88304c52017/brjain-linkedin.json"
    print(scrape_linkedin_profiles(linkedin_profile_url))
