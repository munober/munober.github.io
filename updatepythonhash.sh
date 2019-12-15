python hashGen.py
git commit -a -m "Updated hash key."
git push
echo Waiting for page to update.
sleep 30
wget -O check.txt fratiloiu.com/key
python hashCheck.py
rm check.txt
rm generatedHash.txt