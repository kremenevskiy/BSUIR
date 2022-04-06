a = tail -n 
while IFS="," read -r rec_column1 rec_column2 rec_column3
do
  echo "Displaying Record-$rec_column1"
  echo "Quantity: $rec_column2"
  echo "Price: $rec_column3"
  echo ""
done < {tail -n 1 data.csv}


kate = ['love, mouse', 'kissa']

