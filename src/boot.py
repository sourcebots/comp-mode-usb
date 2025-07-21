"""
boot.py

This file is executed before the USB connection is setup so we can alter what
USB devices are created.
"""
import busio
import board
import os
import json
import sdcardio
import storage
import usb_cdc

# Make USB mount read-only (to host), this can only be done in boot.py
storage.remount('/', readonly=False)  # readonly here applies to MCU not host

# Set the name the mass storage appears as,
# this can only be done while the storage is writable to the microcontroller
m = storage.getmount("/")
if m.label != 'COMP_USB':
    m.label = "COMP_USB"

# Mount SD card
sd_spi = busio.SPI(board.SD_SCK, board.SD_CMD, board.SD_D0)
try:
    sd = sdcardio.SDCard(sd_spi, board.SD_D3)
except OSError:
    print("No SD card")
else:
    sd_vfs = storage.VfsFat(sd)
    storage.mount(sd_vfs, '/sd')

# Update stored values from SD
if 'metadata.json' in os.listdir('/sd'):
    print('Updating metadata')
    try:
        with open('/sd/metadata.json') as fp:
            config = fp.read()
            data = json.loads(config)

        assert 'zone' in data
        assert 'is_competition' in data

        try:
            with open('metadata.json') as fp:
                old_config = fp.read()
                old_data = json.loads(old_config)
        except Exception:
            old_data = {}

        if old_data != data:
            with open('metadata.json', 'w') as fp:
                json.dump(data, fp)
    except Exception as e:
        print('Update failed', e)
    finally:
        # Unmount SD card
        storage.umount(sd_vfs)

# Uncomment to have writable drive
# storage.remount('/', readonly=True)  # readonly here applies to MCU not host

# Disable serial console
# usb_cdc.disable()
