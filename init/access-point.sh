### 1. installation

# Use the following to update your Raspbian installation:
sudo apt-get update
sudo apt-get dist-upgrade

# Install all the required software in one go with this command:
sudo apt-get install dnsmasq hostapd -y

# Since the configuration files are not ready yet, turn the new software off as follows:
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd



### 2. CONFIGURING A STATIC IP

# wlan0 is disabled by editing the configuration file
echo 'denyinterfaces wlan0' >> /etc/dhcpcd.conf

# Check the end of file section:
sudo nano /etc/dhcpcd.conf

# To configure the static IP address, edit the interfaces configuration file with:
echo 'allow-hotplug wlan0' >> /etc/network/interfaces
echo 'iface wlan0 inet static' >> /etc/network/interfaces
echo '    address 192.168.0.1' >> /etc/network/interfaces
echo '    netmask 255.255.255.0' >> /etc/network/interfaces
echo '    network 192.168.0.0' >> /etc/network/interfaces

# Check the wlan0 section:
sudo nano /etc/dhcpcd.conf

# Now restart the dhcpcd daemon and set up the new wlan0 configuration:
sudo service dhcpcd restart
sudo ifdown wlan0
sudo ifup wlan0



### 3. CONFIGURING THE DHCP SERVER (DNSMASQ)

# Rename this configuration file, and edit a new one:
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.backup
sudo touch /etc/dnsmasq.conf

# Type or copy the following information into the dnsmasq configuration file and save it
echo 'interface=wlan0      # Use the require wireless interface - usually wlan0' >> /etc/dnsmasq.conf
echo 'dhcp-range=192.168.0.2,192.168.0.20,255.255.255.0,24h' >> /etc/dnsmasq.conf

# Check the dnsmasq:
sudo nano /etc/dnsmasq.conf


### 4. CONFIGURING THE ACCESS POINT HOST SOFTWARE (HOSTAPD)

# your wireless network.
sudo touch /etc/hostapd/hostapd.conf
echo 'interface=wlan0' >> /etc/hostapd/hostapd.conf
echo 'driver=nl80211' >> /etc/hostapd/hostapd.conf
echo 'ssid=NameOfNetwork' >> /etc/hostapd/hostapd.conf
echo 'hw_mode=g' >> /etc/hostapd/hostapd.conf
echo 'channel=7' >> /etc/hostapd/hostapd.conf
echo 'wmm_enabled=0' >> /etc/hostapd/hostapd.conf
echo 'macaddr_acl=0' >> /etc/hostapd/hostapd.conf
echo 'auth_algs=1' >> /etc/hostapd/hostapd.conf
echo 'ignore_broadcast_ssid=0' >> /etc/hostapd/hostapd.conf
echo 'wpa=2' >> /etc/hostapd/hostapd.conf
echo 'wpa_passphrase=AardvarkBadgerHedgehog' >> /etc/hostapd/hostapd.conf
echo 'wpa_key_mgmt=WPA-PSK' >> /etc/hostapd/hostapd.conf
echo 'wpa_pairwise=TKIP' >> /etc/hostapd/hostapd.conf
echo 'rsn_pairwise=CCMP' >> /etc/hostapd/hostapd.conf

# Check the hostapd:
sudo nano /etc/hostapd/hostapd.conf

# We now need to tell the system where to find this configuration file.
echo 'DAEMON_CONF="/etc/hostapd/hostapd.conf"' >> /etc/default/hostapd

# Check the hostapd:
sudo nano /etc/default/hostapd


### 5. START IT UP
# Now start up the remaining services:
sudo service hostapd start
sudo service dnsmasq start
