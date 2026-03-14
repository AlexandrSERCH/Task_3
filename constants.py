BASE_URL = "https://stellarburgers.education-services.ru"

URLS = {
    "site": f"{BASE_URL}",
    "login_page": f"{BASE_URL}/login",
    "forgot_password_page": f"{BASE_URL}/forgot-password",
    "reset_password_page": f"{BASE_URL}/reset-password",
    "order_feed": f"{BASE_URL}/feed",
    "account_profile_page": f"{BASE_URL}/account/profile",
}

API_ENDPOINTS = {
    "create_user": f"{BASE_URL}/api/auth/register",
    "delete_user": f"{BASE_URL}/api/auth/user"
}


def site_url():
    return URLS["site"]


def login_page_url():
    return URLS["login_page"]


def forgot_password_url():
    return URLS["forgot_password_page"]


def reset_password_url():
    return URLS["reset_password_page"]


def order_feed_url():
    return URLS["order_feed"]


def account_profile_url():
    return URLS["account_profile_page"]


def create_user_endpoint():
    return API_ENDPOINTS["create_user"]


def delete_user_endpoint():
    return API_ENDPOINTS["delete_user"]
