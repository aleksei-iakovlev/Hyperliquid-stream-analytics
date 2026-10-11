from hyperliquid.info import Info
from hyperliquid.utils import constants

account_address = "0x5d3BDD5b2A9A460772B02537A1ec454e1E2b73A6"


def get_user_state(account_address):
    info = Info(constants.MAINNET_API_URL, skip_ws=True)
    user_state = info.user_state(account_address)
    return user_state


if __name__ == '__main__':
    user_state = get_user_state(account_address)
    print(user_state)
