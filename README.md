# Competition Mode USB
An implementation of the Metadata USBs in CircuitPython using LilyGo T-Dongle S3.

## __DO NOT EDIT FILES ON COMP_USB__
You will notice that COMP_USB is only around 50kB so if editors try to generate cache files they quickly fill the disk.
Additionally the microcontroller resets when files are edited to load in their changes which can cause editors to corrupt the files.
Instead, edit the files on your computer and copy the updated files across.

If you did not heed this warning and have broken the drive follow [these instructions](https://learn.adafruit.com/welcome-to-circuitpython/troubleshooting#circuitpy-drive-issues-2978456-26) to erase the filesystem and start again.

# Understanding the Reset Modes

Pressing the reset button while using the dongle can enter different modes.
The important thing to remember is that if screen is not displaying a corner colour, you are not in the operating mode.
Pressing reset once should restart the dongle back into operating mode.

If you hold down the reset button the dongle will not start until the button is released.
Pressing the reset button within 1 second of boot will enter safe mode and the USB drive will show up read-write while the screen remains blank.
All these modes can be exited by pressing the reset button once.

# Other Notes

## Debugging errors
Since we've disabled the serial terminal you cannot normally view what error is causing the dongle to crash.
A workaround for this is to boot into safe mode, which will re-enable the serial terminal.

Once you connect to the serial terminal, press a key to enter the REPL and enter `import code`.
This will run the standard code and allow you to view the error.

Note, generally the import command will not return so use Ctrl-C to be able to enter more commands.
