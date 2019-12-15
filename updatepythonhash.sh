python hashGen.py
git commit -a -m echo hashTimestamp.txt
git push
echo Waiting for page to update.
sleep 15
python hashCheck.py