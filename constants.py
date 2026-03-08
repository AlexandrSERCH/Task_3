BASE_URL = "https://stellarburgers.education-services.ru"

URLS = {
    "site": f"{BASE_URL}",
    "login_page": f"{BASE_URL}/login",
    "forgot_passwrod_page": f"{BASE_URL}/forgot-password",
    "reset_passwrod_page": f"{BASE_URL}/reset-password",
}


def site_url():
    return URLS["site"]


def login_page_url():
    return URLS["login_page"]


def forgot_passwrod_url():
    return URLS["forgot_passwrod_page"]


def reset_passwrod_url():
    return URLS["reset_passwrod_page"]
