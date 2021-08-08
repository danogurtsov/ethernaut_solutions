from brownie import *
from .reports import *
from web3 import Web3
import binascii


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
    target = GatekeeperOne.deploy({'from': a0})

    # attacker should start with little ETH balance
    balance_to_burn = a1.balance() - 1*BIGNUMBER
    burn_address = accounts[3]
    a1.transfer(burn_address,balance_to_burn)

    REPORT.print()
    REPORT.txt_print('PRE-ATTACK STATE IS READY')
    return target

def attack(target):

    # read target's storage and unlock
    attacker = Attacker.deploy(target,{'from':a1})
    
    if target.entrant() == a1.address:
        REPORT.txt_print('ATTACK SUCCESSFUL')
    else:
        REPORT.txt_print('ATTACK IS NOT SUCCESSFUL')
