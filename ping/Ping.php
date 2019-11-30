<?php
/**
 * 使用PHP检测能否ping通IP或域名
 * @param type $address
 * @return boolean
 */

$url = $_GET['url'];
$check_ip = !empty($_GET['ip']) ? $_GET['ip'] : '118.190.80.179';
// ping域名
$ip = gethostbyname($url);
$data = [];
$data['url'] = $url;
$data['ip'] = $ip;
if($url == $ip)
{
    $data['status'] = 1;
}
elseif($ip == $check_ip)
{
    $data['status'] = 200;
}
else
{
    $data['status'] = 0;
}


echo json_encode($data);


