sudo cp ./painbot-updater.service /etc/systemd/system/painbot-updater.service
sudo systemctl enable painbot-updater.service
sudo systemctl start painbot-updater.service