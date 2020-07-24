python3 hashGen.py
git commit -a -m "Updated hash key."
git push
echo Waiting 30 seconds for page to update.
sleep 30
wget -O check.txt fratiloiu.com/key
python3 hashCheck.py
rm check.txt
rm generatedHash.txt
