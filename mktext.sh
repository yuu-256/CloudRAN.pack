#!/bin/bash

# Mesure time
start=`date +%s`

echo "Writing 1000 imput files..."

# Get cloud field at 1000 random seed values
for i in {0..999}
do
    # Execute python code, save output to file
    python3 mktext_input.py "out_field/output_$i.npy" "out_text/output_$i.txt"

    # Print progress
    echo "Progress: $((i+1))/1000"
done

echo "Done!"

end=`date +%s`
runtime=$((end-start))
echo "Runtime: $runtime"

