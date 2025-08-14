// SPDX-License-Identifier: MIT
pragma solidity ^0.8.21;

contract RelayControl {
    bool public relayState;

    event RelaySet(address indexed setter, bool state);

    function setRelayState(bool _state) public {
        relayState = _state;
        emit RelaySet(msg.sender, _state);
    }

    function getRelayState() public view returns (bool) {
        return relayState;
    }
}
