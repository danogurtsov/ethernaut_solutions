// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import './GatekeeperOne.sol';

contract Attacker {

  address payable target;
  address public deployer;

  constructor (address payable _target) public payable {
    target = _target;
    deployer = msg.sender;
  }

  function attack(bytes32 password) public {
    GatekeeperOne(target);
    }

}
