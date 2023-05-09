# Dual boot Ubuntu and Window 11 💻 
Dual booting Windows and Linux on the same computer can be a great solution to enjoy the unique benefits of both operating systems without sacrificing any features, and it is possible to do it without losing any data, although it requires careful partitioning of the hard disk drive (HDD) or solid-state drive (SSD), as well as following a detailed installation process.


## Shrink the Windows partition to make space for Ubuntu:

Firstly, it is necessary to shrink the Windows partition to make space for Ubuntu. To do this

- Right-click on the Start menu and select Disk Management
- Choose the main drive (C:)
- Right-click on it and select Shrink Volume
- Choose how much space to allocate and click Shrink


## Download the Ubuntu ISO file and create a bootable USB drive:

You need to download the Ubuntu ISO file from the official website. You can choose between the LTS (Long-Term Support) or the latest version, depending on your needs. Once you've downloaded the file, you'll need to create a bootable USB drive (of minimum 8gb) with a tool like Rufus or Etcher.

- Install tools like Rufus and open it
- Select the USB drive and the ISO file
- Choose GPT in the partition scheme
- Click Start to create the bootable drive


## Boot from the USB drive and prepare for installation:

Once the ISO file preparation is done. It's the time to boot from the USB drive. Insert the USB drive and restart your computer, press the key(F12) that takes you to the boot menu. 

- Look for the Secure Boot option and disable it
- Save changes and exit the BIOS setup
- Again come in BIOS menu and boot the USB drive, Ubuntu logo will appear and you'll be able to see Ubuntu UI
- Select try Ubuntu and choose the language, keyboard layout
- Don't install directly, first check if your sound, wifi connection and everything else is working
- Choose to install third-party software for graphics and Wi-Fi hardware, if desired, and click "Continue".


## Install Ubuntu alongside Windows or create custom partitions:

The next step is very crucial, you need to manipulate the space and divide it. For this follow the exact steps in this [video](https://www.youtube.com/watch?v=5mfYj6uE1z0&ab_channel=TechnoBaazi).

- On the installation type screen, choose the option to install Ubuntu alongside Windows (dual boot) or select Something Else if you want to create custom partitions for Ubuntu.
- If you choose Something Else, you'll need to create two new partitions: 
    - One for the root directory ("/") with at least 20 GB of space
    - One for the swap area with twice the size of your RAM

- Optionally, create a separate partition for the home directory (/home) to keep personal files and settings separate from system files.


## Set up and complete the installation:

- Set up your time zone, username, and password
- Click "Continue" and wait for the installation to complete
- Restart your computer
- You should now have the option to boot into either Windows or Ubuntu

It is important to note that the installation process may vary depending on the computer's hardware and software configurations, and some problems may arise during the process. Therefore, it is recommended to follow the instructions carefully and seek assistance from reliable sources if needed.
