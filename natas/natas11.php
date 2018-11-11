#!/usr/bin/php
<?php
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");


function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
 }
echo(xor_encrypt(base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw")));
//$original = json_encode($defaultdata);
$key = 'qw8J';

$good_data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

$good_plaintext = json_encode($good_data);
$good_ciphertext = json_encode($good_plaintext);

$cookie = base64_encode($good_ciphertext);

echo($cookie);
?>