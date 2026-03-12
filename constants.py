BASE_URL = "https://stellarburgers.education-services.ru"

URLS = {
    "site": f"{BASE_URL}",
    "login_page": f"{BASE_URL}/login",
    "forgot_passwrod_page": f"{BASE_URL}/forgot-password",
    "reset_passwrod_page": f"{BASE_URL}/reset-password",
}

API_ENDPOINTS = {
    "create_user": f"{BASE_URL}/api/auth/register",
    "delete_user": f"{BASE_URL}/api/auth/user"
}


def site_url():
    return URLS["site"]


def login_page_url():
    return URLS["login_page"]


def forgot_passwrod_url():
    return URLS["forgot_passwrod_page"]


def reset_passwrod_url():
    return URLS["reset_passwrod_page"]

def create_user_endpoint():
    return API_ENDPOINTS["create_user"]

def delete_user_endpoint():
    return API_ENDPOINTS["delete_user"]