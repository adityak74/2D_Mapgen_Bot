echo "Mapgen Bot v1.0"
echo "###############"

read -p "Enter the I.P address of Pi : " ip

if [[ $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  sshpass -p "pi" ssh -X pi@$ip
  python camera_loc.py -ip $ip:8081
else
  echo "fail"
fi
