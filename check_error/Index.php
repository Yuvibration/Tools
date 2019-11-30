
<?php
$url = $_GET['url'];
$word = $_GET['word'];
$data = file_get_contents($url);
if(strpos($data,$word) !== false){
    $info['status'] = 1;
    $info['url'] = $url;
}else{
    $info['status'] = 2;
    $info['url'] = '不包含';
}

echo json_encode($info);
?>