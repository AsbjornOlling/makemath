#!/bin/bash
script_dir="/home/asbjorn/Scripts/markmath"
temp_file_name="temp.html"
temp_file_path="$script_dir/$temp_file_name"

markdown_file="$1"
pdf_file="${markdown_file::-3}"".pdf"

echo Converting "$markdown_file to $pdf_file, with sexy math"
python $script_dir/markmath.py $markdown_file > $temp_file_path && pandoc $temp_file_path -o $pdf_file
