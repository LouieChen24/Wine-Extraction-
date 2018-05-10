for f in *.jpg; do
  python3 bounding_box.py "$f" 
done
