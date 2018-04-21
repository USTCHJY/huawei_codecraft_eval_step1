echo $#
if [ $# != 3 ];then
	echo 'USAGE:sh data_prepare.sh Train_year.month Test_year.month.day length'
	exit 1;
fi

if ! [[ $1 =~ 201[5-6]+.[0-9]+ ]];then
	echo "Please input year.month!(example:2015.12)"
	exit 1;
fi
train="$1"
train_year=${train%.*}
train_month=${train#*.}
train=${train_year}_${train_month}
echo "Train:$train_year , $train_month"


if ! [[ $2 =~ 201[5-6]+.[0-9]+.[0-9]+ ]];then
	echo "Please input year.month!(example:2015.12.1)"
	exit 1;
fi
test="$2"
test_year=${test%%.*}
test_month_day=${test#*.}
test_month=${test_month_day%.*}
test_day=${test##*.}
test=${test_year}_${test_month}
echo "Test:$test_year , $test_month , $test_day"

if [ ! -d $train ];then
	mkdir $train
else
	echo "$train is exist!"
fi

start=$test_day
let end=$test_day+$3-1
echo $end
dir_name="${train}/${start}_${end}"
echo "dir_name:"$dir_name
if [ -d "$dir_name" ];then
	rm -r "$dir_name"
fi
mkdir "$dir_name"

sh copy_input.sh $dir_name

cp "raw_data/data_$train.txt" "${dir_name}/train.txt"
echo "Copy train.txt Done!"

cat "raw_data/data_$test.txt" | awk -F "[\t -]" -v start="$start" -v end="$end" '{if ($6>=start &&
		$6<=end){print $0}}' > "${dir_name}/test.txt"
echo "Write test.txt Done!"
