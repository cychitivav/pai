for ((i = 0; i < 32; i++)); do
    echo "check gpio $i"
    pigs w $i 1 r $i w $i 0 r $i w $i 1 r $i w $i 0 r $i
done
