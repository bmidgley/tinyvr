# makecode.microbit.org
radio.setGroup(55)
basic.forever(function () {
    basic.pause(100)
    radio.sendValue("roll", input.acceleration(Dimension.X))
    radio.sendValue("pitch", input.acceleration(Dimension.Y))
})
