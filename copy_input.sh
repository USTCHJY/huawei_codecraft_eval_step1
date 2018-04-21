if [ $# != 1 ];then
	echo "Please input target dir!"
	exit 1;
fi
cp example/input.txt $1
echo "Copy input.txt Done!"
