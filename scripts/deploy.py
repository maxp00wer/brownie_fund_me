from brownie import FundMe, network, config, MockV3Aggregator
import time
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        "0xF8b0853b5e19Bc627dEC35c6F8Be51760d90c258",
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    time.sleep(1)
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
