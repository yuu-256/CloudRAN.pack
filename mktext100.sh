#!/bin/bash

# Mesure time
start=`date +%s`

echo "Writing 1000 imput files..."

# Get cloud field at 1000 random seed values
for i in {1000..1999}
do
    # Execute python code, save output to file
    python3 mktext_input.py "../../data/cloudgen/deep_fields_norm_2/output_$i.npy" "../../data/mcstar_in/intext100_2/output_$i.txt"

    # Print progress
    echo "Progress: $((i+1))/1000"
done

echo "Done!"

end=`date +%s`
runtime=$((end-start))
echo "Runtime: $runtime"

