#!/bin/bash

# Mesure time
start=`date +%s`

echo "Writing 1000 imput files..."

# Get cloud field at 1000 random seed values
for i in {0..999}
do
    # Execute python code, save output to file
    python3 mktext_input.py "out_field2/output_$i.npy" "out_text2/output_$((i+1000)).txt"

    # Print progress
    echo "Progress: $((i+1))/1000"
done

echo "Done!"

end=`date +%s`
runtime=$((end-start))
echo "Runtime: $runtime"

