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
pitch = 0
roll = 0
basic.forever(function () {
    basic.pause(100)
    radio.sendValue("roll", input.acceleration(Dimension.X))
    radio.sendValue("pitch", input.acceleration(Dimension.Y))
})
