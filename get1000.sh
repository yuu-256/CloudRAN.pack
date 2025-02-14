#!/bin/bash

# Mesure time
start=`date +%s`

echo "Generating 1000 cloud fields..."

# Get cloud field at 1000 random seed values
for i in {2000..9999}
do
    # Get random seed value
    seed_value=$((RANDOM % 10000))

    # Execute python code, save output to file
    python3 cloudgen.py "../../data/cloudgen/deep_fields_3/output_$i" $seed_value

    # Print progress
    echo "Progress: $((i+1))/1000"
done

echo "Done!"

end=`date +%s`
runtime=$((end-start))
echo "Runtime: $runtime"
