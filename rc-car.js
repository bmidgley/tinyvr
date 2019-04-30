# makecode.microbit.org
let roll = 0
let pitch = 0
radio.onReceivedValue(function (name, value) {
    if (name == "roll") {
        roll = value / 22
    } else if (name == "pitch") {
        pitch = (0 - value) / 22
    }
    pins.servoWritePin(AnalogPin.P1, 90 + (pitch + roll))
    pins.servoWritePin(AnalogPin.P2, 90 - (pitch - roll))
})
radio.setGroup(55)
