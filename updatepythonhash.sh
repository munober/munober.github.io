python hashGen.py
git commit -a -m "Updated hash key."
git push
echo Waiting for page to update.
sleep 15
wget -O chech.txt fratiloiu.com/key
hashCheck.py
rm check.txt
rm generatedHash.txt