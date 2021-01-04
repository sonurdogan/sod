x="1"
read -p "Enter number of files:" sayi
while [ $x -le  $sayi ]
do
        read -p "Enter a number or letter which is in end of the file name" son
        file_name=*$son.png
        current_time=$(date -r $file_name  "+%Y.%m.%d")
        new_fileName=$current_time."Q5Solutions"$x".png"
        cp $file_name $new_fileName
        rm $file_name
        x=$((x+1))
done
