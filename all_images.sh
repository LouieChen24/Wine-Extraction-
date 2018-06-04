for f in *.jpg; do
  python3 bounding_box.py "$f" 
  python3 run_pytess.py "$f"
done
